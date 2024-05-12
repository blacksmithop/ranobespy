from pydantic import BaseModel
from typing import Optional

class Novel(BaseModel):
    name: str
    novel_url: str
    chapter: Optional[int] = None
    image_url: str

class Author(BaseModel):
    name: str
    profile_url: str
    image_url: str
    
class Comment(BaseModel):
    author: Author
    upvote: int
    downvote: int
    novel: Novel
    comment: str
