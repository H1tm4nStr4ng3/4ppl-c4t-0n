"""
Schemas Pydantic para el módulo PA_DI - Gestión de Documentos
"""
from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from datetime import datetime


# ============== PA_DI_FA (Fallas/Eventos) ==============

class PA_DI_FABase(BaseModel):
    """Schema base para Fallas/Eventos"""
    registrado_por: Optional[str] = Field(None, max_length=255, description="Usuario que registró el evento")
    fecha: Optional[datetime] = Field(None, description="Fecha del evento")
    evento: Optional[str] = Field(None, description="Descripción del evento")
    resuelto: bool = Field(False, description="Indica si el evento fue resuelto")
    trial814: Optional[str] = Field(None, max_length=1)


class PA_DI_FACreate(PA_DI_FABase):
    """Schema para crear Falla/Evento"""
    pass


class PA_DI_FAUpdate(PA_DI_FABase):
    """Schema para actualizar Falla/Evento"""
    registrado_por: Optional[str] = None
    resuelto: Optional[bool] = None


class PA_DI_FA(PA_DI_FABase):
    """Schema completo de Falla/Evento"""
    id: int = Field(..., description="ID único del registro")
    
    model_config = ConfigDict(from_attributes=True)


# ============== PA_DI_PR (Procesos) ==============

class PA_DI_PRBase(BaseModel):
    """Schema base para Procesos"""
    codigo_del_proceso: Optional[str] = Field(None, max_length=255, description="Código del proceso")
    proceso: Optional[str] = Field(None, max_length=255, description="Nombre del proceso")
    vigente: bool = Field(False, description="Indica si el proceso está vigente")
    trial814: Optional[str] = Field(None, max_length=1)


class PA_DI_PRCreate(PA_DI_PRBase):
    """Schema para crear Proceso"""
    pass


class PA_DI_PRUpdate(PA_DI_PRBase):
    """Schema para actualizar Proceso"""
    codigo_del_proceso: Optional[str] = None
    proceso: Optional[str] = None
    vigente: Optional[bool] = None


class PA_DI_PR(PA_DI_PRBase):
    """Schema completo de Proceso"""
    id: int = Field(..., description="ID único del registro")
    
    model_config = ConfigDict(from_attributes=True)


# ============== PA_DI_RA (Registro de Actualización de Documentos) ==============

class PA_DI_RABase(BaseModel):
    """Schema base para Registro de Actualización"""
    fecha_de_apertura: Optional[datetime] = Field(None, description="Fecha de apertura del registro")
    registrado_por: Optional[str] = Field(None, max_length=255, description="Usuario que registró")
    origen_de_documento: Optional[str] = Field(None, max_length=255, description="Origen del documento")
    tipo_de_documento: Optional[str] = Field(None, max_length=255, description="Tipo de documento")
    proceso: Optional[int] = Field(None, description="ID del proceso relacionado")
    codigo_de_documento_global: Optional[str] = Field(None, max_length=255, description="Código global")
    codigo_particular: Optional[str] = Field(None, max_length=255, description="Código particular")
    documento: Optional[str] = Field(None, max_length=255, description="Nombre del documento")
    revisado_por: Optional[str] = Field(None, max_length=255, description="Usuario que revisó")
    modificaciones: Optional[str] = Field(None, description="Descripción de modificaciones")
    numerales_afectados: Optional[str] = Field(None, description="Numerales afectados")
    observaciones: Optional[str] = Field(None, description="Observaciones")
    aprobado_por: Optional[str] = Field(None, max_length=255, description="Usuario que aprobó")
    version_nueva: Optional[str] = Field(None, max_length=50, description="Nueva versión")
    aprobado: bool = Field(False, description="Indica si fue aprobado")
    aplica_comprobacion: bool = Field(False, description="Indica si aplica comprobación")
    comentarios_de_comprobacion: Optional[str] = Field(None, description="Comentarios de comprobación")
    comprobado: bool = Field(False, description="Indica si fue comprobado")
    ubicacion: Optional[str] = Field(None, max_length=255, description="Ubicación del documento")
    fecha_de_cierre: Optional[datetime] = Field(None, description="Fecha de cierre")
    trial814: Optional[str] = Field(None, max_length=1)


class PA_DI_RACreate(PA_DI_RABase):
    """Schema para crear Registro de Actualización"""
    pass


class PA_DI_RAUpdate(PA_DI_RABase):
    """Schema para actualizar Registro de Actualización"""
    fecha_de_apertura: Optional[datetime] = None
    aprobado: Optional[bool] = None
    aplica_comprobacion: Optional[bool] = None
    comprobado: Optional[bool] = None


class PA_DI_RA(PA_DI_RABase):
    """Schema completo de Registro de Actualización"""
    id: int = Field(..., description="ID único del registro")
    
    model_config = ConfigDict(from_attributes=True)
