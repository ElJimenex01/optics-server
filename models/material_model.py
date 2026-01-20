from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from database.database import Base
from pydantic import BaseModel

class Material(Base):
    __tablename__ = "materiales"

    id = Column(Integer, primary_key=True, index=True)
    material = Column(String(100), nullable=False)

class MaterialCreate(BaseModel):
    material: str

class MaterialUpdate(BaseModel):
    material: str | None = None

class MaterialOut(BaseModel):
    id: int
    material: str

    class Config:
        from_attributes = True