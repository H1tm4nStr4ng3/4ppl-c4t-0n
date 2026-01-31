"""
Factory genérico para crear routers CRUD
Este archivo reduce dramáticamente el código repetitivo
"""
from typing import Any, Callable, Dict, List, Optional, Type, TypeVar
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.core.database import get_db, Base
from app.crud.base import CRUDBase
from app.schemas.base import PaginatedResponse, MessageResponse
from app.core.config import settings

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)
SchemaType = TypeVar("SchemaType", bound=BaseModel)


def create_crud_router(
    model: Type[ModelType],
    schema: Type[SchemaType],
    create_schema: Type[CreateSchemaType],
    update_schema: Type[UpdateSchemaType],
    prefix: str,
    tags: List[str],
    crud_class: Optional[Type[CRUDBase]] = None,
) -> APIRouter:
    """
    Crea un router CRUD completo para un modelo.
    
    Args:
        model: Modelo SQLAlchemy
        schema: Schema Pydantic de respuesta
        create_schema: Schema Pydantic para crear
        update_schema: Schema Pydantic para actualizar
        prefix: Prefijo de la URL (ej: "/pa-di-fa")
        tags: Tags para documentación
        crud_class: Clase CRUD personalizada (opcional)
        
    Returns:
        Router configurado con endpoints CRUD
    """
    router = APIRouter(prefix=prefix, tags=tags)
    
    # Inicializar CRUD
    if crud_class is None:
        crud = CRUDBase[ModelType, CreateSchemaType, UpdateSchemaType](model)
    else:
        crud = crud_class(model)
    
    @router.get(
        "/",
        response_model=PaginatedResponse[schema],
        summary=f"Listar {tags[0]}",
        description=f"Obtiene una lista paginada de {tags[0]}"
    )
    def list_items(
        skip: int = Query(0, ge=0, description="Registros a saltar"),
        limit: int = Query(
            settings.DEFAULT_PAGE_SIZE,
            ge=1,
            le=settings.MAX_PAGE_SIZE,
            description="Límite de registros"
        ),
        db: Session = Depends(get_db)
    ) -> Any:
        """Lista todos los registros con paginación"""
        try:
            items = crud.get_multi(db, skip=skip, limit=limit)
            total = crud.count(db)
            return PaginatedResponse.create(
                items=items,
                total=total,
                skip=skip,
                limit=limit
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error al listar registros: {str(e)}"
            )
    
    @router.get(
        "/{id}",
        response_model=schema,
        summary=f"Obtener {tags[0]} por ID",
        description=f"Obtiene un registro específico de {tags[0]} por su ID"
    )
    def get_item(
        id: Any,
        db: Session = Depends(get_db)
    ) -> Any:
        """Obtiene un registro por ID"""
        try:
            item = crud.get(db, id=id)
            if not item:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Registro con ID {id} no encontrado"
                )
            return item
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error al obtener registro: {str(e)}"
            )
    
    @router.post(
        "/",
        response_model=schema,
        status_code=status.HTTP_201_CREATED,
        summary=f"Crear {tags[0]}",
        description=f"Crea un nuevo registro de {tags[0]}"
    )
    def create_item(
        item_in: create_schema,
        db: Session = Depends(get_db)
    ) -> Any:
        """Crea un nuevo registro"""
        try:
            item = crud.create(db, obj_in=item_in)
            return item
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error al crear registro: {str(e)}"
            )
    
    @router.put(
        "/{id}",
        response_model=schema,
        summary=f"Actualizar {tags[0]}",
        description=f"Actualiza un registro existente de {tags[0]}"
    )
    def update_item(
        id: Any,
        item_in: update_schema,
        db: Session = Depends(get_db)
    ) -> Any:
        """Actualiza un registro existente"""
        try:
            item = crud.get(db, id=id)
            if not item:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Registro con ID {id} no encontrado"
                )
            item = crud.update(db, db_obj=item, obj_in=item_in)
            return item
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error al actualizar registro: {str(e)}"
            )
    
    @router.delete(
        "/{id}",
        response_model=MessageResponse,
        summary=f"Eliminar {tags[0]}",
        description=f"Elimina un registro de {tags[0]}"
    )
    def delete_item(
        id: Any,
        db: Session = Depends(get_db)
    ) -> Any:
        """Elimina un registro"""
        try:
            item = crud.delete(db, id=id)
            if not item:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Registro con ID {id} no encontrado"
                )
            return MessageResponse(
                message="Registro eliminado exitosamente",
                detail=f"Registro con ID {id} fue eliminado"
            )
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error al eliminar registro: {str(e)}"
            )
    
    return router
