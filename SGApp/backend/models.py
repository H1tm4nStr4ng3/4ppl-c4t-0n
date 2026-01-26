"""
Modelos SQLAlchemy para el Sistema SGApp
Base de datos PostgreSQL
"""

from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime

Base = declarative_base()

# ============================================================================
# MÓDULO: PA_DI - Documentación e Información
# ============================================================================

class PA_DI_PR(Base):
    """Procesos de la documentación"""
    __tablename__ = 'pa_di_pr'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    codigo_del_proceso = Column(String(255))
    proceso = Column(String(255))
    vigente = Column(Boolean, default=False, nullable=False)
    trial814 = Column(String(1))
    
    # Relaciones
    registros_accion = relationship("PA_DI_RA", back_populates="proceso_rel")
    
    def __repr__(self):
        return f"<PA_DI_PR(id={self.id}, proceso='{self.proceso}')>"


class PA_DI_FA(Base):
    """Fallas y eventos de la documentación"""
    __tablename__ = 'pa_di_fa'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    registrado_por = Column(String(255), ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    fecha = Column(DateTime)
    evento = Column(Text)
    resuelto = Column(Boolean, default=False, nullable=False)
    trial814 = Column(String(1))
    
    # Relaciones
    registrador = relationship("PA_PE_PE", foreign_keys=[registrado_por])
    
    def __repr__(self):
        return f"<PA_DI_FA(id={self.id}, resuelto={self.resuelto})>"


class PA_DI_RA(Base):
    """Registro de acciones de documentación"""
    __tablename__ = 'pa_di_ra'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha_de_apertura = Column(DateTime)
    registrado_por = Column(String(255), ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    origen_de_documento = Column(String(255))
    tipo_de_documento = Column(String(255))
    proceso = Column(Integer, ForeignKey('SGApp.pa_di_pr.id'))
    codigo_de_documento_global = Column('codigo_de-documento_global', String(255))
    codigo_particular = Column(String(255))
    documento = Column(String(255))
    revisado_por = Column(String(255))
    modificaciones = Column(Text)
    numerales_afectados = Column(Text)
    observaciones = Column(Text)
    aprobado_por = Column(String(255))
    version_nueva = Column(String(255))
    aprobado = Column(Boolean, default=False, nullable=False)
    aplica_comprobacion = Column(Boolean, default=False, nullable=False)
    comentarios_de_comprobacion = Column(Text)
    comprobado = Column(Boolean, default=False, nullable=False)
    ubicacion = Column(String(255))
    fecha_de_cierre = Column(DateTime)
    trial814 = Column(String(1))
    
    # Relaciones
    registrador = relationship("PA_PE_PE", foreign_keys=[registrado_por])
    proceso_rel = relationship("PA_DI_PR", back_populates="registros_accion")
    
    def __repr__(self):
        return f"<PA_DI_RA(id={self.id}, documento='{self.documento}')>"


# ============================================================================
# MÓDULO: PA_EQ - Equipamiento
# ============================================================================

class PA_EQ_AC(Base):
    """Actividades de equipamiento"""
    __tablename__ = 'pa_eq_ac'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    actividad = Column(String(255), unique=True, nullable=False)
    descripcion = Column(Text)
    trial814 = Column(String(1))
    
    # Relaciones
    programas_actividad = relationship("PA_EQ_PR", back_populates="actividad_rel")
    
    def __repr__(self):
        return f"<PA_EQ_AC(id={self.id}, actividad='{self.actividad}')>"


class PA_EQ_EQ(Base):
    """Equipos - Tabla principal de equipamiento"""
    __tablename__ = 'pa_eq_eq'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    equipamiento = Column(String(255))
    codigo_interno = Column(String(255), unique=True, nullable=False)
    marca = Column(String(255))
    serie = Column(String(255))
    material = Column(String(255))
    numero_de_piezas = Column(String(255))
    max_vn = Column(String(255))
    d = Column(String(255))
    clase_de_exactitud = Column(String(255))
    ubicacion = Column(String(255))
    comentarios = Column(Text)
    puesta_en_funcionamiento = Column(DateTime)
    estado = Column(String(255))
    requiere = Column(Text)
    frecuencia_de_calibracion = Column(String(255))
    frecuencia_de_mantenimiento = Column(String(255))
    frecuencia_de_comprobacion_intermedia = Column(String(255))
    frecuencia_de_calificacion = Column(String(255))
    trial814 = Column(String(1))
    
    # Relaciones
    listas_equipo = relationship("PA_EQ_LE", back_populates="equipo")
    calibraciones = relationship("PA_EQ_CA", back_populates="equipo")
    mantenimientos = relationship("PA_EQ_MA", back_populates="equipo")
    programas_equipo = relationship("PA_EQ_PR", back_populates="equipo")
    verificaciones_patron = relationship("PA_EQ_VE", foreign_keys="PA_EQ_VE.set_patron", back_populates="equipo_patron")
    verificaciones_comparado = relationship("PA_EQ_VE", foreign_keys="PA_EQ_VE.set_comparado", back_populates="equipo_comparado")
    comprobaciones_intermedias = relationship("PA_EQ_CI", back_populates="balanza")
    monitoreos_ambiente = relationship("PA_IA_AM", back_populates="instrumento_rel")
    
    def __repr__(self):
        return f"<PA_EQ_EQ(codigo_interno='{self.codigo_interno}', equipamiento='{self.equipamiento}')>"


class PA_EQ_LE(Base):
    """Lista de equipos"""
    __tablename__ = 'pa_eq_le'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    lista_de_equipos = Column(String(255))
    equipamiento = Column(String(255), ForeignKey('SGApp.pa_eq_eq.codigo_interno'), nullable=False)
    trial814 = Column(String(1))
    
    # Relaciones
    equipo = relationship("PA_EQ_EQ", back_populates="listas_equipo")
    
    def __repr__(self):
        return f"<PA_EQ_LE(id={self.id}, lista='{self.lista_de_equipos}')>"


class PA_EQ_CA(Base):
    """Calibraciones de equipos"""
    __tablename__ = 'pa_eq_ca'
    __table_args__ = {'schema': 'SGApp'}
    
    id_equi = Column(Integer, primary_key=True, autoincrement=True)
    registrado_por = Column(String(255))
    fecha = Column(DateTime)
    equipamiento = Column(String(255), ForeignKey('SGApp.pa_eq_eq.codigo_interno'), nullable=False)
    certificado = Column(String(255), unique=True, nullable=False)
    ente_calibrador = Column(String(255))
    fecha_de_calibracion = Column(DateTime)
    unidades = Column(String(255))
    observaciones = Column(Text)
    apto = Column(Boolean, default=False, nullable=False)
    regla = Column(String(255))
    trial814 = Column(String(1))
    
    # Relaciones
    equipo = relationship("PA_EQ_EQ", back_populates="calibraciones")
    datos_calibracion = relationship("PA_EQ_DC", back_populates="calibracion")
    datos_exactitud = relationship("PA_EQ_EX", back_populates="calibracion")
    datos_homogeneidad = relationship("PA_EQ_HM", back_populates="calibracion")
    datos_repetibilidad = relationship("PA_EQ_RP", back_populates="calibracion")
    
    def __repr__(self):
        return f"<PA_EQ_CA(certificado='{self.certificado}')>"


class PA_EQ_CI(Base):
    """Comprobaciones intermedias de equipos"""
    __tablename__ = 'pa_eq_ci'
    __table_args__ = {'schema': 'SGApp'}
    
    id_equi = Column(Integer, primary_key=True, autoincrement=True)
    registrado_por = Column(String(255))
    fecha = Column(DateTime)
    equipamiento = Column(String(255))
    balanza_utilizada = Column(String(255), ForeignKey('SGApp.pa_eq_eq.codigo_interno'))
    unidades = Column(String(255))
    observaciones = Column(Text)
    promedio = Column(Float, default=0)
    desv_est = Column(Float, default=0)
    tol_sistematico = Column(Float, default=0)
    conclusion_sistematico = Column(String(255))
    temperatura = Column(Float, default=0)
    lugar = Column(String(255))
    presion_hpa = Column(Float, default=0)
    humedad_relativa = Column(Float, default=0)
    en = Column(Float, default=0)
    conclusion_en = Column(String(255))
    volumen_nominal = Column(Float, default=0)
    valor = Column(Float, default=0)
    incertidumbre = Column(Float, default=0)
    tipo_comprobacion = Column(String(255))
    tempprogramada = Column(Float, default=0)
    termometro_id = Column(String(255))
    cg = Column(Float, default=0)
    cgk = Column(Float, default=0)
    trial814 = Column(String(1))
    
    # Relaciones
    balanza = relationship("PA_EQ_EQ", back_populates="comprobaciones_intermedias")
    comprobaciones_balanza = relationship("PA_EQ_CB", back_populates="comprobacion_intermedia")
    comprobaciones_volumetricas = relationship("PA_EQ_CV", back_populates="comprobacion_intermedia")
    comprobaciones_horno = relationship("PA_EQ_CH", back_populates="comprobacion_intermedia")
    
    def __repr__(self):
        return f"<PA_EQ_CI(id={self.id_equi}, equipamiento='{self.equipamiento}')>"


class PA_EQ_CB(Base):
    """Comprobación de balanzas"""
    __tablename__ = 'pa_eq_cb'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_ci = Column(Integer, ForeignKey('SGApp.pa_eq_ci.id_equi'))
    tipoprueba = Column(String(255))
    pesapatron_id = Column(String(255))
    posicion = Column(String(255))
    lectura_balanza = Column(Float, default=0)
    lectura_corregida = Column(Float, default=0)
    trial814 = Column(String(1))
    
    # Relaciones
    comprobacion_intermedia = relationship("PA_EQ_CI", back_populates="comprobaciones_balanza")
    
    def __repr__(self):
        return f"<PA_EQ_CB(id={self.id})>"


class PA_EQ_CV(Base):
    """Comprobación volumétrica"""
    __tablename__ = 'pa_eq_cv'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_ci = Column(Integer, ForeignKey('SGApp.pa_eq_ci.id_equi'))
    matraz_vacio = Column(Float, default=0)
    corr1 = Column(Float, default=0)
    matraz_lleno = Column(Float, default=0)
    corr2 = Column(Float, default=0)
    masa_h2o = Column(Float, default=0)
    densidad = Column(Float, default=0)
    volumen = Column(Float, default=0)
    trial814 = Column(String(1))
    
    # Relaciones
    comprobacion_intermedia = relationship("PA_EQ_CI", back_populates="comprobaciones_volumetricas")
    
    def __repr__(self):
        return f"<PA_EQ_CV(id={self.id})>"


class PA_EQ_CH(Base):
    """Comprobación de hornos/cámaras"""
    __tablename__ = 'pa_eq_ch'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_ci = Column(Integer, ForeignKey('SGApp.pa_eq_ci.id_equi'))
    posicion = Column(String(255))
    temppatron_leida = Column(Float, default=0)
    tempequipo_leida = Column(Float, default=0)
    diferencia = Column(Float, default=0)
    resultadopunto = Column(String(255))
    trial814 = Column(String(1))
    
    # Relaciones
    comprobacion_intermedia = relationship("PA_EQ_CI", back_populates="comprobaciones_horno")
    
    def __repr__(self):
        return f"<PA_EQ_CH(id={self.id})>"


class PA_EQ_DC(Base):
    """Datos de calibración"""
    __tablename__ = 'pa_eq_dc'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_ca = Column(String(255), ForeignKey('SGApp.pa_eq_ca.certificado'))
    valor_nominal = Column(Float, default=0)
    referencia = Column(String(255))
    correccion_reportada = Column(Float, default=0)
    incertidumbre = Column(Float, default=0)
    tolerancia_de_medicion = Column(Float, default=0)
    conformidad = Column(String(255))
    trial814 = Column(String(1))
    
    # Relaciones
    calibracion = relationship("PA_EQ_CA", back_populates="datos_calibracion")
    
    def __repr__(self):
        return f"<PA_EQ_DC(id={self.id})>"


class PA_EQ_EX(Base):
    """Datos de exactitud de calibración"""
    __tablename__ = 'pa_eq_ex'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_ca = Column(String(255), ForeignKey('SGApp.pa_eq_ca.certificado'))
    posicion = Column(String(255))
    resultado = Column(Float, default=0)
    resultado_c = Column(Float, default=0)
    trial814 = Column(String(1))
    
    # Relaciones
    calibracion = relationship("PA_EQ_CA", back_populates="datos_exactitud")
    
    def __repr__(self):
        return f"<PA_EQ_EX(id={self.id})>"


class PA_EQ_HM(Base):
    """Datos de homogeneidad de calibración"""
    __tablename__ = 'pa_eq_hm'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_ca = Column(String(255), ForeignKey('SGApp.pa_eq_ca.certificado'))
    posicion = Column(String(255))
    lectura1 = Column(Float, default=0)
    lectura2 = Column(Float, default=0)
    lectura3 = Column(Float, default=0)
    promedio = Column(Float, default=0)
    desviacion_del_promedio = Column(Float, default=0)
    trial814 = Column(String(1))
    
    # Relaciones
    calibracion = relationship("PA_EQ_CA", back_populates="datos_homogeneidad")
    
    def __repr__(self):
        return f"<PA_EQ_HM(id={self.id})>"


class PA_EQ_RP(Base):
    """Datos de repetibilidad de calibración"""
    __tablename__ = 'pa_eq_rp'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_ca = Column(String(255), ForeignKey('SGApp.pa_eq_ca.certificado'))
    lectura1 = Column(Float, default=0)
    lectura2 = Column(Float, default=0)
    lectura3 = Column(Float, default=0)
    promedio = Column(Float, default=0)
    trial814 = Column(String(1))
    
    # Relaciones
    calibracion = relationship("PA_EQ_CA", back_populates="datos_repetibilidad")
    
    def __repr__(self):
        return f"<PA_EQ_RP(id={self.id})>"


class PA_EQ_MA(Base):
    """Mantenimiento de equipos"""
    __tablename__ = 'pa_eq_ma'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    registrado_por = Column('registrado-por', String(255), ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    fecha = Column(DateTime)
    equipamiento = Column(String(255), ForeignKey('SGApp.pa_eq_eq.codigo_interno'), nullable=False)
    descripcion_de_mantenimiento = Column(Text)
    realizado_por = Column(String(255))
    autorizado_por = Column(String(255))
    trial814 = Column(String(1))
    
    # Relaciones
    registrador = relationship("PA_PE_PE", foreign_keys=[registrado_por])
    equipo = relationship("PA_EQ_EQ", back_populates="mantenimientos")
    
    def __repr__(self):
        return f"<PA_EQ_MA(id={self.id})>"


class PA_EQ_RE(Base):
    """Reactivos"""
    __tablename__ = 'pa_eq_re'
    __table_args__ = {'schema': 'SGApp'}
    
    id_reactivo = Column(String(255), primary_key=True)
    descripcion = Column(String(255))
    marca = Column(String(255))
    fecha_apert = Column(DateTime)
    fecha_venc = Column(DateTime)
    cantidad_aprox = Column(Float, default=0)
    unidad = Column(String(255))
    ubicacion = Column(String(255))
    lote = Column(String(255))
    concentracion = Column(String(255))
    factor = Column(Float, default=0)
    densidad_g_cm3 = Column(Float, default=0)
    pureza = Column(Float, default=0)
    tipo = Column(String(255))
    proveedor = Column(String(255))
    comentarios = Column(Text)
    ensayo_estabilidad = Column(String(255))
    trial814 = Column(String(1))
    
    # Relaciones
    movimientos = relationship("PA_EQ_MO", back_populates="reactivo")
    
    def __repr__(self):
        return f"<PA_EQ_RE(id_reactivo='{self.id_reactivo}')>"


class PA_EQ_MO(Base):
    """Movimientos de reactivos"""
    __tablename__ = 'pa_eq_mo'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    registrado_por = Column(String(255), ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    fecha = Column(DateTime)
    id_reactivo = Column(String(255), ForeignKey('SGApp.pa_eq_re.id_reactivo'))
    id_adquisicion = Column(Integer, ForeignKey('SGApp.pa_ps_ad.id'))
    tipo = Column(String(255))
    cantidad = Column(Float, default=0)
    unidad = Column(String(255))
    comentarios = Column(Text)
    trial814 = Column(String(1))
    
    # Relaciones
    registrador = relationship("PA_PE_PE", foreign_keys=[registrado_por])
    reactivo = relationship("PA_EQ_RE", back_populates="movimientos")
    adquisicion = relationship("PA_PS_AD", back_populates="movimientos_reactivo")
    
    def __repr__(self):
        return f"<PA_EQ_MO(id={self.id})>"


class PA_EQ_PA(Base):
    """Programas de actividades de equipamiento"""
    __tablename__ = 'pa_eq_pa'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    registrado_por = Column(String(255), ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    fecha = Column(DateTime)
    programa = Column(String(255))
    trial814 = Column(String(1))
    
    # Relaciones
    registrador = relationship("PA_PE_PE", foreign_keys=[registrado_por])
    detalles_programa = relationship("PA_EQ_PR", back_populates="programa")
    
    def __repr__(self):
        return f"<PA_EQ_PA(id={self.id}, programa='{self.programa}')>"


class PA_EQ_PR(Base):
    """Detalles del programa de actividades"""
    __tablename__ = 'pa_eq_pr'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    equipamiento = Column(String(255), ForeignKey('SGApp.pa_eq_eq.codigo_interno'))
    actividad = Column(String(255), ForeignKey('SGApp.pa_eq_ac.actividad'))
    fecha_de_actuacion = Column(DateTime)
    realizado = Column(Boolean, default=False)
    fecha_realizado = Column(DateTime)
    id_pa = Column(Integer, ForeignKey('SGApp.pa_eq_pa.id'))
    trial814 = Column(String(1))
    
    # Relaciones
    equipo = relationship("PA_EQ_EQ", back_populates="programas_equipo")
    actividad_rel = relationship("PA_EQ_AC", back_populates="programas_actividad")
    programa = relationship("PA_EQ_PA", back_populates="detalles_programa")
    
    def __repr__(self):
        return f"<PA_EQ_PR(id={self.id})>"


class PA_EQ_MR(Base):
    """Material de referencia"""
    __tablename__ = 'pa_eq_mr'
    __table_args__ = {'schema': 'SGApp'}
    
    codigo_interno = Column(String(255), primary_key=True)
    material_de_referencia = Column(String(255))
    fabricante_proveedor = Column(String(255))
    numero_de_certificado = Column(String(255))
    lote = Column(String(255))
    fecha_de_apertura = Column(DateTime)
    fecha_de_vencimiento = Column(DateTime)
    ubicacion = Column(String(255))
    cantidad_aprox = Column(Float, default=0)
    unidad = Column(String(255))
    comentarios = Column(Text)
    estado = Column(String(255))
    cantidad_disponible = Column(Float, default=0)
    tipo = Column(String(255))
    trial814 = Column(String(1))
    
    # Relaciones
    movimientos = relationship("PA_EQ_MV", back_populates="material_referencia")
    
    def __repr__(self):
        return f"<PA_EQ_MR(codigo_interno='{self.codigo_interno}')>"


class PA_EQ_MV(Base):
    """Movimientos de material de referencia"""
    __tablename__ = 'pa_eq_mv'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha = Column(DateTime)
    id_mr = Column(String(255), ForeignKey('SGApp.pa_eq_mr.codigo_interno'))
    tipo = Column(String(255))
    cantidad = Column(Float, default=0)
    unidad = Column(String(255))
    trial814 = Column(String(1))
    
    # Relaciones
    material_referencia = relationship("PA_EQ_MR", back_populates="movimientos")
    
    def __repr__(self):
        return f"<PA_EQ_MV(id={self.id})>"


class PA_EQ_VE(Base):
    """Verificación de equipos"""
    __tablename__ = 'pa_eq_ve'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    registrado_por = Column(String(255), ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    fecha = Column(DateTime)
    set_patron = Column(String(255), ForeignKey('SGApp.pa_eq_eq.codigo_interno'))
    set_comparado = Column(String(255), ForeignKey('SGApp.pa_eq_eq.codigo_interno'), nullable=False)
    temperatura_ºc = Column(Float, default=0)
    humedad_relativa = Column(Float, default=0)
    
    # Campos de verificación - simplificados (hay muchos en la tabla real)
    observaciones = Column(Text)
    conclusion = Column(String(255))
    trial814 = Column(String(1))
    
    # Relaciones
    registrador = relationship("PA_PE_PE", foreign_keys=[registrado_por])
    equipo_patron = relationship("PA_EQ_EQ", foreign_keys=[set_patron], back_populates="verificaciones_patron")
    equipo_comparado = relationship("PA_EQ_EQ", foreign_keys=[set_comparado], back_populates="verificaciones_comparado")
    
    def __repr__(self):
        return f"<PA_EQ_VE(id={self.id})>"


# ============================================================================
# MÓDULO: PA_PE - Personal
# ============================================================================

class PA_PE_DE(Base):
    """Descripción de cargos/puestos"""
    __tablename__ = 'pa_pe_de'
    __table_args__ = {'schema': 'SGApp'}
    
    abreviacion = Column(String(255), primary_key=True)
    cargo = Column(String(255))
    trial814 = Column(String(1))
    
    # Relaciones
    personal = relationship("PA_PE_PE", back_populates="cargo_rel", foreign_keys="PA_PE_PE.cargo")
    requisitos = relationship("PA_PE_RQ", back_populates="cargo_req_rel")
    selecciones = relationship("PA_PE_SP", back_populates="puesto_rel")
    inducciones = relationship("PA_PE_IS", back_populates="cargo_rel")
    autorizaciones = relationship("PA_PE_AU", back_populates="cargo_rel")
    
    def __repr__(self):
        return f"<PA_PE_DE(abreviacion='{self.abreviacion}', cargo='{self.cargo}')>"


class PA_PE_PE(Base):
    """Personal - Tabla principal"""
    __tablename__ = 'pa_pe_pe'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    abreviatura = Column(String(255), unique=True, nullable=False)
    personal = Column(String(255))
    cargo = Column(String(255), ForeignKey('SGApp.pa_pe_de.abreviacion'))
    fecha_de_contratacion = Column(DateTime)
    fecha_de_terminacion = Column(DateTime)
    ci = Column(String(255))
    activo = Column(Boolean, default=False)
    tipo_usuario = Column(String(255))
    usuario = Column(String(255))
    contraseña = Column(String(255))
    correo = Column(String(255))
    telefono = Column(String(255))
    firma = Column(String(255))
    firma_simple = Column(String(255))
    genero = Column(String(255))
    fecha_nacimiento = Column(DateTime)
    direccion = Column(String(255))
    trial814 = Column(String(1))
    
    # Relaciones
    cargo_rel = relationship("PA_PE_DE", back_populates="personal", foreign_keys=[cargo])
    competencias = relationship("PA_PE_CV", back_populates="personal_rel")
    seguimientos = relationship("PA_PE_SE", back_populates="personal_rel", foreign_keys="PA_PE_SE.personal")
    autorizaciones_recibidas = relationship("PA_PE_AU", back_populates="autorizado_rel")
    
    def __repr__(self):
        return f"<PA_PE_PE(abreviatura='{self.abreviatura}', personal='{self.personal}')>"


class PA_PE_EC(Base):
    """Elementos de competencia"""
    __tablename__ = 'pa_pe_ec'
    __table_args__ = {'schema': 'SGApp'}
    
    elemento_de_competencia = Column(String(255), primary_key=True)
    descripcion = Column(Text)
    trial814 = Column(String(1))
    
    # Relaciones
    evaluaciones = relationship("PA_PE_CV", back_populates="requisito_rel")
    
    def __repr__(self):
        return f"<PA_PE_EC(elemento='{self.elemento_de_competencia}')>"


class PA_PE_CV(Base):
    """Competencias y evaluación del personal"""
    __tablename__ = 'pa_pe_cv'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    personal = Column(String(255), ForeignKey('SGApp.pa_pe_pe.abreviatura'), nullable=False)
    requisito_de_competencia = Column(String(255), ForeignKey('SGApp.pa_pe_ec.elemento_de_competencia'), nullable=False)
    responsable = Column(String(255))
    fecha_de_evaluacion = Column(DateTime)
    metodo = Column(String(255))
    resultado = Column(String(255))
    eficaz = Column(Boolean, default=False)
    comentarios = Column(Text)
    trial814 = Column(String(1))
    
    # Relaciones
    personal_rel = relationship("PA_PE_PE", back_populates="competencias")
    requisito_rel = relationship("PA_PE_EC", back_populates="evaluaciones")
    
    def __repr__(self):
        return f"<PA_PE_CV(id={self.id})>"


class PA_PE_FG(Base):
    """Formas de generación"""
    __tablename__ = 'pa_pe_fg'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    forma_de_generacion = Column(String(255))
    trial814 = Column(String(1))
    
    # Relaciones
    planes = relationship("PA_PE_PL", back_populates="forma_generacion_rel")
    
    def __repr__(self):
        return f"<PA_PE_FG(id={self.id})>"


class PA_PE_PL(Base):
    """Planes de capacitación"""
    __tablename__ = 'pa_pe_pl'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    item_del_programa = Column(String(255))
    fecha_de_registro = Column(DateTime)
    tipo_de_plan = Column(String(255))
    elaborado_por = Column(String(255), ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    autorizado_por = Column(String(255), ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    asistentes = Column(Text)  # Almacena valores múltiples
    evaluadores = Column(Text)  # Almacena valores múltiples
    forma_generacion = Column(Integer, ForeignKey('SGApp.pa_pe_fg.id'))
    objetivo = Column(Text)
    contenido = Column(Text)
    fecha_programada = Column(DateTime)
    fecha_realizada = Column(DateTime)
    horas = Column(Float, default=0)
    responsable = Column(String(255))
    trial814 = Column(String(1))
    
    # Relaciones
    elaborador = relationship("PA_PE_PE", foreign_keys=[elaborado_por])
    autorizador = relationship("PA_PE_PE", foreign_keys=[autorizado_por])
    forma_generacion_rel = relationship("PA_PE_FG", back_populates="planes")
    
    def __repr__(self):
        return f"<PA_PE_PL(id={self.id})>"


class PA_PE_RQ(Base):
    """Requisitos de personal"""
    __tablename__ = 'pa_pe_rq'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    cargo_req = Column(String(255), ForeignKey('SGApp.pa_pe_de.abreviacion'), nullable=False)
    responsable = Column(String(255), ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    edad_minima = Column(Integer)
    edad_maxima = Column(Integer)
    genero = Column(String(255))
    educacion_requerida = Column(Text)
    experiencia_requerida = Column(Text)
    conocimientos_especificos = Column(Text)
    habilidades = Column(Text)
    trial814 = Column(String(1))
    
    # Relaciones
    cargo_req_rel = relationship("PA_PE_DE", back_populates="requisitos")
    responsable_rel = relationship("PA_PE_PE", foreign_keys=[responsable])
    seguimientos = relationship("PA_PE_SE", back_populates="requisitos_rel")
    
    def __repr__(self):
        return f"<PA_PE_RQ(id={self.id})>"


class PA_PE_SE(Base):
    """Seguimiento y evaluación del personal"""
    __tablename__ = 'pa_pe_se'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    personal = Column(String(255), ForeignKey('SGApp.pa_pe_pe.abreviatura'), nullable=False)
    requisitos = Column(Integer, ForeignKey('SGApp.pa_pe_rq.id'), nullable=False)
    responsable = Column(String(255), ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    fecha = Column(DateTime)
    puntaje_total = Column(Float, default=0)
    calificacion = Column(String(255))
    observaciones = Column(Text)
    trial814 = Column(String(1))
    
    # Relaciones
    personal_rel = relationship("PA_PE_PE", foreign_keys=[personal], back_populates="seguimientos")
    requisitos_rel = relationship("PA_PE_RQ", back_populates="seguimientos")
    responsable_rel = relationship("PA_PE_PE", foreign_keys=[responsable])
    
    def __repr__(self):
        return f"<PA_PE_SE(id={self.id})>"


class PA_PE_SP(Base):
    """Selección de personal"""
    __tablename__ = 'pa_pe_sp'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    proceso_de_seleccion = Column(String(255))
    puesto = Column(String(255), ForeignKey('SGApp.pa_pe_de.abreviacion'), nullable=False)
    evaluadores = Column(Text)
    fecha_apertura = Column(DateTime)
    fecha_cierre = Column(DateTime)
    trial814 = Column(String(1))
    
    # Relaciones
    puesto_rel = relationship("PA_PE_DE", back_populates="selecciones")
    postulantes = relationship("PA_PE_PO", back_populates="proceso_seleccion_rel")
    
    def __repr__(self):
        return f"<PA_PE_SP(id={self.id})>"


class PA_PE_PO(Base):
    """Postulantes"""
    __tablename__ = 'pa_pe_po'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    proceso_de_seleccion = Column(Integer, ForeignKey('SGApp.pa_pe_sp.id'), nullable=False)
    nombre_completo = Column(String(255))
    ci = Column(String(255))
    fecha_nacimiento = Column(DateTime)
    telefono = Column(String(255))
    correo = Column(String(255))
    direccion = Column(String(255))
    cv = Column(String(255))
    puntaje = Column(Float, default=0)
    observaciones = Column(Text)
    seleccionado = Column(Boolean, default=False)
    trial814 = Column(String(1))
    
    # Relaciones
    proceso_seleccion_rel = relationship("PA_PE_SP", back_populates="postulantes")
    
    def __repr__(self):
        return f"<PA_PE_PO(id={self.id}, nombre='{self.nombre_completo}')>"


class PA_PE_IS(Base):
    """Inducción del personal"""
    __tablename__ = 'pa_pe_is'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    cargo = Column(String(255), ForeignKey('SGApp.pa_pe_de.abreviacion'))
    descripcion = Column(Text)
    trial814 = Column(String(1))
    
    # Relaciones
    cargo_rel = relationship("PA_PE_DE", back_populates="inducciones")
    items = relationship("PA_PE_IE", back_populates="induccion")
    
    def __repr__(self):
        return f"<PA_PE_IS(id={self.id})>"


class PA_PE_IE(Base):
    """Items de inducción"""
    __tablename__ = 'pa_pe_ie'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_is = Column(Integer, ForeignKey('SGApp.pa_pe_is.id'))
    item = Column(String(255))
    descripcion = Column(Text)
    trial814 = Column(String(1))
    
    # Relaciones
    induccion = relationship("PA_PE_IS", back_populates="items")
    
    def __repr__(self):
        return f"<PA_PE_IE(id={self.id})>"


class PA_PE_AU(Base):
    """Autorizaciones del personal"""
    __tablename__ = 'pa_pe_au'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    autorizado_a = Column(String(255), ForeignKey('SGApp.pa_pe_pe.abreviatura'), nullable=False)
    cargo = Column(String(255), ForeignKey('SGApp.pa_pe_de.abreviacion'))
    autorizacion = Column(String(255))
    fecha_autorizacion = Column(DateTime)
    vigente = Column(Boolean, default=False)
    trial814 = Column(String(1))
    
    # Relaciones
    autorizado_rel = relationship("PA_PE_PE", back_populates="autorizaciones_recibidas")
    cargo_rel = relationship("PA_PE_DE", back_populates="autorizaciones")
    
    def __repr__(self):
        return f"<PA_PE_AU(id={self.id})>"


class PA_PE_PR(Base):
    """Programas de personal"""
    __tablename__ = 'pa_pe_pr'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    registrado_por = Column(String(255), ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    fecha = Column(DateTime)
    dirigido_a = Column(Text)
    actividad = Column(String(255))
    lugar = Column(String(255))
    observaciones = Column(Text)
    trial814 = Column(String(1))
    
    # Relaciones
    registrador = relationship("PA_PE_PE", foreign_keys=[registrado_por])
    
    def __repr__(self):
        return f"<PA_PE_PR(id={self.id})>"


class PA_PE_SU(Base):
    """Supervisión del personal"""
    __tablename__ = 'pa_pe_su'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    supervisores = Column(Text)
    fecha = Column(DateTime)
    area = Column(String(255))
    observaciones = Column(Text)
    trial814 = Column(String(1))
    
    def __repr__(self):
        return f"<PA_PE_SU(id={self.id})>"


class PA_PE_EF(Base):
    """Evaluación de eficacia"""
    __tablename__ = 'pa_pe_ef'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String(255))
    item_evaluado = Column(String(255))
    fecha_evaluacion = Column(DateTime)
    resultado = Column(String(255))
    eficaz = Column(Boolean, default=False)
    observaciones = Column(Text)
    trial814 = Column(String(1))
    
    def __repr__(self):
        return f"<PA_PE_EF(id={self.id})>"


# ============================================================================
# MÓDULO: PA_IA - Infraestructura y Ambiente
# ============================================================================

class PA_IA_AR(Base):
    """Áreas"""
    __tablename__ = 'pa_ia_ar'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    area = Column(String(255))
    trial814 = Column(String(1))
    
    # Relaciones
    monitoreos = relationship("PA_IA_AM", back_populates="area_rel")
    
    def __repr__(self):
        return f"<PA_IA_AR(id={self.id}, area='{self.area}')>"


class PA_IA_AM(Base):
    """Ambiente y monitoreo"""
    __tablename__ = 'pa_ia_am'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    instrumento = Column(String(255), ForeignKey('SGApp.pa_eq_eq.codigo_interno'))
    area = Column(Integer, ForeignKey('SGApp.pa_ia_ar.id'))
    parametro = Column(String(255))
    especificacion = Column(String(255))
    frecuencia = Column(String(255))
    trial814 = Column(String(1))
    
    # Relaciones
    instrumento_rel = relationship("PA_EQ_EQ", back_populates="monitoreos_ambiente")
    area_rel = relationship("PA_IA_AR", back_populates="monitoreos")
    historial = relationship("PA_IA_AH", back_populates="monitoreo")
    
    def __repr__(self):
        return f"<PA_IA_AM(id={self.id})>"


class PA_IA_AH(Base):
    """Historial de ambiente"""
    __tablename__ = 'pa_ia_ah'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    registrado_por = Column(String(255), ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    id_am = Column(Integer, ForeignKey('SGApp.pa_ia_am.id'))
    fecha = Column(DateTime)
    valor = Column(Float, default=0)
    conforme = Column(Boolean, default=False)
    observaciones = Column(Text)
    trial814 = Column(String(1))
    
    # Relaciones
    registrador = relationship("PA_PE_PE", foreign_keys=[registrado_por])
    monitoreo = relationship("PA_IA_AM", back_populates="historial")
    
    def __repr__(self):
        return f"<PA_IA_AH(id={self.id})>"


class PA_IA_LI(Base):
    """Lista de infraestructura"""
    __tablename__ = 'pa_ia_li'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    registrado_por = Column(String(255), ForeignKey('SGApp.pa_pe_pe.abreviatura'), nullable=False)
    lista_de_infraestructura = Column(String(255))
    descripcion = Column(Text)
    fecha = Column(DateTime)
    trial814 = Column(String(1))
    
    # Relaciones
    registrador = relationship("PA_PE_PE", foreign_keys=[registrado_por])
    elementos = relationship("PA_IA_LE", back_populates="lista")
    
    def __repr__(self):
        return f"<PA_IA_LI(id={self.id})>"


class PA_IA_LE(Base):
    """Elementos de lista de infraestructura"""
    __tablename__ = 'pa_ia_le'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_li = Column(Integer, ForeignKey('SGApp.pa_ia_li.id'))
    elemento = Column(String(255))
    descripcion = Column(Text)
    trial814 = Column(String(1))
    
    # Relaciones
    lista = relationship("PA_IA_LI", back_populates="elementos")
    
    def __repr__(self):
        return f"<PA_IA_LE(id={self.id})>"


class PA_IA_CA(Base):
    """Condiciones ambientales"""
    __tablename__ = 'pa_ia_ca'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    registrado_por = Column(String(255), ForeignKey('SGApp.pa_pe_pe.abreviatura'), nullable=False)
    condiciones_ambientales = Column(String(255))
    descripcion = Column(Text)
    fecha = Column(DateTime)
    trial814 = Column(String(1))
    
    # Relaciones
    registrador = relationship("PA_PE_PE", foreign_keys=[registrado_por])
    
    def __repr__(self):
        return f"<PA_IA_CA(id={self.id})>"


class PA_IA_RA(Base):
    """Requisitos ambientales"""
    __tablename__ = 'pa_ia_ra'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    registrado_por = Column(String(255), ForeignKey('SGApp.pa_pe_pe.abreviatura'), nullable=False)
    id_requisitos_condiciones_ambientales = Column(String(255))
    fecha = Column(DateTime)
    trial814 = Column(String(1))
    
    # Relaciones
    registrador = relationship("PA_PE_PE", foreign_keys=[registrado_por])
    seguimientos = relationship("PA_IA_SA", back_populates="requisito_ambiental")
    
    def __repr__(self):
        return f"<PA_IA_RA(id={self.id})>"


class PA_IA_SA(Base):
    """Seguimiento de requisitos ambientales"""
    __tablename__ = 'pa_ia_sa'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_requisitos_condiciones_ambientales = Column(Integer, ForeignKey('SGApp.pa_ia_ra.id'), nullable=False)
    seguimiento = Column(String(255))
    trial814 = Column(String(1))
    
    # Relaciones
    requisito_ambiental = relationship("PA_IA_RA", back_populates="seguimientos")
    
    def __repr__(self):
        return f"<PA_IA_SA(id={self.id})>"


class PA_IA_RI(Base):
    """Requisitos de instalación"""
    __tablename__ = 'pa_ia_ri'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    registrado_por = Column(String(255), ForeignKey('SGApp.pa_pe_pe.abreviatura'), nullable=False)
    id_requisitos_de_instalacion = Column(String(255))
    fecha = Column(DateTime)
    trial814 = Column(String(1))
    
    # Relaciones
    registrador = relationship("PA_PE_PE", foreign_keys=[registrado_por])
    seguimientos = relationship("PA_IA_SI", back_populates="requisito_instalacion")
    
    def __repr__(self):
        return f"<PA_IA_RI(id={self.id})>"


class PA_IA_SI(Base):
    """Seguimiento de requisitos de instalación"""
    __tablename__ = 'pa_ia_si'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_requisitos_de_instalacion = Column(Integer, ForeignKey('SGApp.pa_ia_ri.id'), nullable=False)
    registrado_por = Column(String(255), ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    seguimiento = Column(String(255))
    trial814 = Column(String(1))
    
    # Relaciones
    requisito_instalacion = relationship("PA_IA_RI", back_populates="seguimientos")
    registrador = relationship("PA_PE_PE", foreign_keys=[registrado_por])
    
    def __repr__(self):
        return f"<PA_IA_SI(id={self.id})>"


# ============================================================================
# MÓDULO: PA_PS - Productos y Servicios
# ============================================================================

class PA_PS_PS(Base):
    """Productos y Servicios - Tabla principal"""
    __tablename__ = 'pa_ps_ps'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    producto_servicio = Column(String(255))
    tipo = Column(String(255))
    descripcion = Column(Text)
    codigo = Column(String(255))
    vigente = Column(Boolean, default=False)
    trial814 = Column(String(1))
    
    # Relaciones
    adquisiciones = relationship("PA_PS_AD", back_populates="producto_servicio_rel")
    
    def __repr__(self):
        return f"<PA_PS_PS(id={self.id}, codigo='{self.codigo}')>"


class PA_PS_AD(Base):
    """Adquisiciones"""
    __tablename__ = 'pa_ps_ad'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    registrado_por = Column(String(255), ForeignKey('SGApp.pa_pe_pe.abreviatura'), nullable=False)
    fecha = Column(DateTime)
    producto_o_servicio = Column(Integer, ForeignKey('SGApp.pa_ps_ps.id'))
    descripcion = Column(Text)
    cantidad = Column(Float, default=0)
    unidad = Column(String(255))
    proveedor_seleccionado = Column(String(255))
    monto = Column(Float, default=0)
    estado = Column(String(255))
    observaciones = Column(Text)
    trial814 = Column(String(1))
    
    # Relaciones
    registrador = relationship("PA_PE_PE", foreign_keys=[registrado_por])
    producto_servicio_rel = relationship("PA_PS_PS", back_populates="adquisiciones")
    ordenes_servicio = relationship("PA_PS_OS", back_populates="adquisicion")
    evaluaciones_proveedor = relationship("PA_PS_EV", back_populates="adquisicion")
    movimientos_reactivo = relationship("PA_EQ_MO", back_populates="adquisicion")
    
    def __repr__(self):
        return f"<PA_PS_AD(id={self.id})>"


class PA_PS_OS(Base):
    """Órdenes de servicio"""
    __tablename__ = 'pa_ps_os'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_ad = Column(Integer, ForeignKey('SGApp.pa_ps_ad.id'), nullable=False)
    numero_orden = Column(String(255))
    fecha_emision = Column(DateTime)
    fecha_entrega_esperada = Column(DateTime)
    fecha_entrega_real = Column(DateTime)
    estado = Column(String(255))
    trial814 = Column(String(1))
    
    # Relaciones
    adquisicion = relationship("PA_PS_AD", back_populates="ordenes_servicio")
    
    def __repr__(self):
        return f"<PA_PS_OS(id={self.id}, numero='{self.numero_orden}')>"


class PA_PS_PR(Base):
    """Proveedores"""
    __tablename__ = 'pa_ps_pr'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    proveedor = Column(String(255))
    razon_social = Column(String(255))
    nit = Column(String(255))
    direccion = Column(String(255))
    telefono = Column(String(255))
    correo = Column(String(255))
    contacto = Column(String(255))
    tipo_proveedor = Column(String(255))
    activo = Column(Boolean, default=False)
    trial814 = Column(String(1))
    
    # Relaciones
    evaluaciones = relationship("PA_PS_EV", back_populates="proveedor")
    
    def __repr__(self):
        return f"<PA_PS_PR(id={self.id}, proveedor='{self.proveedor}')>"


class PA_PS_CR(Base):
    """Criterios de evaluación de proveedores"""
    __tablename__ = 'pa_ps_cr'
    __table_args__ = {'schema': 'SGApp'}
    
    id_criterio = Column(String(255), primary_key=True)
    criterio = Column(String(255))
    descripcion = Column(Text)
    trial814 = Column(String(1))
    
    # Relaciones
    detalles_evaluacion = relationship("PA_PS_DE", back_populates="criterio")
    
    def __repr__(self):
        return f"<PA_PS_CR(id_criterio='{self.id_criterio}')>"


class PA_PS_EV(Base):
    """Evaluaciones de proveedores"""
    __tablename__ = 'pa_ps_ev'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_adquisicion = Column(Integer, ForeignKey('SGApp.pa_ps_ad.id'))
    id_proveedor = Column(Integer, ForeignKey('SGApp.pa_ps_pr.id'))
    fecha_evaluacion = Column(DateTime)
    puntaje_total = Column(Float, default=0)
    calificacion = Column(String(255))
    observaciones = Column(Text)
    trial814 = Column(String(1))
    
    # Relaciones
    adquisicion = relationship("PA_PS_AD", back_populates="evaluaciones_proveedor")
    proveedor = relationship("PA_PS_PR", back_populates="evaluaciones")
    detalles = relationship("PA_PS_DE", back_populates="evaluacion")
    
    def __repr__(self):
        return f"<PA_PS_EV(id={self.id})>"


class PA_PS_DE(Base):
    """Detalles de evaluación de proveedores"""
    __tablename__ = 'pa_ps_de'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_evaluacion = Column(Integer, ForeignKey('SGApp.pa_ps_ev.id'), nullable=False)
    id_criterio = Column(String(255), ForeignKey('SGApp.pa_ps_cr.id_criterio'))
    puntaje = Column(Float, default=0)
    trial814 = Column(String(1))
    
    # Relaciones
    evaluacion = relationship("PA_PS_EV", back_populates="detalles")
    criterio = relationship("PA_PS_CR", back_populates="detalles_evaluacion")
    
    def __repr__(self):
        return f"<PA_PS_DE(id={self.id})>"


# ============================================================================
# MÓDULO: PC - Procesos de Cliente
# ============================================================================

class PC_RE_CL(Base):
    """Clientes"""
    __tablename__ = 'pc_re_cl'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    cliente = Column(String(255))
    razon_social = Column(String(255))
    nit = Column(String(255))
    direccion = Column(String(255))
    telefono = Column(String(255))
    correo = Column(String(255))
    activo = Column(Boolean, default=False)
    trial814 = Column(String(1))
    
    # Relaciones
    contactos = relationship("PC_RE_CC", back_populates="cliente")
    analisis = relationship("PC_RE_AC", back_populates="cliente_rel")
    
    def __repr__(self):
        return f"<PC_RE_CL(id={self.id}, cliente='{self.cliente}')>"


class PC_RE_CC(Base):
    """Contactos de clientes"""
    __tablename__ = 'pc_re_cc'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_cl = Column(Integer, ForeignKey('SGApp.pc_re_cl.id'))
    nombre_contacto = Column(String(255))
    cargo = Column(String(255))
    telefono = Column(String(255))
    correo = Column(String(255))
    trial814 = Column(String(1))
    
    # Relaciones
    cliente = relationship("PC_RE_CL", back_populates="contactos")
    analisis = relationship("PC_RE_AC", back_populates="contacto_rel")
    
    def __repr__(self):
        return f"<PC_RE_CC(id={self.id}, nombre='{self.nombre_contacto}')>"


class PC_RE_SG(Base):
    """Servicios Globales"""
    __tablename__ = 'pc_re_sg'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    servicio_global = Column(String(255))
    descripcion = Column(Text)
    trial814 = Column(String(1))
    
    # Relaciones
    historial = relationship("PC_RE_SH", back_populates="servicio_global_rel")
    analisis = relationship("PC_RE_AC", back_populates="servicio_global_rel")
    
    def __repr__(self):
        return f"<PC_RE_SG(id={self.id}, servicio='{self.servicio_global}')>"


class PC_RE_SE(Base):
    """Servicios"""
    __tablename__ = 'pc_re_se'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    servicio = Column(String(255))
    descripcion = Column(Text)
    codigo = Column(String(255))
    vigente = Column(Boolean, default=False)
    trial814 = Column(String(1))
    
    # Relaciones
    historial_servicio = relationship("PC_RE_SH", back_populates="servicio_rel")
    items_proforma = relationship("PC_RE_PI", back_populates="servicio_rel")
    analisis = relationship("PC_RE_AC", back_populates="servicio_rel")
    
    def __repr__(self):
        return f"<PC_RE_SE(id={self.id}, codigo='{self.codigo}')>"


class PC_RE_SH(Base):
    """Servicios en historial"""
    __tablename__ = 'pc_re_sh'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_sg = Column(Integer, ForeignKey('SGApp.pc_re_sg.id'))
    servicio = Column(Integer, ForeignKey('SGApp.pc_re_se.id'))
    trial814 = Column(String(1))
    
    # Relaciones
    servicio_global_rel = relationship("PC_RE_SG", back_populates="historial")
    servicio_rel = relationship("PC_RE_SE", back_populates="historial_servicio")
    
    def __repr__(self):
        return f"<PC_RE_SH(id={self.id})>"


class PC_RE_PR(Base):
    """Proformas"""
    __tablename__ = 'pc_re_pr'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    registrado_por = Column(String(255), ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    fecha = Column(DateTime)
    codigo_proforma = Column(String(255))
    cliente = Column(String(255))
    contacto = Column(String(255))
    monto_total = Column(Float, default=0)
    vigencia = Column(DateTime)
    estado = Column(String(255))
    observaciones = Column(Text)
    trial814 = Column(String(1))
    
    # Relaciones
    registrador = relationship("PA_PE_PE", foreign_keys=[registrado_por])
    items = relationship("PC_RE_PI", back_populates="proforma")
    analisis = relationship("PC_RE_AC", back_populates="proforma_rel")
    
    def __repr__(self):
        return f"<PC_RE_PR(id={self.id}, codigo='{self.codigo_proforma}')>"


class PC_RE_PI(Base):
    """Proforma - Items"""
    __tablename__ = 'pc_re_pi'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_pr = Column(Integer, ForeignKey('SGApp.pc_re_pr.id'))
    servicio = Column(Integer, ForeignKey('SGApp.pc_re_se.id'))
    cantidad = Column(Integer)
    precio_unitario = Column(Float, default=0)
    subtotal = Column(Float, default=0)
    trial814 = Column(String(1))
    
    # Relaciones
    proforma = relationship("PC_RE_PR", back_populates="items")
    servicio_rel = relationship("PC_RE_SE", back_populates="items_proforma")
    
    def __repr__(self):
        return f"<PC_RE_PI(id={self.id})>"


class PC_RE_AC(Base):
    """Análisis de cliente / Aceptación"""
    __tablename__ = 'pc_re_ac'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    cliente = Column(Integer, ForeignKey('SGApp.pc_re_cl.id'))
    contacto = Column(Integer, ForeignKey('SGApp.pc_re_cc.id'))
    servicio_global = Column(Integer, ForeignKey('SGApp.pc_re_sg.id'))
    servicio = Column(Integer, ForeignKey('SGApp.pc_re_se.id'))
    proforma = Column(Integer, ForeignKey('SGApp.pc_re_pr.id'))
    responsable_de_muestra = Column(String(255), ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    fecha_solicitud = Column(DateTime)
    fecha_inicio = Column(DateTime)
    fecha_finalizacion = Column(DateTime)
    estado = Column(String(255))
    observaciones = Column(Text)
    trial814 = Column(String(1))
    
    # Relaciones
    cliente_rel = relationship("PC_RE_CL", back_populates="analisis")
    contacto_rel = relationship("PC_RE_CC", back_populates="analisis")
    servicio_global_rel = relationship("PC_RE_SG", back_populates="analisis")
    servicio_rel = relationship("PC_RE_SE", back_populates="analisis")
    proforma_rel = relationship("PC_RE_PR", back_populates="analisis")
    responsable = relationship("PA_PE_PE", foreign_keys=[responsable_de_muestra])
    muestras = relationship("PC_RE_MU", back_populates="analisis_cliente")
    
    def __repr__(self):
        return f"<PC_RE_AC(id={self.id})>"


class PC_RE_MU(Base):
    """Muestras"""
    __tablename__ = 'pc_re_mu'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_ac = Column(Integer, ForeignKey('SGApp.pc_re_ac.id'))
    codigo_muestra = Column(String(255))
    descripcion = Column(Text)
    fecha_recepcion = Column(DateTime)
    estado = Column(String(255))
    trial814 = Column(String(1))
    
    # Relaciones
    analisis_cliente = relationship("PC_RE_AC", back_populates="muestras")
    
    def __repr__(self):
        return f"<PC_RE_MU(id={self.id}, codigo='{self.codigo_muestra}')>"


class PC_RE_OF(Base):
    """Ofertas"""
    __tablename__ = 'pc_re_of'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    revisado_por = Column(String(255), ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    fecha = Column(DateTime)
    codigo_oferta = Column(String(255))
    descripcion = Column(Text)
    trial814 = Column(String(1))
    
    # Relaciones
    revisor = relationship("PA_PE_PE", foreign_keys=[revisado_por])
    
    def __repr__(self):
        return f"<PC_RE_OF(id={self.id}, codigo='{self.codigo_oferta}')>"


class PC_RE_CO(Base):
    """Cotizaciones"""
    __tablename__ = 'pc_re_co'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    codigo_cotizacion = Column(String(255))
    fecha = Column(DateTime)
    cliente = Column(String(255))
    monto_total = Column(Float, default=0)
    estado = Column(String(255))
    trial814 = Column(String(1))
    
    def __repr__(self):
        return f"<PC_RE_CO(id={self.id}, codigo='{self.codigo_cotizacion}')>"


class PC_RE_SO(Base):
    """Solicitudes"""
    __tablename__ = 'pc_re_so'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    codigo_solicitud = Column(String(255))
    fecha = Column(DateTime)
    solicitante = Column(String(255))
    descripcion = Column(Text)
    estado = Column(String(255))
    trial814 = Column(String(1))
    
    def __repr__(self):
        return f"<PC_RE_SO(id={self.id}, codigo='{self.codigo_solicitud}')>"


class PC_RE_ANALISIS(Base):
    """Análisis detallado"""
    __tablename__ = 'pc_re_analisis'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha = Column(DateTime)
    codigo_analisis = Column(String(255))
    descripcion = Column(Text)
    trial814 = Column(String(1))
    
    def __repr__(self):
        return f"<PC_RE_ANALISIS(id={self.id}, codigo='{self.codigo_analisis}')>"


class PC_TC_TC(Base):
    """Trazabilidad del cliente"""
    __tablename__ = 'pc_tc_tc'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    registrado_por = Column(String(255), ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    fecha = Column(DateTime)
    codigo = Column(String(255))
    descripcion = Column(Text)
    trial814 = Column(String(1))
    
    # Relaciones
    registrador = relationship("PA_PE_PE", foreign_keys=[registrado_por])
    
    def __repr__(self):
        return f"<PC_TC_TC(id={self.id}, codigo='{self.codigo}')>"


class PC_QR_QU(Base):
    """Quejas y reclamos"""
    __tablename__ = 'pc_qr_qu'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    registrado_por = Column(String(255), ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    fecha = Column(DateTime)
    codigo_queja = Column(String(255))
    cliente = Column(String(255))
    tipo = Column(String(255))
    descripcion = Column(Text)
    estado = Column(String(255))
    resolucion = Column(Text)
    trial814 = Column(String(1))
    
    # Relaciones
    registrador = relationship("PA_PE_PE", foreign_keys=[registrado_por])
    
    def __repr__(self):
        return f"<PC_QR_QU(id={self.id}, codigo='{self.codigo_queja}')>"


class PC_ES_ES(Base):
    """Encuestas de satisfacción"""
    __tablename__ = 'pc_es_es'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    responsable = Column(String(255), ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    fecha = Column(DateTime)
    cliente = Column(String(255))
    puntaje_total = Column(Float, default=0)
    observaciones = Column(Text)
    trial814 = Column(String(1))
    
    # Relaciones
    responsable_rel = relationship("PA_PE_PE", foreign_keys=[responsable])
    
    def __repr__(self):
        return f"<PC_ES_ES(id={self.id})>"


# ============================================================================
# MÓDULO: PC_LAB - Laboratorio
# ============================================================================

class PC_LAB_PATRONES(Base):
    """Patrones de laboratorio"""
    __tablename__ = 'pc_lab_patrones'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    codigo_patron = Column(String(255))
    descripcion = Column(Text)
    concentracion = Column(String(255))
    trial814 = Column(String(1))
    
    def __repr__(self):
        return f"<PC_LAB_PATRONES(id={self.id}, codigo='{self.codigo_patron}')>"


class PC_LAB_SOLUCIONES(Base):
    """Soluciones de laboratorio"""
    __tablename__ = 'pc_lab_soluciones'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    codigo_solucion = Column(String(255))
    nombre = Column(String(255))
    concentracion = Column(String(255))
    fecha_preparacion = Column(DateTime)
    fecha_vencimiento = Column(DateTime)
    preparado_por = Column(String(255))
    trial814 = Column(String(1))
    
    # Relaciones
    detalles = relationship("PC_LAB_SOLUCIONES_DET", back_populates="solucion")
    
    def __repr__(self):
        return f"<PC_LAB_SOLUCIONES(id={self.id}, codigo='{self.codigo_solucion}')>"


class PC_LAB_SOLUCIONES_DET(Base):
    """Detalles de soluciones"""
    __tablename__ = 'pc_lab_soluciones_det'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_solucion = Column(Integer, ForeignKey('SGApp.pc_lab_soluciones.id'))
    reactivo = Column(String(255))
    cantidad = Column(Float, default=0)
    unidad = Column(String(255))
    trial814 = Column(String(1))
    
    # Relaciones
    solucion = relationship("PC_LAB_SOLUCIONES", back_populates="detalles")
    
    def __repr__(self):
        return f"<PC_LAB_SOLUCIONES_DET(id={self.id})>"


class PC_LAB_VALIDACIONMETODOS(Base):
    """Validación de métodos"""
    __tablename__ = 'pc_lab_validacionmetodos'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    codigo_metodo = Column(String(255))
    nombre_metodo = Column(String(255))
    fecha_validacion = Column(DateTime)
    responsable = Column(String(255))
    estado = Column(String(255))
    observaciones = Column(Text)
    trial814 = Column(String(1))
    
    def __repr__(self):
        return f"<PC_LAB_VALIDACIONMETODOS(id={self.id}, codigo='{self.codigo_metodo}')>"


# ============================================================================
# MÓDULO: PE - Procesos Estratégicos
# ============================================================================

class PE_PL_ES(Base):
    """Estrategias"""
    __tablename__ = 'pe_pl_es'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    registrado_por = Column(String(255), ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    fecha = Column(DateTime)
    estrategia = Column(String(255))
    descripcion = Column(Text)
    vigente = Column(Boolean, default=False)
    trial814 = Column(String(1))
    
    # Relaciones
    registrador = relationship("PA_PE_PE", foreign_keys=[registrado_por])
    objetivos = relationship("PE_PL_OB", back_populates="estrategia")
    
    def __repr__(self):
        return f"<PE_PL_ES(id={self.id}, estrategia='{self.estrategia}')>"


class PE_PL_OB(Base):
    """Objetivos"""
    __tablename__ = 'pe_pl_ob'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    registrado_por = Column(String(255), ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    estrategia_1 = Column(Integer, ForeignKey('SGApp.pe_pl_es.id'))
    fecha = Column(DateTime)
    objetivo = Column(String(255))
    descripcion = Column(Text)
    vigente = Column(Boolean, default=False)
    trial814 = Column(String(1))
    
    # Relaciones
    registrador = relationship("PA_PE_PE", foreign_keys=[registrado_por])
    estrategia = relationship("PE_PL_ES", back_populates="objetivos")
    planes = relationship("PE_PL_PL", back_populates="objetivo_rel")
    
    def __repr__(self):
        return f"<PE_PL_OB(id={self.id}, objetivo='{self.objetivo}')>"


class PE_PL_PL(Base):
    """Planes"""
    __tablename__ = 'pe_pl_pl'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    objetivo = Column(Integer, ForeignKey('SGApp.pe_pl_ob.id'))
    plan = Column(String(255))
    descripcion = Column(Text)
    fecha_inicio = Column(DateTime)
    fecha_fin = Column(DateTime)
    estado = Column(String(255))
    trial814 = Column(String(1))
    
    # Relaciones
    objetivo_rel = relationship("PE_PL_OB", back_populates="planes")
    
    def __repr__(self):
        return f"<PE_PL_PL(id={self.id}, plan='{self.plan}')>"


class PE_PL_RO(Base):
    """Riesgos y Oportunidades"""
    __tablename__ = 'pe_pl_ro'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    registrado_por = Column(String(255), ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    fecha = Column(DateTime)
    tipo = Column(String(255))
    descripcion = Column(Text)
    probabilidad = Column(String(255))
    impacto = Column(String(255))
    nivel_riesgo = Column(String(255))
    estado = Column(String(255))
    trial814 = Column(String(1))
    
    # Relaciones
    registrador = relationship("PA_PE_PE", foreign_keys=[registrado_por])
    acciones = relationship("PE_PL_AC", back_populates="riesgo_oportunidad_rel")
    planificaciones = relationship("PE_PL_PC", back_populates="riesgo_oportunidad_rel")
    
    def __repr__(self):
        return f"<PE_PL_RO(id={self.id}, tipo='{self.tipo}')>"


class PE_PL_AC(Base):
    """Acciones para riesgos y oportunidades"""
    __tablename__ = 'pe_pl_ac'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    riesgo_oportunidad = Column(Integer, ForeignKey('SGApp.pe_pl_ro.id'))
    acciones_de_mejora = Column(Integer, ForeignKey('SGApp.pe_se_me.id'))
    acciones_correctivas = Column(Integer, ForeignKey('SGApp.pe_se_ac.id'))
    correciones = Column(Integer, ForeignKey('SGApp.pe_se_ac.id'))
    accion = Column(Text)
    responsable = Column(String(255))
    fecha_planificada = Column(DateTime)
    fecha_cumplida = Column(DateTime)
    estado = Column(String(255))
    trial814 = Column(String(1))
    
    # Relaciones
    riesgo_oportunidad_rel = relationship("PE_PL_RO", back_populates="acciones")
    mejora = relationship("PE_SE_ME", foreign_keys=[acciones_de_mejora])
    accion_correctiva = relationship("PE_SE_AC", foreign_keys=[acciones_correctivas])
    correccion = relationship("PE_SE_AC", foreign_keys=[correciones])
    
    def __repr__(self):
        return f"<PE_PL_AC(id={self.id})>"


class PE_PL_PC(Base):
    """Planificación y control"""
    __tablename__ = 'pe_pl_pc'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    responsable = Column(String(255), ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    riesgo_oportunidad = Column(Integer, ForeignKey('SGApp.pe_pl_ro.id'))
    fecha = Column(DateTime)
    descripcion = Column(Text)
    trial814 = Column(String(1))
    
    # Relaciones
    responsable_rel = relationship("PA_PE_PE", foreign_keys=[responsable])
    riesgo_oportunidad_rel = relationship("PE_PL_RO", back_populates="planificaciones")
    
    def __repr__(self):
        return f"<PE_PL_PC(id={self.id})>"


class PE_PL_CO(Base):
    """Contexto de la organización"""
    __tablename__ = 'pe_pl_co'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    registrado_por = Column(String(255), ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    fecha = Column(DateTime)
    tipo = Column(String(255))
    descripcion = Column(Text)
    trial814 = Column(String(1))
    
    # Relaciones
    registrador = relationship("PA_PE_PE", foreign_keys=[registrado_por])
    
    def __repr__(self):
        return f"<PE_PL_CO(id={self.id}, tipo='{self.tipo}')>"


class PE_PL_PI(Base):
    """Partes interesadas"""
    __tablename__ = 'pe_pl_pi'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    registrado_por = Column(String(255), ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    fecha = Column(DateTime)
    parte_interesada = Column(String(255))
    necesidades_expectativas = Column(Text)
    relevancia = Column(String(255))
    trial814 = Column(String(1))
    
    # Relaciones
    registrador = relationship("PA_PE_PE", foreign_keys=[registrado_por])
    
    def __repr__(self):
        return f"<PE_PL_PI(id={self.id}, parte='{self.parte_interesada}')>"


class PE_SE_EE(Base):
    """Entradas de evaluación"""
    __tablename__ = 'pe_se_ee'
    __table_args__ = {'schema': 'SGApp'}
    
    entradas = Column(String(255), primary_key=True)
    trial814 = Column(String(1))
    
    # Relaciones
    procesos_entrada = relationship("PE_SE_EN", back_populates="entrada_rel")
    
    def __repr__(self):
        return f"<PE_SE_EE(entradas='{self.entradas}')>"


class PE_SE_SS(Base):
    """Salidas de seguimiento"""
    __tablename__ = 'pe_se_ss'
    __table_args__ = {'schema': 'SGApp'}
    
    salidas = Column(String(255), primary_key=True)
    trial814 = Column(String(1))
    
    # Relaciones
    procesos_salida = relationship("PE_SE_SA", back_populates="salida_rel")
    
    def __repr__(self):
        return f"<PE_SE_SS(salidas='{self.salidas}')>"


class PE_SE_RE(Base):
    """Recursos para evaluación"""
    __tablename__ = 'pe_se_re'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    recurso = Column(String(255))
    descripcion = Column(Text)
    tipo = Column(String(255))
    trial814 = Column(String(1))
    
    # Relaciones
    entradas = relationship("PE_SE_EN", back_populates="recurso")
    salidas = relationship("PE_SE_SA", back_populates="recurso")
    
    def __repr__(self):
        return f"<PE_SE_RE(id={self.id}, recurso='{self.recurso}')>"


class PE_SE_EN(Base):
    """Entradas de proceso"""
    __tablename__ = 'pe_se_en'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_re = Column(Integer, ForeignKey('SGApp.pe_se_re.id'), nullable=False)
    entrada = Column(String(255), ForeignKey('SGApp.pe_se_ee.entradas'))
    descripcion = Column(Text)
    trial814 = Column(String(1))
    
    # Relaciones
    recurso = relationship("PE_SE_RE", back_populates="entradas")
    entrada_rel = relationship("PE_SE_EE", back_populates="procesos_entrada")
    
    def __repr__(self):
        return f"<PE_SE_EN(id={self.id})>"


class PE_SE_SA(Base):
    """Salidas de proceso"""
    __tablename__ = 'pe_se_sa'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_re = Column(Integer, ForeignKey('SGApp.pe_se_re.id'), nullable=False)
    salida = Column(String(255), ForeignKey('SGApp.pe_se_ss.salidas'))
    descripcion = Column(Text)
    trial814 = Column(String(1))
    
    # Relaciones
    recurso = relationship("PE_SE_RE", back_populates="salidas")
    salida_rel = relationship("PE_SE_SS", back_populates="procesos_salida")
    
    def __repr__(self):
        return f"<PE_SE_SA(id={self.id})>"


class PE_SE_AC(Base):
    """Acciones correctivas"""
    __tablename__ = 'pe_se_ac'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    registrado_por = Column(String(255), ForeignKey('SGApp.pa_pe_pe.abreviatura'), nullable=False)
    fecha = Column(DateTime)
    descripcion_no_conformidad = Column(Text)
    causa_raiz = Column(Text)
    accion_correctiva = Column(Text)
    responsable = Column(String(255))
    fecha_planificada = Column(DateTime)
    fecha_implementada = Column(DateTime)
    estado = Column(String(255))
    trial814 = Column(String(1))
    
    # Relaciones
    registrador = relationship("PA_PE_PE", foreign_keys=[registrado_por])
    correcciones_detalle = relationship("PE_SE_CO", back_populates="accion_correctiva_rel")
    causas = relationship("PE_SE_CA", back_populates="accion_correctiva_rel")
    
    def __repr__(self):
        return f"<PE_SE_AC(id={self.id})>"


class PE_SE_CO(Base):
    """Correcciones"""
    __tablename__ = 'pe_se_co'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    correcciones = Column(Integer, ForeignKey('SGApp.pe_se_ac.id'))
    descripcion = Column(Text)
    fecha = Column(DateTime)
    responsable = Column(String(255))
    trial814 = Column(String(1))
    
    # Relaciones
    accion_correctiva_rel = relationship("PE_SE_AC", back_populates="correcciones_detalle")
    
    def __repr__(self):
        return f"<PE_SE_CO(id={self.id})>"


class PE_SE_CA(Base):
    """Causas de acciones correctivas"""
    __tablename__ = 'pe_se_ca'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    acciones_correctivas = Column(Integer, ForeignKey('SGApp.pe_se_ac.id'))
    causa = Column(Text)
    trial814 = Column(String(1))
    
    # Relaciones
    accion_correctiva_rel = relationship("PE_SE_AC", back_populates="causas")
    
    def __repr__(self):
        return f"<PE_SE_CA(id={self.id})>"


class PE_SE_ME(Base):
    """Mejoras"""
    __tablename__ = 'pe_se_me'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha = Column(DateTime)
    descripcion_oportunidad = Column(Text)
    accion_mejora = Column(Text)
    responsable = Column(String(255))
    fecha_planificada = Column(DateTime)
    fecha_implementada = Column(DateTime)
    estado = Column(String(255))
    trial814 = Column(String(1))
    
    # Relaciones
    mejoras_adicionales = relationship("PE_SE_MA", back_populates="mejora")
    
    def __repr__(self):
        return f"<PE_SE_ME(id={self.id})>"


class PE_SE_MA(Base):
    """Mejoras adicionales"""
    __tablename__ = 'pe_se_ma'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    acciones_de_mejora = Column(Integer, ForeignKey('SGApp.pe_se_me.id'))
    descripcion = Column(Text)
    trial814 = Column(String(1))
    
    # Relaciones
    mejora = relationship("PE_SE_ME", back_populates="mejoras_adicionales")
    
    def __repr__(self):
        return f"<PE_SE_MA(id={self.id})>"


# ============================================================================
# TABLAS AUXILIARES DEL SISTEMA
# ============================================================================

class SYS_FACTORESK(Base):
    """Factores K del sistema"""
    __tablename__ = 'sys_factoresk'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    k = Column(Float, default=0)
    n = Column(Integer)
    trial814 = Column(String(1))
    
    def __repr__(self):
        return f"<SYS_FACTORESK(id={self.id}, k={self.k}, n={self.n})>"


class TBL_LUGARES(Base):
    """Tabla de lugares"""
    __tablename__ = 'tbl_lugares'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    lugar = Column(String(255))
    descripcion = Column(Text)
    activo = Column(Boolean, default=False)
    trial814 = Column(String(1))
    
    def __repr__(self):
        return f"<TBL_LUGARES(id={self.id}, lugar='{self.lugar}')>"


class TBL_POSICIONES_HORNO(Base):
    """Posiciones del horno"""
    __tablename__ = 'tbl_posiciones_horno'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    posicion = Column(String(255))
    descripcion = Column(Text)
    trial814 = Column(String(1))
    
    def __repr__(self):
        return f"<TBL_POSICIONES_HORNO(id={self.id}, posicion='{self.posicion}')>"