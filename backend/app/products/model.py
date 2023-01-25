from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    price: float
    category_id: int
    serie: int 

class ProductUpdate(BaseModel):
    name: str
    price: float
    category_id: int