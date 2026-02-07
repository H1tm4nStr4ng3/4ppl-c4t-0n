"""
Modelos del módulo PA_EQ - Gestión de Equipamiento
"""
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base


class PA_EQ_AC(Base):
    """Modelo para Actividades de Equipamiento"""
    __tablename__ = 'pa_eq_ac'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, nullable=False, index=True)
    actividad = Column(String(255), primary_key=True, nullable=False)
    descripcion = Column(Text, nullable=True)
    trial814 = Column(String(1), nullable=True)
    
    def __repr__(self):
        return f"<PA_EQ_AC(actividad={self.actividad})>"


class PA_EQ_CA(Base):
    """Modelo para Calibraciones"""
    __tablename__ = 'pa_eq_ca'
    __table_args__ = {'schema': 'SGApp'}
    
    id_equi = Column(Integer, nullable=False)
    registrado_por = Column(String(255), nullable=True)
    fecha = Column(DateTime, nullable=True)
    equipamiento = Column(String(255), nullable=True)
    certificado = Column(String(255), primary_key=True, nullable=False)
    ente_calibrador = Column(String(255), nullable=True)
    fecha_de_calibracion = Column(DateTime, nullable=True)
    unidades = Column(String(50), nullable=True)
    observaciones = Column(Text, nullable=True)
    apto = Column(Boolean, default=False, nullable=False)
    regla = Column(String(255), nullable=True)
    trial814 = Column(String(1), nullable=True)
    
    # Relaciones
    pa_eq_dc_items = relationship('PA_EQ_DC', back_populates='pa_eq_ca_rel', cascade='all, delete-orphan')
    pa_eq_ex_items = relationship('PA_EQ_EX', back_populates='pa_eq_ca_rel', cascade='all, delete-orphan')
    pa_eq_hm_items = relationship('PA_EQ_HM', back_populates='pa_eq_ca_rel', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f"<PA_EQ_CA(certificado={self.certificado})>"


class PA_EQ_CB(Base):
    """Modelo para Comprobación de Balanzas"""
    __tablename__ = 'pa_eq_cb'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    id_ci = Column(Integer, nullable=True)
    tipoprueba = Column(String(100), nullable=True)
    pesapatron_id = Column(String(100), nullable=True)
    posicion = Column(String(100), nullable=True)
    lectura_balanza = Column(Float, nullable=True)
    lectura_corregida = Column(Float, nullable=True)
    trial814 = Column(String(1), nullable=True)
    
    def __repr__(self):
        return f"<PA_EQ_CB(id={self.id})>"


class PA_EQ_CH(Base):
    """Modelo para Comprobación de Hornos"""
    __tablename__ = 'pa_eq_ch'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    id_ci = Column(Integer, nullable=True)
    posicion = Column(String(100), nullable=True)
    temppatron_leida = Column(Float, nullable=True)
    tempequipo_leida = Column(Float, nullable=True)
    diferencia = Column(Float, nullable=True)
    resultadopunto = Column(String(100), nullable=True)
    trial814 = Column(String(1), nullable=True)
    
    def __repr__(self):
        return f"<PA_EQ_CH(id={self.id})>"


class PA_EQ_CI(Base):
    """Modelo para Comprobaciones Intermedias"""
    __tablename__ = 'pa_eq_ci'
    __table_args__ = {'schema': 'SGApp'}
    
    # NOTA: Esta tabla no tiene primary key definida en el SQL original
    # Agregamos id_equi como primary key para evitar problemas
    id_equi = Column(Integer, primary_key=True, nullable=False)
    registrado_por = Column(String(255), nullable=True)
    fecha = Column(DateTime, nullable=True)
    equipamiento = Column(String(255), nullable=True)
    balanza_utilizada = Column(String(255), nullable=True)
    unidades = Column(String(50), nullable=True)
    observaciones = Column(Text, nullable=True)
    promedio = Column(Float, nullable=True)
    desv_est = Column(Float, nullable=True)
    tol_sistematico = Column(Float, nullable=True)
    conclusion_sistematico = Column(String(255), nullable=True)
    temperatura = Column(Float, nullable=True)
    lugar = Column(String(255), nullable=True)
    presion_hpa = Column(Float, nullable=True)
    humedad_relativa = Column(Float, nullable=True)
    en = Column(Float, nullable=True)
    conclusion_en = Column(String(255), nullable=True)
    volumen_nominal = Column(Float, nullable=True)
    valor = Column(Float, nullable=True)
    incertidumbre = Column(Float, nullable=True)
    tipo_comprobacion = Column(String(100), nullable=True)
    tempprogramada = Column(Float, nullable=True)
    termometro_id = Column(String(100), nullable=True)
    cg = Column(Float, nullable=True)
    cgk = Column(Float, nullable=True)
    trial814 = Column(String(1), nullable=True)
    
    def __repr__(self):
        return f"<PA_EQ_CI(id_equi={self.id_equi})>"


class PA_EQ_CV(Base):
    """Modelo para Comprobación de Volumen"""
    __tablename__ = 'pa_eq_cv'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    id_ci = Column(Integer, nullable=True)
    matraz_vacio = Column(Float, nullable=True)
    corr1 = Column(Float, nullable=True)
    matraz_lleno = Column(Float, nullable=True)
    corr2 = Column(Float, nullable=True)
    masa_h2o = Column(Float, nullable=True)
    densidad = Column(Float, nullable=True)
    volumen = Column(Float, nullable=True)
    trial814 = Column(String(1), nullable=True)
    
    def __repr__(self):
        return f"<PA_EQ_CV(id={self.id})>"


class PA_EQ_DC(Base):
    """Modelo para Datos de Calibración"""
    __tablename__ = 'pa_eq_dc'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    id_ca = Column(String(255), ForeignKey('SGApp.pa_eq_ca.certificado', ondelete='CASCADE'))
    valor_nominal = Column(Float, nullable=True)
    referencia = Column(String(255), nullable=True)
    correccion_reportada = Column(Float, nullable=True)
    incertidumbre = Column(Float, nullable=True)
    tolerancia_de_medicion = Column(Float, nullable=True)
    conformidad = Column(String(100), nullable=True)
    trial814 = Column(String(1), nullable=True)
    
    # Relación
    pa_eq_ca_rel = relationship('PA_EQ_CA', back_populates='pa_eq_dc_items')
    
    def __repr__(self):
        return f"<PA_EQ_DC(id={self.id})>"


class PA_EQ_EQ(Base):
    """Modelo para Equipamiento"""
    __tablename__ = 'pa_eq_eq'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    equipamiento = Column(String(255), nullable=True)
    codigo_interno = Column(String(100), nullable=False, unique=True)
    marca = Column(String(100), nullable=True)
    serie = Column(String(100), nullable=True)
    material = Column(String(100), nullable=True)
    numero = Column(String(100), nullable=True)
    max_vn = Column(String(100), nullable=True)
    d = Column(String(100), nullable=True)
    clase_de_exactitud = Column(String(100), nullable=True)
    ubicacion = Column(String(255), nullable=True)
    comentarios = Column(Text, nullable=True)
    puesta_en_funcionamiento = Column(DateTime, nullable=True)
    estado = Column(String(100), nullable=True)
    requiere = Column(String(255), nullable=True)
    frecuencia_de_calibracion = Column(String(100), nullable=True)
    frecuencia_de_mantenimiento = Column(String(100), nullable=True)
    frecuencia_de_comprobacion_intermedia = Column(String(100), nullable=True)
    frecuencia_de_calificacion = Column(String(100), nullable=True)
    trial814 = Column(String(1), nullable=True)
    
    def __repr__(self):
        return f"<PA_EQ_EQ(id={self.id}, codigo_interno={self.codigo_interno})>"


class PA_EQ_EX(Base):
    """Modelo para Excentricidad"""
    __tablename__ = 'pa_eq_ex'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    id_ca = Column(String(255), ForeignKey('SGApp.pa_eq_ca.certificado', ondelete='CASCADE'))
    carga = Column(Float, nullable=True)
    posicion = Column(Float, nullable=True)
    diferencia_reportada = Column(Float, nullable=True)
    tolerancia = Column(Float, nullable=True)
    conformidad = Column(String(100), nullable=True)
    trial814 = Column(String(1), nullable=True)
    
    # Relación
    pa_eq_ca_rel = relationship('PA_EQ_CA', back_populates='pa_eq_ex_items')
    
    def __repr__(self):
        return f"<PA_EQ_EX(id={self.id})>"


class PA_EQ_HM(Base):
    """Modelo para Homogeneidad de Temperatura"""
    __tablename__ = 'pa_eq_hm'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    id_ca = Column(String(255), ForeignKey('SGApp.pa_eq_ca.certificado', ondelete='CASCADE'))
    temperatura_nominal = Column(Float, nullable=True)
    en_el_tiempo = Column(Float, nullable=True)
    incertidumbre_expandida = Column(Float, nullable=True)
    tolerancia_en_el_tiempo = Column(Float, nullable=True)
    conformidad_tiempo = Column(String(100), nullable=True)
    en_el_espacio = Column(Float, nullable=True)
    tolerancia_en_el_espacio = Column(Float, nullable=True)
    conformidad_espacio = Column(String(100), nullable=True)
    trial814 = Column(String(1), nullable=True)
    
    # Relación
    pa_eq_ca_rel = relationship('PA_EQ_CA', back_populates='pa_eq_hm_items')
    
    def __repr__(self):
        return f"<PA_EQ_HM(id={self.id})>"
