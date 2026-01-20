from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from database.database import Base
from pydantic import BaseModel

class Armazon(Base):
    __tablename__ = "armazones"

    id = Column(Integer, primary_key=True, index=True)
    marca = Column(String(100), nullable=False)

class ArmazonCreate(BaseModel):
    marca: str

class ArmazonUpdate(BaseModel):
    marca: str | None = None

class ArmazonOut(BaseModel):
    id: int
    marca: str

    class Config:
        from_attributes = True