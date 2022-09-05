from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200))
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    phone_number =Column(String(20))
    address = Column(String(50))
    is_active = Column(Boolean, default=True)

    insurance_table = relationship("Insurance", back_populates = "user_table")


class Insurance(Base):
    __tablename__ = "insurance"

    id = Column(Integer, primary_key=True, index=True)
    user = Column(Integer,  ForeignKey("users.id", ondelete="CASCADE"))

    user_table = relationship("Users", back_populates = "insurance_table")

class QRPAgent(Base):
    __tablename__ = "agents"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200))
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    state = Column(String)
    address = Column(String(50))
    phone_number =Column(String(20))
    is_active = Column(Boolean, default=True)
