"""
Schemas base y utilidades para toda la aplicación
"""
from pydantic import BaseModel, ConfigDict, Field
from typing import Generic, TypeVar, List, Optional
from datetime import datetime


# TypeVars para genéricos
T = TypeVar('T')


class PaginationParams(BaseModel):
    """Parámetros de paginación"""
    skip: int = Field(default=0, ge=0, description="Número de registros a saltar")
    limit: int = Field(default=50, ge=1, le=1000, description="Límite de registros por página")


class PaginatedResponse(BaseModel, Generic[T]):
    """Respuesta paginada genérica"""
    items: List[T] = Field(description="Lista de items")
    total: int = Field(description="Total de registros")
    skip: int = Field(description="Registros saltados")
    limit: int = Field(description="Límite de registros")
    has_next: bool = Field(description="Indica si hay más páginas")
    has_prev: bool = Field(description="Indica si hay páginas previas")
    
    @classmethod
    def create(cls, items: List[T], total: int, skip: int, limit: int):
        """Crea una respuesta paginada"""
        return cls(
            items=items,
            total=total,
            skip=skip,
            limit=limit,
            has_next=skip + limit < total,
            has_prev=skip > 0
        )


class MessageResponse(BaseModel):
    """Respuesta genérica de mensaje"""
    message: str = Field(description="Mensaje de la operación")
    detail: Optional[str] = Field(default=None, description="Detalles adicionales")


class ErrorResponse(BaseModel):
    """Respuesta de error"""
    error: str = Field(description="Tipo de error")
    message: str = Field(description="Mensaje de error")
    detail: Optional[str] = Field(default=None, description="Detalles adicionales")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="Timestamp del error")
