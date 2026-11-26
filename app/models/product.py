from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Numeric
from app.db.session import Base
from sqlalchemy.orm import relationship

class Product(Base):
    __tablename__ = "products"
    order_items = relationship("OrderItem", back_populates="product")
    category = relationship("Category", back_populates="products")

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)
    price = Column(Numeric(10, 2), nullable=False)
    is_available = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)