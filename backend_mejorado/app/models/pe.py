"""
Modelos del módulo PE - Procesos Estratégicos
"""
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text
from app.core.database import Base


class PE_SE_AC(Base):
    """Modelo para Acciones Correctivas"""
    __tablename__ = 'pe_se_ac'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    fecha_registro = Column(DateTime, nullable=True)
    registrado_por = Column(String(255), nullable=True)
    descripcion_de_la_no_conformidad = Column(Text, nullable=True)
    evidencia = Column(Text, nullable=True)
    requisito_o_criterio_implicado = Column(Text, nullable=True)
    analisis_de_la_no_conformidad = Column(Text, nullable=True)
    por_que_1 = Column('1_por_qué', Text, nullable=True)  # Nombre de columna con número
    por_que_2 = Column('2_por_qué', Text, nullable=True)
    por_que_3 = Column('3_por_qué', Text, nullable=True)
    por_que_4 = Column('4_por_qué', Text, nullable=True)
    por_que_5 = Column('5_por_qué', Text, nullable=True)
    no_conformidad_similar_o_potencial = Column(Text, nullable=True)
    causa = Column(Text, nullable=True)
    responsable_de_seguimiento = Column(String(255), nullable=True)
    fecha_de_seguimiento_de_eficacia_de_acciones = Column(DateTime, nullable=True)
    efecto_deseado = Column(Text, nullable=True)
    seguimiento = Column(Text, nullable=True)
    eficaz = Column(Boolean, default=False, nullable=False)
    fecha_seguimiento = Column(DateTime, nullable=True)
    observaciones = Column(Text, nullable=True)
    cerrado = Column(Boolean, default=False, nullable=False)
    trial827 = Column(String(1), nullable=True)
    
    def __repr__(self):
        return f"<PE_SE_AC(id={self.id})>"


class PE_SE_CA(Base):
    """Modelo para Correcciones de Acciones"""
    __tablename__ = 'pe_se_ca'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    acciones_correctivas = Column(Integer, nullable=True)
    acciones_abordar = Column(Text, nullable=True)
    responsable_actividades = Column(String(255), nullable=True)
    recursos = Column(Text, nullable=True)
    fecha_frecuencia_actividad = Column(DateTime, nullable=True)
    resultado_esperado = Column(Text, nullable=True)
    fecha_seguimiento = Column(DateTime, nullable=True)
    responsable_seguimiento = Column(String(255), nullable=True)
    conclusion_seguimiento = Column(Text, nullable=True)
    realizado = Column(Boolean, default=False, nullable=False)
    trial827 = Column(String(1), nullable=True)
    
    def __repr__(self):
        return f"<PE_SE_CA(id={self.id})>"


class PE_SE_CO(Base):
    """Modelo para Correcciones"""
    __tablename__ = 'pe_se_co'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    correcciones = Column(Integer, nullable=True)
    acciones_abordar = Column(Text, nullable=True)
    responsable_actividades = Column(String(255), nullable=True)
    recursos = Column(Text, nullable=True)
    fecha_frecuencia_actividad = Column(DateTime, nullable=True)
    resultado_esperado = Column(Text, nullable=True)
    fecha_seguimiento = Column(DateTime, nullable=True)
    responsable_seguimiento = Column(String(255), nullable=True)
    conclusion_seguimiento = Column(Text, nullable=True)
    realizado = Column(Boolean, default=False, nullable=False)
    trial827 = Column(String(1), nullable=True)
    
    def __repr__(self):
        return f"<PE_SE_CO(id={self.id})>"


class PE_SE_EE(Base):
    """Modelo para Entradas de Evaluación"""
    __tablename__ = 'pe_se_ee'
    __table_args__ = {'schema': 'SGApp'}
    
    # NOTA: Esta tabla no tiene primary key en el SQL original
    # Agregamos entradas como primary key
    entradas = Column(String(255), primary_key=True, nullable=False)
    trial827 = Column(String(1), nullable=True)
    
    def __repr__(self):
        return f"<PE_SE_EE(entradas={self.entradas})>"


