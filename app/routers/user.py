from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, utils
from ..database import get_db


# prefix will give you the option to instead of having multiple routes with the same name, you can have a prefix and then additional add ons such as id
# tag will group the routes together when you view the code in swagger ui making the layout easier to the eye
router = APIRouter(
    prefix = "/users",
    tags = ["Users"]
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model = schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    # hash the password - user.password 
    # for the hash property to work you need to pip install passlib[bcrypt] and import the libraries into the main file 
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.dict())  # adding **post.dict will help the main code read all the feilds that are related to model instead of having to type the scheme out individually
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.get('/{id}', response_model= schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail= f'User with id {id} does not exist')
    
    return user