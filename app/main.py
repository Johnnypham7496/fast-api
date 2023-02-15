from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

# models.Base.metadata.create_all(bind=engine) we no longer this line because of alembic. This line would run and create all the models associated with out model.py

app = FastAPI()

# 2 code below if for the appmiddleware so other sites can access our api such as google, youtube, etc. This can also be set for specific sites
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    return {"message": "Hello World!!!!"}      # this is the data that is sent back to the user, this can be changed


# decorators can be changed to which ever extension the user prefers such as instead of "/" they can use "/johnny", this is how multiple pages are created
# the decorator must also be changed in the website url for the user to be able to hit the end point otherwise it would be a user error

# order will matter when having a code that has multiple paths for url's because the code will always read from top down to find the matching one
@app.get("/posts/latest")
def get_latest_post():
    post = my_post[len(my_post)-1]
    return post


