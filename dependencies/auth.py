from fastapi import HTTPException, status, Depends, Request
from sqlalchemy.orm import Session
import models.db_schema as models
from config.database import SessionLocal
from typing import Annotated

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(request: Request, db: Session = Depends(get_db)):
    user_id = request.cookies.get('session_id')
    if user_id is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='You are not logged in')
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid session')
    return user

current_user_dependency = Annotated[models.User, Depends(get_current_user)]
db_dependency = Annotated[Session, Depends(get_db)]