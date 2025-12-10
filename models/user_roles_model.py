from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from database.database import Base
from pydantic import BaseModel, EmailStr

class UserRole (Base):

    __tablename__ = "user_roles"

    id = Column(Integer, primary_key=True, index=True)
    rol = Column(String(100), unique=True, index=True, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)

class UserRoleCreate (BaseModel):
    rol: str
    is_active: bool | None = True

class UserRoleUpdate (BaseModel):
    rol: str | None = None
    is_active: bool | None = None

class UserRoleOut (BaseModel):
    id: int
    rol: str
    is_active: bool

    class Config:
        from_attributes = True