from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from database.database import Base
from pydantic import BaseModel

class Servicio(Base):
    __tablename__ = "servicios"

    id = Column(Integer, primary_key=True, index=True)
    servicio = Column(String(100), nullable=False)

class ServicioCreate(BaseModel):
    servicio: str

class ServicioUpdate(BaseModel):
    servicio: str | None = None

class ServicioOut(BaseModel):
    id: int
    servicio: str
    
    class Config:
        from_attributes = True