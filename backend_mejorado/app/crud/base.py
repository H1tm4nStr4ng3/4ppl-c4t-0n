"""
Operaciones CRUD genéricas para reutilizar en todos los modelos
"""
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import inspect

from app.core.database import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    """
    Clase base genérica para operaciones CRUD.
    
    Parámetros:
    - model: Modelo SQLAlchemy
    - create_schema: Schema Pydantic para crear
    - update_schema: Schema Pydantic para actualizar
    """
    
    def __init__(self, model: Type[ModelType]):
        """
        Inicializa el CRUD con el modelo específico.
        
        Args:
            model: Modelo SQLAlchemy
        """
        self.model = model
        self.primary_key = self._get_primary_key()
    
    def _get_primary_key(self) -> str:
        """Obtiene el nombre de la clave primaria del modelo"""
        mapper = inspect(self.model)
        return mapper.primary_key[0].name
    
    def get(self, db: Session, id: Any) -> Optional[ModelType]:
        """
        Obtiene un registro por su ID.
        
        Args:
            db: Sesión de base de datos
            id: ID del registro
            
        Returns:
            Registro encontrado o None
        """
        return db.query(self.model).filter(
            getattr(self.model, self.primary_key) == id
        ).first()
    
    def get_multi(
        self, 
        db: Session, 
        *, 
        skip: int = 0, 
        limit: int = 100,
        filters: Optional[Dict[str, Any]] = None
    ) -> List[ModelType]:
        """
        Obtiene múltiples registros con paginación y filtros opcionales.
        
        Args:
            db: Sesión de base de datos
            skip: Número de registros a saltar
            limit: Número máximo de registros a retornar
            filters: Diccionario de filtros {campo: valor}
            
        Returns:
            Lista de registros
        """
        query = db.query(self.model)
        
        if filters:
            for field, value in filters.items():
                if hasattr(self.model, field) and value is not None:
                    query = query.filter(getattr(self.model, field) == value)
        
        return query.offset(skip).limit(limit).all()
    
    def count(self, db: Session, filters: Optional[Dict[str, Any]] = None) -> int:
        """
        Cuenta el total de registros con filtros opcionales.
        
        Args:
            db: Sesión de base de datos
            filters: Diccionario de filtros {campo: valor}
            
        Returns:
            Número total de registros
        """
        query = db.query(self.model)
        
        if filters:
            for field, value in filters.items():
                if hasattr(self.model, field) and value is not None:
                    query = query.filter(getattr(self.model, field) == value)
        
        return query.count()
    
    def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
        """
        Crea un nuevo registro.
        
        Args:
            db: Sesión de base de datos
            obj_in: Datos del objeto a crear
            
        Returns:
            Registro creado
        """
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def update(
        self,
        db: Session,
        *,
        db_obj: ModelType,
        obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> ModelType:
        """
        Actualiza un registro existente.
        
        Args:
            db: Sesión de base de datos
            db_obj: Objeto de base de datos a actualizar
            obj_in: Datos a actualizar
            
        Returns:
            Registro actualizado
        """
        obj_data = jsonable_encoder(db_obj)
        
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.model_dump(exclude_unset=True)
        
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def delete(self, db: Session, *, id: Any) -> Optional[ModelType]:
        """
        Elimina un registro.
        
        Args:
            db: Sesión de base de datos
            id: ID del registro a eliminar
            
        Returns:
            Registro eliminado o None si no existe
        """
        obj = db.query(self.model).filter(
            getattr(self.model, self.primary_key) == id
        ).first()
        
        if obj:
            db.delete(obj)
            db.commit()
        
        return obj
