from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Optional
from .. import models, schemas, oauth2
from ..database import get_db



# prefix will give you the option to instead of having multiple routes with the same name, you can have a prefix and then additional add ons such as id
# tag will group the routes together when you view the code in swagger ui making the layout easier to the eye
router = APIRouter(
    prefix = "/posts", 
    tags = ['Posts']
)


# @router.get("/", response_model = List[schemas.Post])
@router.get("/", response_model=List[schemas.PostOut])
def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ''):  # created 3 arguments, a limit to how many posts can bbe retrieved, skipping over posts, and to search by a str    
#    cursor.execute("""SELECT * FROM posts""")
#    posts = cursor.fetchall()
#    posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()  # .filter(models.Post.owner_id == current_user.id) this code filters the posts so users can only recieve their own and not others
    posts = db.query(models.Post, func.count(models.Vote.post_id).label('votes')).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter= True).group_by(models.Post.id).filter(
        models.Post.title.contains(search)).limit(limit).offset(skip).all() # this line creates a join in our postgres database, adding a line for join will always default to left inner join unless specified
    
    return posts


# path paramiter that goes and gets a specific post
@router.get("/{id}", response_model = schemas.PostOut)
def get_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
#    cursor.execute("""SELECT * FROM posts WHERE id = %s """, (str(id)))
#    post = cursor.fetchone()
#    post = db.query(models.Post).filter(models.Post.id == id).first()

    post = db.query(models.Post, func.count(models.Vote.post_id).label('votes')).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter= True).group_by(models.Post.id).filter(models.Post.id == id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail= f'post with id: {id} was not found')

#        response.status_code = status.HTTP_404_NOT_FOUND         # this is another way to write status codes however it's not the best method
#         return {'message': f'post with id: {id} was not found'}
    return post


# normally all the data that is being entered by the user will be sent to a database instead if storing the data on this code
# the code below in the path operation is how to change the status when using 201
@router.post("/", status_code=status.HTTP_201_CREATED, response_model = schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
#    cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """, (post.title, post.content, post.published))
#    new_post = cursor.fetchone()
#    conn.commit()
    new_post = models.Post(owner_id= current_user.id, **post.dict())  # adding **post.dict will help the main code read all the feilds that are related to model instead of having to type the scheme out individually
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


# deleting post
# find the index in the array that has the required ID
# my_post.pop(index)
# when deleting data the expectation is that no data will be sent back to the user, in the return statement you will need a 'Response' with the 204 status code so that there will be no errors related
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)): 
#    cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING * """, (str(id)))
#    deleted_post = cursor.fetchone()
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail= f'post with id: {id} does not exist')
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to preform requested action")
    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model = schemas.Post)
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
#    cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""", (post.title, post.content, post.published, (str(id))))
#    updated_post = cursor.fetchone()
#    conn.commit()
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail= f'post with id: {id} does not exist')
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to preform requested action")

    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()
