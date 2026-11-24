from sqlalchemy import Column, Integer, String, Boolean
from app.db.session import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    orders = relationship("Order", back_populates="user")
    refund_requests = relationship("Refund", foreign_keys="Refund.requested_by", back_populates="requester")
    refund_approvals = relationship("Refund", foreign_keys="Refund.approved_by", back_populates="approver")
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(20), default="cashier")
    is_active = Column(Boolean, default=True)