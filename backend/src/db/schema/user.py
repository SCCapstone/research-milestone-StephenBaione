from typing import List, Optional
from pydantic import BaseModel, Field

class User(BaseModel):
    id: Optional[int] = Field(...)
    username: str = Field(...)
    email: str = Field(...)

    class Config:
        orm_mode = True
