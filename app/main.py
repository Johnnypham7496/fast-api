from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# dictionary that we created at the beginning to use as a example
my_post = [
    {"title": "title of post 1", "content": "content of post 1", "id": 1}, 
    {"title": "favorite foods", "content": "I like Pizza", "id": 2}
]


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

# code below is consider a path operation/route
@app.get("/")     # get is sending a get request to the api. There are other decoratores that can be used such as POST, PUT, DELETE, GET
def root():              # the name for the function does not matter but preferred to be descriptive
    return {"message": "Hello World"}      # this is the data that is sent back to the user, this can be changed


# decorators can be changed to which ever extension the user prefers such as instead of "/" they can use "/johnny", this is how multiple pages are created
# the decorator must also be changed in the website url for the user to be able to hit the end point otherwise it would be a user error

# order will matter when having a code that has multiple paths for url's because the code will always read from top down to find the matching one
@app.get("/posts/latest")
def get_latest_post():
    post = my_post[len(my_post)-1]
    return post


