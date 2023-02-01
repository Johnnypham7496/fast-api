from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import database, schemas, models, utils, oauth2

# this is a router to the main.py file, help us manage our code better by splitting into different files rather than keeping everything in main
# tags is a goruping for swagger ui incase someone views our code and wants to know what each sections contains
router  = APIRouter(tags = ['Authentication'])

# the session must be added to the function for the code to access the database
@router.post('/login', response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):

    # this code is the hashed password from the database that we will use in the verify function to compare the hashed password in the database and the one the user is entering
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail = f'Invalid Credentials')

    # this is the function we call to verify the passwords from the user and the database
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail = f'Invalid Credentials')

    # create a token and return the token value
    # the data being pased into the payload below is just the user_id. Extra information can be added if you choose
    access_token = oauth2.create_access_token(data= {"user_id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}