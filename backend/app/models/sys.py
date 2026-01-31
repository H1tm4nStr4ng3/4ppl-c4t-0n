"""
Modelos del módulo SYS - Tablas del Sistema
"""
from sqlalchemy import Column, Integer, String, Float
from app.core.database import Base


class SYS_FACTORESK(Base):
    """Modelo para Factores K"""
    __tablename__ = 'sys_factoresk'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    descripcion = Column(String(255), nullable=True)
    factor = Column(Float, nullable=True)
    trial830 = Column(String(1), nullable=True)
    
    def __repr__(self):
        return f"<SYS_FACTORESK(id={self.id}, descripcion={self.descripcion})>"


class TBL_LUGARES(Base):
    """Modelo para Lugares"""
    __tablename__ = 'tbl_lugares'
    __table_args__ = {'schema': 'SGApp'}
    
    lugarid = Column(Integer, primary_key=True, index=True, nullable=False)
    ciudad = Column(String(255), nullable=True)
    departamento = Column(String(255), nullable=True)
    altitud = Column(Integer, nullable=True)
    presionref_hpa = Column(Integer, nullable=True)
    humedadref_pct = Column(Integer, nullable=True)
    prioridad = Column(Integer, nullable=True)
    trial830 = Column(String(1), nullable=True)
    
    def __repr__(self):
        return f"<TBL_LUGARES(lugarid={self.lugarid}, ciudad={self.ciudad})>"


class TBL_POSICIONES_HORNO(Base):
    """Modelo para Posiciones de Horno"""
    __tablename__ = 'tbl_posiciones_horno'
    __table_args__ = {'schema': 'SGApp'}
    
    posicionid = Column(Integer, primary_key=True, index=True, nullable=False)
    clasedeequipo = Column(String(255), nullable=True)
    nombreposicion = Column(String(255), nullable=True)
    trial830 = Column(String(1), nullable=True)
    
    def __repr__(self):
        return f"<TBL_POSICIONES_HORNO(posicionid={self.posicionid}, nombreposicion={self.nombreposicion})>"
