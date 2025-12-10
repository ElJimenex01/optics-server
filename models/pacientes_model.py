from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from database.database import Base
from pydantic import BaseModel, EmailStr
from datetime import datetime

class Paciente(Base):

    __tablename__ = "pacientes"

    id = Column(Integer, primary_key=True, index=True)
    nombres = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    edad = Column(Integer, nullable=False)
    ocupacion = Column(String(100), nullable=True)
    problema_ocular = Column(String(255), nullable=True)
    medicamento_actual = Column(String(255), nullable=True)
    lentes = Column(Boolean, default=False, nullable=False)
    antecedentes_familiares_lentes = Column(Boolean, default=False, nullable=True)
    hipertension = Column(Boolean, default=False, nullable=True)
    diabetico = Column(Boolean, default=False, nullable=True)
    util_lentes = Column(Boolean, default=False, nullable=True)
    cefaleas = Column(Boolean, default=False, nullable=True)
    princip_defi_visual = Column(String(255), nullable=True)
    otros = Column(String(255), nullable=True)
    cliente_id = Column(Integer, nullable=True)

class PacienteCreate(BaseModel):
    nombres: str
    apellidos: str
    edad: int
    ocupacion: str | None = None
    problema_ocular: str | None = None
    medicamento_actual: str | None = None
    lentes: bool | None = None
    antecedentes_familiares_lentes: bool | None = None
    hipertension: bool | None = None
    diabetico: bool | None = None
    util_lentes: bool | None = None
    cefaleas: bool | None = None
    princip_defi_visual: str | None = None
    otros: str | None = None
    cliente_id: int | None = None

class PacienteUpdate(BaseModel):
    nombres: str | None = None
    apellidos: str | None = None
    edad: int | None = None
    ocupacion: str | None = None
    problema_ocular: str | None = None
    medicamento_actual: str | None = None
    lentes: bool | None = None
    antecedentes_familiares_lentes: bool | None = None
    hipertension: bool | None = None
    diabetico: bool | None = None
    util_lentes: bool | None = None
    cefaleas: bool | None = None
    princip_defi_visual: str | None = None
    otros: str | None = None
    cliente_id: int | None = None

class PacienteOut(BaseModel):
    id: int
    nombres: str
    apellidos: str
    edad: int
    ocupacion: str | None = None
    problema_ocular: str | None = None
    medicamento_actual: str | None = None
    lentes: bool
    antecedentes_familiares_lentes: bool | None = None
    hipertension: bool | None = None
    diabetico: bool | None = None
    util_lentes: bool | None = None
    cefaleas: bool | None = None
    princip_defi_visual: str | None = None
    otros: str | None = None
    cliente_id: int | None = None

    class Config:
        from_attributes = True