from sqlalchemy import Column, Integer, String, Text
from config.database import  Base 

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    
class Posts(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(Text, nullable=False)
    user_id = Column(Integer, nullable=False)