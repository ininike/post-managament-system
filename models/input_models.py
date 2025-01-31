from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    password: str
    
class PostBase(BaseModel):
    title: str
    content: str
    
class PostEdit(BaseModel):
    section: str
    newcontent: str