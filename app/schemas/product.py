from pydantic import BaseModel, Field
from decimal import Decimal

class ProductCreate(BaseModel):
    name: str = Field(min_length=3, max_length=100)
    description: str | None = Field(default=None, max_length=100)
    price: Decimal
    is_available: bool = True
    category_id: int

    model_config = {
        "from_attributes": True
    }

class ProductResponse(BaseModel):
    id: int
    name: str
    description: str | None
    price: Decimal
    is_available: bool
    category_id: int

    model_config = {
        "from_attributes": True
    }