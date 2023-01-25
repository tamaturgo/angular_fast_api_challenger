from pydantic import BaseModel

class CategoryBase(BaseModel):
    name: str

class CategoryUpdate(BaseModel):
    name: str