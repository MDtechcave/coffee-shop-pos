from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, DateTime
from app.db.session import Base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class Refund(Base):
    __tablename__ = "refunds"

    id = Column(Integer, primary_key=True, index=True)
    payment_id = Column(Integer, ForeignKey("payments.id"), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    refund_method = Column(String(20), nullable=True)
    reason = Column(String(255), nullable=False)
    requested_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    approved_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    refund_status = Column(String(20), default="pending", nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    payment = relationship("Payment", back_populates="refunds")
    requester = relationship("User", foreign_keys=[requested_by], back_populates="refund_requests")
    approver = relationship("User", foreign_keys=[approved_by], back_populates="refund_approvals")


