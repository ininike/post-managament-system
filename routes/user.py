from fastapi import APIRouter, HTTPException, status, Request, Response
import models.db_schema as models
from dependencies.auth import db_dependency
from models.input_models import UserBase
from passlib.context import CryptContext

router = APIRouter(
    prefix="/user",
    tags=["User"]
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/register", status_code=status.HTTP_200_OK)
async def create_user(user: UserBase, db: db_dependency):
    user.password = pwd_context.hash(user.password)
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    return {"message": "User created successfully!"}
    
@router.post("/login", status_code=status.HTTP_200_OK)
async def login(input: UserBase, db: db_dependency, response: Response):
    user = db.query(models.User).filter(models.User.username == input.username).first()
    if user is None:
        raise HTTPException(status_code=401,detail='Incorrect username/password')
    valid = pwd_context.verify(input.password, user.password)
    if not valid:
        raise HTTPException(status_code=401,detail='Incorrect username/password')
    response.set_cookie(key='session_id', value= user.id)
    return {'message': 'Login Successful'}

@router.get("/logout", status_code=status.HTTP_200_OK)
async def logout(request: Request, response: Response):
    user_id = request.cookies.get('session_id')
    if user_id is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail='You are not logged in')
    response.delete_cookie(key='session_id')
    return {'message': 'Logout successful'}





    


