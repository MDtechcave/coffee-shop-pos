from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from app.db.session import Base
from sqlalchemy.orm import relationship

class OrderItem(Base):
    __tablename__ = "order_items"
    order = relationship("Order", back_populates="order_items")
    product = relationship("Product", back_populates="order_items")

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    unit_price = Column(Numeric(10, 2), nullable=False)
