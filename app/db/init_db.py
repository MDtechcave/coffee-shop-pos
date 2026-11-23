from app.db.session import Base, engine

# Import all models so SQLAlchemy knows about them
from app.models import (
    User,
    Category,
    Product,
    Order,
    OrderItem,
    Payment
)

# Create database tables
Base.metadata.create_all(bind=engine)