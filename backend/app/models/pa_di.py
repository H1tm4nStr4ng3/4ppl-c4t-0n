"""
Modelos del módulo PA_DI - Gestión de Documentos
"""
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text
from app.core.database import Base


class PA_DI_FA(Base):
    """Modelo para Fallas/Eventos"""
    __tablename__ = 'pa_di_fa'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    registrado_por = Column(String(255), nullable=True)
    fecha = Column(DateTime, nullable=True)
    evento = Column(Text, nullable=True)
    resuelto = Column(Boolean, default=False, nullable=False)
    trial814 = Column(String(1), nullable=True)
    
    def __repr__(self):
        return f"<PA_DI_FA(id={self.id}, evento={self.evento[:30] if self.evento else None})>"


class PA_DI_PR(Base):
    """Modelo para Procesos"""
    __tablename__ = 'pa_di_pr'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    codigo_del_proceso = Column(String(255), nullable=True)
    proceso = Column(String(255), nullable=True)
    vigente = Column(Boolean, default=False, nullable=False)
    trial814 = Column(String(1), nullable=True)
    
    def __repr__(self):
        return f"<PA_DI_PR(id={self.id}, proceso={self.proceso})>"


class PA_DI_RA(Base):
    """Modelo para Registros de Actualización de Documentos"""
    __tablename__ = 'pa_di_ra'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    fecha_de_apertura = Column(DateTime, nullable=True)
    registrado_por = Column(String(255), nullable=True)
    origen_de_documento = Column(String(255), nullable=True)
    tipo_de_documento = Column(String(255), nullable=True)
    proceso = Column(Integer, nullable=True)
    codigo_de_documento_global = Column(String(255), nullable=True)
    codigo_particular = Column(String(255), nullable=True)
    documento = Column(String(255), nullable=True)
    revisado_por = Column(String(255), nullable=True)
    modificaciones = Column(Text, nullable=True)
    numerales_afectados = Column(Text, nullable=True)
    observaciones = Column(Text, nullable=True)
    aprobado_por = Column(String(255), nullable=True)
    version_nueva = Column(String(50), nullable=True)
    aprobado = Column(Boolean, default=False, nullable=False)
    aplica_comprobacion = Column(Boolean, default=False, nullable=False)
    comentarios_de_comprobacion = Column(Text, nullable=True)
    comprobado = Column(Boolean, default=False, nullable=False)
    ubicacion = Column(String(255), nullable=True)
    fecha_de_cierre = Column(DateTime, nullable=True)
    trial814 = Column(String(1), nullable=True)
    
    def __repr__(self):
        return f"<PA_DI_RA(id={self.id}, documento={self.documento})>"