class PE_SE_EN(Base):
    """Modelo para Entradas"""
    __tablename__ = 'pe_se_en'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    id_re = Column(Integer, nullable=True)
    entrada = Column(String(255), nullable=True)
    fuente = Column(String(255), nullable=True)
    link = Column(Text, nullable=True)
    conveniencia = Column(Text, nullable=True)
    conveniente = Column(Boolean, default=False, nullable=False)
    adecuacion = Column(Text, nullable=True)
    adecuado = Column(Boolean, default=False, nullable=False)
    eficacia = Column(Text, nullable=True)
    eficaz = Column(Boolean, default=False, nullable=False)
    trial827 = Column(String(1), nullable=True)
    
    def __repr__(self):
        return f"<PE_SE_EN(id={self.id})>"


class PE_SE_MA(Base):
    """Modelo para Mejoras de Acciones"""
    __tablename__ = 'pe_se_ma'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    acciones_de_mejora = Column(Integer, nullable=True)
    acciones_abordar = Column(Text, nullable=True)
    responsable_actividades = Column(String(255), nullable=True)
    recursos = Column(Text, nullable=True)
    fecha_frecuencia_actividad = Column(DateTime, nullable=True)
    resultado_esperado = Column(Text, nullable=True)
    fecha_seguimiento = Column(DateTime, nullable=True)
    responsable_seguimiento = Column(String(255), nullable=True)
    conclusion_seguimiento = Column(Text, nullable=True)
    realizado = Column(Boolean, default=False, nullable=False)
    trial827 = Column(String(1), nullable=True)
    
    def __repr__(self):
        return f"<PE_SE_MA(id={self.id})>"


class PE_SE_ME(Base):
    """Modelo para Oportunidades de Mejora"""
    __tablename__ = 'pe_se_me'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    fecha_registro = Column(DateTime, nullable=True)
    registrado_por = Column(String(255), nullable=True)
    oportunidad_de_mejora = Column(String(255), nullable=True)
    descripcion_de_oportunidad_de_mejora = Column(Text, nullable=True)
    analisis_de_la_oportunidad_de_mejora = Column(Text, nullable=True)
    oportunidad_de_mejora_seleccionada = Column(Boolean, default=False, nullable=False)
    responsable_de_seguimiento = Column(String(255), nullable=True)
    fecha_de_seguimiento_de_eficacia_de_acciones = Column(DateTime, nullable=True)
    efecto_deseado = Column(Text, nullable=True)
    seguimiento = Column(Text, nullable=True)
    eficaz = Column(Boolean, default=False, nullable=False)
    fecha_seguimiento = Column(DateTime, nullable=True)
    observaciones = Column(Text, nullable=True)
    cerrado = Column(Boolean, default=False, nullable=False)
    trial827 = Column(String(1), nullable=True)
    
    def __repr__(self):
        return f"<PE_SE_ME(id={self.id})>"


class PE_SE_RE(Base):
    """Modelo para Reuniones"""
    __tablename__ = 'pe_se_re'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    participante_1 = Column(String(255), nullable=True)
    participante_2 = Column(String(255), nullable=True)
    participante_3 = Column(String(255), nullable=True)
    participante_4 = Column(String(255), nullable=True)
    participante_5 = Column(String(255), nullable=True)
    participante_6 = Column(String(255), nullable=True)
    participante_7 = Column(String(255), nullable=True)
    participante_8 = Column(String(255), nullable=True)
    fecha = Column(DateTime, nullable=True)
    medio_de_reunion = Column(String(100), nullable=True)
    tipo_de_revision = Column(String(100), nullable=True)
    comentarios_y_observaciones = Column(Text, nullable=True)
    trial827 = Column(String(1), nullable=True)
    
    def __repr__(self):
        return f"<PE_SE_RE(id={self.id})>"


class PE_SE_SA(Base):
    """Modelo para Salidas de Acciones"""
    __tablename__ = 'pe_se_sa'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    id_re = Column(Integer, nullable=True)
    salida = Column(String(255), nullable=True)
    decision = Column(Text, nullable=True)
    acciones = Column(Text, nullable=True)
    trial827 = Column(String(1), nullable=True)
    
    def __repr__(self):
        return f"<PE_SE_SA(id={self.id})>"


class PE_SE_SS(Base):
    """Modelo para Salidas de Seguimiento"""
    __tablename__ = 'pe_se_ss'
    __table_args__ = {'schema': 'SGApp'}
    
    # NOTA: Esta tabla no tiene primary key en el SQL original
    # Agregamos salidas como primary key
    salidas = Column(String(255), primary_key=True, nullable=False)
    trial827 = Column(String(1), nullable=True)
    
    def __repr__(self):
        return f"<PE_SE_SS(salidas={self.salidas})>"
