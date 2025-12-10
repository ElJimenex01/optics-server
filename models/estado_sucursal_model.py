from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from database.database import Base
from pydantic import BaseModel, EmailStr
from datetime import datetime

class Estado_Sucursal(Base):
    __tablename__ = "estado_sucursal"

    id = Column(Integer, primary_key=True, index=True)
    estado = Column(String(100), nullable=False)

class EstadoSucursalCreate(BaseModel):
    estado: str

class EstadoSucursalUpdate(BaseModel):
    estado: str | None = None

class EstadoSucursalOut(BaseModel):
    id: int
    estado: str

    class Config:
        from_attributes = True