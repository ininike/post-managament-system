from fastapi import APIRouter, HTTPException, status, Request
import models.db_schema as models
from dependencies.auth import db_dependency, current_user_dependency
from models.input_models import PostBase, PostEdit

router = APIRouter(
    prefix="/post",
    tags=["Post"]
)

@router.post("/make_post", status_code=status.HTTP_200_OK)
async def make_post(db: db_dependency, post: PostBase, current_user: current_user_dependency):
    db_post = models.Posts(**post.model_dump())
    db_post.user_id = current_user.id
    db.add(db_post)
    db.commit()
    return {"message": "Post created successfully"}

@router.put("/edit_post/{post_id}", status_code=status.HTTP_200_OK)
async def edit_post(post_id: int, db: db_dependency, post: PostBase, current_user: current_user_dependency):
    db_post = db.query(models.Posts).filter(models.Posts.id == post_id, models.Posts.user_id == current_user.id).first()
    if db_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Post not found')
    db_post.title = post.title
    db_post.content = post.content
    db.commit()
    return {"message": "Post updated successfully"}

@router.delete("/delete_post/{post_id}", status_code=status.HTTP_200_OK)
async def delete_post(post_id: int, request: Request, db: db_dependency, current_user: current_user_dependency):
    db_post = db.query(models.Posts).filter(models.Posts.id == post_id, models.Posts.user_id == current_user.id).first()
    if db_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Post not found')
    db.delete(db_post)
    db.commit()
    return {"message": "Post deleted successfully"}

@router.get("/my_posts", status_code=status.HTTP_200_OK)
async def my_posts(db: db_dependency, current_user: current_user_dependency):
    user_posts = db.query(models.Posts).filter(models.Posts.user_id == current_user.id).all()
    return user_posts

@router.get("/my_posts/{id}", status_code=status.HTTP_200_OK)
async def my_posts(id: int, db: db_dependency, current_user: current_user_dependency):
    user_posts = db.query(models.Posts).filter(models.Posts.user_id == current_user.id, models.Posts.id == id).first()
    return user_posts

@router.get("/all_posts", status_code=status.HTTP_200_OK)
async def all_posts(db: db_dependency):
    all_posts = db.query(models.Posts).all()
    return all_posts

@router.get("/all_posts/{user_id}", status_code=status.HTTP_200_OK)
async def all_posts(db: db_dependency, user_id: int):
    all_posts = db.query(models.Posts).filter(models.Posts.user_id == user_id).all()
    return all_posts

@router.patch("/edit_post/{post_id}", status_code=status.HTTP_200_OK)
async def edit_post(post_id: int, db: db_dependency, current_user: current_user_dependency, post: PostEdit):
    db_post = db.query(models.Posts).filter(models.Posts.id == post_id, models.Posts.user_id == current_user.id).first()
    if db_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Post not found')
    if post.section == 'content':
        db_post.content = post.newcontent
    if post.section == 'title':
        db_post.title = post.newcontent
    db.commit()
    return {"message": "Post updated successfully"}