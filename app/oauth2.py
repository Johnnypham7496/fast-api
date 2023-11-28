from jose import JWTError, jwt
from datetime import datetime, timedelta
from . import schemas, database, models
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl= 'login')

# SECRET_KEY: this key is something that resides only in the api and nowhere else for verification purposes. The User will not know this
# Algorithum: 'HS256'
# Expiration time: giving a token to a user without an expiration time could leave them logged in forever 

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithum
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

# function below is what created the token access 
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    # the code below is the code that is used to create the jwt token: 1. everything that we want to enter into the payload, secret key, algorithum
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# the code below will take the token that came from get_current_user and decodes the jwt token data, extracts the id from the token, then verifies the id. If there is no id then it will raise a error
def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms= [ALGORITHM])

        id: str = payload.get("user_id")
        if id is None:
            raise credentials_exception
        token_data = schemas.TokenData(id=id)

    except JWTError:
        raise credentials_exception
    
    return token_data

# code below takes the token taken from the path op and checks it into the verify_access_token function
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):

    # this is error message that we be used if the token is no verified properly in the verify_access_token
    credentials_exception = HTTPException(status_code= status.HTTP_401_UNAUTHORIZED, detail=f"Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
    token = verify_access_token(token, credentials_exception)
    # this code underneath will associate the user id with the token id 
    user = db.query(models.User).filter(models.User.id == token.id).first()
    return user
