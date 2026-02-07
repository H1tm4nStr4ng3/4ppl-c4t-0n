from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float, Text, ForeignKey, LargeBinary, FetchedValue
from sqlalchemy.orm import relationship, synonym
from app.core.database import Base

# ==========================================
# MÓDULO DOCUMENTACIÓN (PA_DI)
# ==========================================

class PA_DI_FA(Base):
    __tablename__ = 'pa_di_fa'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    registrado_por = Column(String, ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    fecha = Column(DateTime)
    evento = Column(String)
    resuelto = Column(Boolean, nullable=False)

    registrado_por_rel = relationship('PA_PE_PE', back_populates='pa_di_fa_items')

class PA_DI_PR(Base):
    __tablename__ = 'pa_di_pr'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    codigo_del_proceso = Column(String)
    proceso = Column(String)
    vigente = Column(Boolean, nullable=False)

    pa_di_ra_items = relationship('PA_DI_RA', back_populates='proceso_rel')

class PA_DI_RA(Base):
    __tablename__ = 'pa_di_ra'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    fecha_de_apertura = Column(DateTime)
    registrado_por = Column(String, ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    origen_de_documento = Column(String)
    tipo_de_documento = Column(String)
    proceso = Column(Integer, ForeignKey('SGApp.pa_di_pr.id'))
    codigo_de_documento_global = Column("codigo_de-documento_global", String)
    codigo_particular = Column(String)
    documento = Column(String)
    revisado_por = Column(String)
    modificaciones = Column(String)
    numerales_afectados = Column(String)
    observaciones = Column(String)
    aprobado_por = Column(String)
    version_nueva = Column(String)
    aprobado = Column(Boolean, nullable=False)
    aplica_comprobacion = Column(Boolean, nullable=False)
    comentarios_de_comprobacion = Column(String)
    comprobado = Column(Boolean, nullable=False)
    ubicacion = Column(String)
    fecha_de_cierre = Column(DateTime)

    registrado_por_rel = relationship('PA_PE_PE', back_populates='pa_di_ra_items')
    proceso_rel = relationship('PA_DI_PR', back_populates='pa_di_ra_items')

# ==========================================
# MÓDULO EQUIPAMIENTO (PA_EQ)
# ==========================================

class PA_EQ_AC(Base):
    __tablename__ = 'pa_eq_ac'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, nullable=False)
    actividad = Column(String, primary_key=True, nullable=False)
    descripcion = Column("descripción",String)
    
    pa_eq_pr_items = relationship('PA_EQ_PR', back_populates='actividad_rel')

class PA_EQ_CA(Base):
    __tablename__ = 'pa_eq_ca'
    __table_args__ = {'schema': 'SGApp'}
    id_equi = Column(Integer, nullable=False)
    registrado_por = Column(String)
    fecha = Column(DateTime)
    equipamiento = Column(String, ForeignKey('SGApp.pa_eq_eq.codigo_interno'))
    certificado = Column(String, primary_key=True, nullable=False)
    ente_calibrador = Column(String)
    fecha_de_calibracion = Column(DateTime)
    unidades = Column(String)
    observaciones = Column(String)
    apto = Column(Boolean, nullable=False)
    regla = Column(String)

    pa_eq_dc_items = relationship('PA_EQ_DC', back_populates='pa_eq_ca_rel')
    pa_eq_ex_items = relationship('PA_EQ_EX', back_populates='pa_eq_ca_rel')
    pa_eq_hm_items = relationship('PA_EQ_HM', back_populates='pa_eq_ca_rel')
    pa_eq_rp_items = relationship('PA_EQ_RP', back_populates='pa_eq_ca_rel')
    equipamiento_rel = relationship('PA_EQ_EQ', back_populates='pa_eq_ca_items')

class PA_EQ_CB(Base):
    __tablename__ = 'pa_eq_cb'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    id_ci = Column(Integer, ForeignKey('SGApp.pa_eq_ci.id_equi'))
    tipoprueba = Column(String)
    pesapatron_id = Column(String)
    posicion = Column(String)
    lectura_balanza = Column(Float)
    lectura_corregida = Column(Float)

    comprobacion_rel = relationship('PA_EQ_CI', back_populates='pa_eq_cb_items')

class PA_EQ_CH(Base):
    __tablename__ = 'pa_eq_ch'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    id_ci = Column(Integer, ForeignKey('SGApp.pa_eq_ci.id_equi'))
    posicion = Column(String)
    temppatron_leida = Column(Float)
    tempequipo_leida = Column(Float)
    diferencia = Column(Float)
    resultadopunto = Column(String)

    comprobacion_rel = relationship('PA_EQ_CI', back_populates='pa_eq_ch_items')

class PA_EQ_CI(Base):
    __tablename__ = 'pa_eq_ci'
    __table_args__ = {'schema': 'SGApp'}
    id_equi = Column(Integer, primary_key=True, nullable=False)
    registrado_por = Column(String)
    fecha = Column(DateTime)
    equipamiento = Column(String)
    balanza_utilizada = Column(String, ForeignKey('SGApp.pa_eq_eq.codigo_interno'))
    unidades = Column(String)
    observaciones = Column(String)
    promedio = Column(Float)
    desv_est = Column(Float)
    tol_sistematico = Column(Float)
    conclusion_sistematico = Column(String)
    temperatura = Column(Float)
    lugar = Column(String)
    presion_hpa = Column(Float)
    humedad_relativa = Column(Float)
    en = Column(Float)
    conclusion_en = Column(String)
    volumen_nominal = Column(Float)
    valor = Column(Float)
    incertidumbre = Column(Float)
    tipo_comprobacion = Column(String)
    tempprogramada = Column(Float)
    termometro_id = Column(String)
    cg = Column(Float)
    cgk = Column(Float)

    balanza_rel = relationship('PA_EQ_EQ', back_populates='pa_eq_ci_items')
    pa_eq_cb_items = relationship('PA_EQ_CB', back_populates='comprobacion_rel')
    pa_eq_cv_items = relationship('PA_EQ_CV', back_populates='comprobacion_rel')
    pa_eq_ch_items = relationship('PA_EQ_CH', back_populates='comprobacion_rel')

class PA_EQ_CV(Base):
    __tablename__ = 'pa_eq_cv'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    id_ci = Column(Integer, ForeignKey('SGApp.pa_eq_ci.id_equi'))
    matraz_vacio = Column(Float)
    corr1 = Column(Float)
    matraz_lleno = Column(Float)
    corr2 = Column(Float)
    masa_h2o = Column(Float)
    densidad = Column(Float)
    volumen = Column(Float)

    comprobacion_rel = relationship('PA_EQ_CI', back_populates='pa_eq_cv_items')

class PA_EQ_DC(Base):
    __tablename__ = 'pa_eq_dc'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    id_ca = Column(String, ForeignKey('SGApp.pa_eq_ca.certificado'))
    valor_nominal = Column(Float)
    referencia = Column(String)
    correccion_reportada = Column(Float)
    incertidumbre = Column(Float)
    tolerancia_de_medicion = Column(Float)
    conformidad = Column(String)
    
    pa_eq_ca_rel = relationship('PA_EQ_CA', back_populates='pa_eq_dc_items')

class PA_EQ_EQ(Base):
    __tablename__ = 'pa_eq_eq'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    # FK con cascada
    equipamiento = Column(String, ForeignKey('SGApp.pa_eq_le.lista_de_equipos', onupdate="CASCADE"))
    codigo_interno = Column(String, nullable=False, unique=True)
    marca = Column(String)
    serie = Column(String)
    material = Column(String)
    numero_de_piezas = Column(String)
    max_vn = Column(String)
    d = Column(String)
    clase_de_exactitud = Column(String)
    ubicacion = Column(String)
    comentarios = Column(String)
    puesta_en_funcionamiento = Column(DateTime)
    estado = Column(String)
    requiere = Column(String)
    frecuencia_de_calibracion = Column(String)
    frecuencia_de_mantenimiento = Column(String)
    frecuencia_de_comprobacion_intermedia = Column(String)
    frecuencia_de_calificacion = Column(String)
    version_software = Column(String)
    version_firmware = Column(String)

    lista_rel = relationship('PA_EQ_LE', back_populates='pa_eq_eq_items')
    pa_eq_ve_patron_items = relationship('PA_EQ_VE', foreign_keys='PA_EQ_VE.set_patron', back_populates='set_patron_rel')
    pa_eq_ve_comparado_items = relationship('PA_EQ_VE', foreign_keys='PA_EQ_VE.set_comparado', back_populates='set_comparado_rel')
    pa_eq_pr_items = relationship('PA_EQ_PR', back_populates='equipamiento_rel')
    pa_eq_ma_items = relationship('PA_EQ_MA', back_populates='equipamiento_rel')
    pa_eq_ca_items = relationship('PA_EQ_CA', back_populates='equipamiento_rel')
    pa_eq_ci_items = relationship('PA_EQ_CI', back_populates='balanza_rel')
    pa_ia_am_items = relationship('PA_IA_AM', back_populates='instrumento_rel')

class PA_EQ_EX(Base):
    __tablename__ = 'pa_eq_ex'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    id_ca = Column(String, ForeignKey('SGApp.pa_eq_ca.certificado'))
    carga = Column(Float)
    posicion = Column(Float)
    diferencia_reportada = Column(Float)
    tolerancia = Column(Float)
    conformidad = Column(String)
    
    pa_eq_ca_rel = relationship('PA_EQ_CA', back_populates='pa_eq_ex_items')

class PA_EQ_HM(Base):
    __tablename__ = 'pa_eq_hm'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    id_ca = Column(String, ForeignKey('SGApp.pa_eq_ca.certificado'))
    temperatura_nominal = Column(Float)
    en_el_tiempo = Column(Float)
    incertidumbre_expandida = Column(Float)
    tolerancia_en_el_tiempo = Column(Float)
    conformidad_tiempo = Column(String)
    en_el_espacio = Column(Float)
    tolerancia_en_el_espacio = Column(Float)
    conformidad_espacio = Column(String)
    
    pa_eq_ca_rel = relationship('PA_EQ_CA', back_populates='pa_eq_hm_items')

class PA_EQ_LE(Base):
    __tablename__ = 'pa_eq_le'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, nullable=False)
    lista_de_equipos = Column(String, primary_key=True, nullable=False)

    pa_eq_eq_items = relationship('PA_EQ_EQ', back_populates='lista_rel', cascade="save-update, merge")

class PA_EQ_MA(Base):
    __tablename__ = 'pa_eq_ma'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    registrado_por = Column("registrado-por", String, ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    fecha = Column(DateTime)
    equipamiento = Column(String, ForeignKey('SGApp.pa_eq_eq.codigo_interno'))
    tipo_de_mantenimiento = Column(String)
    comentarios_de_mantenimiento = Column(String)
    apto = Column(Boolean, nullable=False)

    equipamiento_rel = relationship('PA_EQ_EQ', back_populates='pa_eq_ma_items')
    registrado_por_rel = relationship('PA_PE_PE', back_populates='pa_eq_ma_items')

class PA_EQ_MO(Base):
    __tablename__ = 'pa_eq_mo'
    __table_args__ = {'schema': 'SGApp'}
    id_movimiento = Column(Integer, primary_key=True, nullable=False)
    id = synonym("id_movimiento")
    registrado_por = Column(String, ForeignKey('SGApp.pa_pe_pe.abreviatura')) 
    
    id_reactivo = Column(Integer, ForeignKey('SGApp.pa_eq_re.id_reactivo'), nullable=False)
    fecha_movimiento = Column(DateTime)
    tipo_movimiento = Column(String)
    cantidad = Column(Float)
    saldo = Column(Float)
    id_adquisicion = Column(Integer, ForeignKey('SGApp.pa_ps_ad.id'))
    observaciones = Column(String)
    
    pa_eq_re_rel = relationship('PA_EQ_RE', back_populates='pa_eq_mo_items')
    registrado_por_rel = relationship('PA_PE_PE', back_populates='pa_eq_mo_items_pe')
    adquisicion_rel = relationship('PA_PS_AD', back_populates='pa_eq_mo_items')

class PA_EQ_MR(Base):
    __tablename__ = 'pa_eq_mr'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    equipamiento = Column(String)
    codigo_interno = Column(String, nullable=False, unique=True)
    tipo = Column(String)
    certificado = Column(String)
    fecha_de_certificado = Column(DateTime)
    codigo_original = Column(String)
    productor_del_material_de_referencia = Column(String)
    procedencia = Column(String)
    serie = Column(String)
    material = Column(String)
    ubicacion = Column(String)
    comentarios = Column(String)
    fecha_de_apertura = Column(DateTime)
    fecha_de_vencimiento = Column(DateTime)
    estado = Column(String)

    pa_eq_mv_items = relationship('PA_EQ_MV', back_populates='material_referencia_rel', lazy="joined")

class PA_EQ_MV(Base):
    __tablename__ = 'pa_eq_mv'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    id_mr = Column(String, ForeignKey('SGApp.pa_eq_mr.codigo_interno'))
    parametro = Column(String)
    valor = Column(Float)
    incertidumbre = Column(Float)
    unidad = Column(String)

    material_referencia_rel = relationship('PA_EQ_MR', back_populates='pa_eq_mv_items')

class PA_EQ_PA(Base):
    __tablename__ = 'pa_eq_pa'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    gestion = Column("gestión", String)
    registrado_por = Column(String, ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    fecha = Column(DateTime)
    comentarios = Column(String)

    pa_eq_pr_items = relationship('PA_EQ_PR', back_populates='planificacion_actividad_rel')
    registrado_por_rel = relationship('PA_PE_PE', back_populates='pa_eq_pa_items')

class PA_EQ_PR(Base):
    __tablename__ = 'pa_eq_pr'
    __table_args__ = {'schema': 'SGApp'}
    id_prog = Column(Integer, primary_key=True, nullable=False)
    id_pa = Column(Integer, ForeignKey('SGApp.pa_eq_pa.id'))
    mes = Column(String)
    actividad = Column(String, ForeignKey('SGApp.pa_eq_ac.actividad'))
    equipamiento = Column(String, ForeignKey('SGApp.pa_eq_eq.codigo_interno'))
    realizado = Column(Boolean, nullable=False)
    anulado = Column(Boolean, nullable=False)
    comentarios = Column(String)

    equipamiento_rel = relationship('PA_EQ_EQ', back_populates='pa_eq_pr_items')
    actividad_rel = relationship('PA_EQ_AC', back_populates='pa_eq_pr_items')
    planificacion_actividad_rel = relationship('PA_EQ_PA', back_populates='pa_eq_pr_items')

class PA_EQ_RE(Base):
    __tablename__ = 'pa_eq_re'
    __table_args__ = {'schema': 'SGApp'}
    id_reactivo = Column(Integer, primary_key=True, nullable=False)
    id = synonym("id_reactivo")
    nombre_reactivo = Column(String)
    proveedor = Column(String)
    unidad_almacen = Column(String)
    stock_minimo = Column(Integer)
    ubicacion = Column(String)
    marca = Column(String)
    serie = Column(String)
    codigo_interno = Column(String)
    no_articulo = Column(String)
    valor = Column(Float)
    unidad = Column(String)
    grado_calidad = Column(String)
    estado = Column(String)
    fecha_de_apertura = Column(DateTime)
    fecha_de_vencimiento = Column(DateTime)
    sustancia_controlada = Column(Boolean, nullable=False)
    comentarios = Column(String)

    pa_eq_mo_items = relationship('PA_EQ_MO', back_populates='pa_eq_re_rel',lazy="joined", cascade="all, delete-orphan")

class PA_EQ_RP(Base):
    __tablename__ = 'pa_eq_rp'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    id_ca = Column(String, ForeignKey('SGApp.pa_eq_ca.certificado'))
    carga = Column(Float)
    desv_est = Column(Float)
    tolerancia = Column(Float)
    conformidad = Column(String)
    
    pa_eq_ca_rel = relationship('PA_EQ_CA', back_populates='pa_eq_rp_items')

class PA_EQ_VE(Base):
    __tablename__ = 'pa_eq_ve'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    fecha = Column(DateTime)
    set_patron = Column("set_patrón", String, ForeignKey('SGApp.pa_eq_eq.codigo_interno'))
    set_comparado = Column(String, ForeignKey('SGApp.pa_eq_eq.codigo_interno'))
    registrado_por = Column(String, ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    objeto_item_medio = Column("objeto_ítem_medio", String(255))
    
    item_1 = Column("ítem_1", String)
    res_patron_1 = Column("res_patrón_1", Float, default=0)
    u_patron_1 = Column("u_patrón_1", Float, default=0)
    res_comparado_1 = Column(Float, default=0)
    u_comparado_1 = Column(Float, default=0)
    en_1 = Column(Float)
    
    item_2 = Column("ítem_2", String)
    res_patron_2 = Column("res_patrón_2", Float, default=0)
    u_patron_2 = Column("u_patrón_2", Float, default=0)
    res_comparado_2 = Column(Float, default=0)
    u_comparado_2 = Column(Float, default=0)
    en_2 = Column(Float)

    item_3 = Column("ítem_3", String)
    res_patron_3 = Column("res_patrón_3", Float, default=0)
    u_patron_3 = Column("u_patrón_3", Float, default=0)
    res_comparado_3 = Column(Float, default=0)
    u_comparado_3 = Column(Float, default=0)
    en_3 = Column(Float)

    item_4 = Column("ítem_4", String)
    res_patron_4 = Column("res_patrón_4", Float, default=0)
    u_patron_4 = Column("u_patrón_4", Float, default=0)
    res_comparado_4 = Column(Float, default=0)
    u_comparado_4 = Column(Float, default=0)
    en_4 = Column(Float)

    item_5 = Column("ítem_5", String)
    res_patron_5 = Column("res_patrón_5", Float, default=0)
    u_patron_5 = Column("u_patrón_5", Float, default=0)
    res_comparado_5 = Column(Float, default=0)
    u_comparado_5 = Column(Float, default=0)
    en_5 = Column(Float)

    item_6 = Column("ítem_6", String)
    res_patron_6 = Column("res_patrón_6", Float, default=0)
    u_patron_6 = Column("u_patrón_6", Float, default=0)
    res_comparado_6 = Column(Float, default=0)
    u_comparado_6 = Column(Float, default=0)
    en_6 = Column(Float)

    item_7 = Column("ítem_7", String)
    res_patron_7 = Column("res_patrón_7", Float, default=0)
    u_patron_7 = Column("u_patrón_7", Float, default=0)
    res_comparado_7 = Column(Float, default=0)
    u_comparado_7 = Column(Float, default=0)
    en_7 = Column(Float)

    item_8 = Column("ítem_8", String)
    res_patron_8 = Column("res_patrón_8", Float, default=0)
    u_patron_8 = Column("u_patrón_8", Float, default=0)
    res_comparado_8 = Column(Float, default=0)
    u_comparado_8 = Column(Float, default=0)
    en_8 = Column(Float)

    item_9 = Column("ítem_9", String)
    res_patron_9 = Column("res_patrón_9", Float, default=0)
    u_patron_9 = Column("u_patrón_9", Float, default=0)
    res_comparado_9 = Column(Float, default=0)
    u_comparado_9 = Column(Float, default=0)
    en_9 = Column(Float)

    item_10 = Column("ítem_10", String)
    res_patron_10 = Column("res_patrón_10", Float, default=0)
    u_patron_10 = Column("u_patrón_10", Float, default=0)
    res_comparado_10 = Column(Float, default=0)
    u_comparado_10 = Column(Float, default=0)
    en_10 = Column(Float)

    item_11 = Column("ítem_11", String(255))
    res_patron_11 = Column("res_patrón_11", Float, default=0)
    u_patron_11 = Column("u_patrón_11", Float, default=0)
    res_comparado_11 = Column(Float, default=0)
    u_comparado_11 = Column(Float, default=0)
    en_11 = Column(Float)

    item_12 = Column("ítem_12", String(255))
    res_patron_12 = Column("res_patrón_12", Float, default=0)
    u_patron_12 = Column("u_patrón_12", Float, default=0)
    res_comparado_12 = Column(Float, default=0)
    u_comparado_12 = Column(Float, default=0)
    en_12 = Column(Float)

    item_13 = Column("ítem_13", String(255))
    res_patron_13 = Column("res_patrón_13", Float, default=0)
    u_patron_13 = Column("u_patrón_13", Float, default=0)
    res_comparado_13 = Column(Float, default=0)
    u_comparado_13 = Column(Float, default=0)
    en_13 = Column(Float)

    item_14 = Column("ítem_14", String(255))
    res_patron_14 = Column("res_patrón_14", Float, default=0)
    u_patron_14 = Column("u_patrón_14", Float, default=0)
    res_comparado_14 = Column(Float, default=0)
    u_comparado_14 = Column(Float, default=0)
    en_14 = Column(Float)

    item_15 = Column("ítem_15", String(255))
    res_patron_15 = Column("res_patrón_15", Float, default=0)
    u_patron_15 = Column("u_patrón_15", Float, default=0)
    res_comparado_15 = Column(Float, default=0)
    u_comparado_15 = Column(Float, default=0)
    en_15 = Column(Float)

    item_16 = Column("ítem_16", String(255))
    res_patron_16 = Column("res_patrón_16", Float, default=0)
    u_patron_16 = Column("u_patrón_16", Float, default=0)
    res_comparado_16 = Column(Float, default=0)
    u_comparado_16 = Column(Float, default=0)
    en_16 = Column(Float)

    item_17 = Column("ítem_17", String(255))
    res_patron_17 = Column("res_patrón_17", Float, default=0)
    u_patron_17 = Column("u_patrón_17", Float, default=0)
    res_comparado_17 = Column(Float, default=0)
    u_comparado_17 = Column(Float, default=0)
    en_17 = Column(Float)

    item_18 = Column("ítem_18", String(255))
    res_patron_18 = Column("res_patrón_18", Float, default=0)
    u_patron_18 = Column("u_patrón_18", Float, default=0)
    res_comparado_18 = Column(Float, default=0)
    u_comparado_18 = Column(Float, default=0)
    en_18 = Column(Float)

    item_19 = Column("ítem_19", String(255))
    res_patron_19 = Column("res_patrón_19", Float, default=0)
    u_patron_19 = Column("u_patrón_19", Float, default=0)
    res_comparado_19 = Column(Float, default=0)
    u_comparado_19 = Column(Float, default=0)
    en_19 = Column(Float)

    item_20 = Column("ítem_20", String(255))
    res_patron_20 = Column("res_patrón_20", Float, default=0)
    u_patron_20 = Column("u_patrón_20", Float, default=0)
    res_comparado_20 = Column(Float, default=0)
    u_comparado_20 = Column(Float, default=0)
    en_20 = Column(Float)

    item_21 = Column("ítem_21", String(255))
    res_patron_21 = Column("res_patrón_21", Float, default=0)
    u_patron_21 = Column("u_patrón_21", Float, default=0)
    res_comparado_21 = Column(Float, default=0)
    u_comparado_21 = Column(Float, default=0)
    en_21 = Column(Float)

    item_22 = Column("ítem_22", String(255))
    res_patron_22 = Column("res_patrón_22", Float, default=0)
    u_patron_22 = Column("u_patrón_22", Float, default=0)
    res_comparado_22 = Column(Float, default=0)
    u_comparado_22 = Column(Float, default=0)
    en_22 = Column(Float)

    item_23 = Column("ítem_23", String(255))
    res_patron_23 = Column("res_patrón_23", Float, default=0)
    u_patron_23 = Column("u_patrón_23", Float, default=0)
    res_comparado_23 = Column(Float, default=0)
    u_comparado_23 = Column(Float, default=0)
    en_23 = Column(Float)

    item_24 = Column("ítem_24", String(255))
    res_patron_24 = Column("res_patrón_24", Float, default=0)
    u_patron_24 = Column("u_patrón_24", Float, default=0)
    res_comparado_24 = Column(Float, default=0)
    u_comparado_24 = Column(Float, default=0)
    en_24 = Column(Float)

    item_25 = Column("ítem_25", String(255))
    res_patron_25 = Column("res_patrón_25", Float, default=0)
    u_patron_25 = Column("u_patrón_25", Float, default=0)
    res_comparado_25 = Column(Float, default=0)
    u_comparado_25 = Column(Float, default=0)
    en_25 = Column(Float)

    conclusion = Column("conclusión", String)
    observaciones = Column(String)

    set_patron_rel = relationship('PA_EQ_EQ', foreign_keys=[set_patron], back_populates='pa_eq_ve_patron_items')
    set_comparado_rel = relationship('PA_EQ_EQ', foreign_keys=[set_comparado], back_populates='pa_eq_ve_comparado_items')
    registrado_por_rel = relationship('PA_PE_PE', back_populates='pa_eq_ve_items')

# ==========================================
# MÓDULO INSTALACIONES (PA_IA)
# ==========================================

class PA_IA_AH(Base):
    __tablename__ = 'pa_ia_ah'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    id_am = Column(Integer, ForeignKey('SGApp.pa_ia_am.id'))
    registrado_por = Column(String, ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    servicio = Column(String)
    til = Column(Float)
    hil = Column(Float)
    fecha_y_hora_inicio = Column(DateTime)
    # ... campos intermedios ...
    aceptado_t = Column(String)
    aceptado_h = Column(String)
    comentario = Column(String)

    pa_ia_am_rel = relationship('PA_IA_AM', back_populates='pa_ia_ah_items')
    registrado_por_rel = relationship('PA_PE_PE', back_populates='pa_ia_ah_items_pe')

class PA_IA_AM(Base):
    __tablename__ = 'pa_ia_am'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    area = Column(Integer, ForeignKey('SGApp.pa_ia_ar.id'))
    instrumento = Column(String, ForeignKey('SGApp.pa_eq_eq.codigo_interno'))
    tmin = Column(Float)
    tmax = Column(Float)
    hmin = Column(Float)
    hmax = Column(Float)
    delta_t_max = Column(Float)
    delta_h_max = Column(Float)

    pa_ia_ah_items = relationship('PA_IA_AH', back_populates='pa_ia_am_rel')
    pa_ia_ar_rel = relationship('PA_IA_AR', back_populates='pa_ia_am_items')
    instrumento_rel = relationship('PA_EQ_EQ', back_populates='pa_ia_am_items')

class PA_IA_AR(Base):
    __tablename__ = 'pa_ia_ar'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    area = Column(String)

    pa_ia_am_items = relationship('PA_IA_AM', back_populates='pa_ia_ar_rel')

class PA_IA_CA(Base):
    __tablename__ = 'pa_ia_ca'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    registrado_por = Column(String, ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    fecha = Column(DateTime)
    instalacion_condicion_ambiental = Column(String)
    elemento = Column(String)
    descripcion_del_control = Column(String)
    control_eficaz = Column(Boolean, nullable=False)

    registrado_por_rel = relationship('PA_PE_PE', back_populates='pa_ia_ca_items')

class PA_IA_LE(Base):
    __tablename__ = 'pa_ia_le'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    id_li = Column(Integer, ForeignKey('SGApp.pa_ia_li.id'))
    area = Column(String)
    que = Column(String)
    frecuencia = Column(String)
    como = Column(String)
    # Definición de columnas del 1 al 31
    D1 = Column("01", String)
    D2 = Column("02", String)
    D3 = Column("03", String)
    D4 = Column("04", String)
    D5 = Column("05", String)
    D6 = Column("06", String)
    D7 = Column("07", String)
    D8 = Column("08", String)
    D9 = Column("09", String)
    D10 = Column("10", String)
    D11 = Column("11", String)
    D12 = Column("12", String)
    D13 = Column("13", String)
    D14 = Column("14", String)
    D15 = Column("15", String)
    D16 = Column("16", String)
    D17 = Column("17", String)
    D18 = Column("18", String)
    D19 = Column("19", String)
    D20 = Column("20", String)
    D21 = Column("21", String)
    D22 = Column("22", String)
    D23 = Column("23", String)
    D24 = Column("24", String)
    D25 = Column("25", String)
    D26 = Column("26", String)
    D27 = Column("27", String)
    D28 = Column("28", String)
    D29 = Column("29", String)
    D30 = Column("30", String)
    D31 = Column("31", String)
    # ...

    lista_rel = relationship('PA_IA_LI', back_populates='pa_ia_le_items')

class PA_IA_LI(Base):
    __tablename__ = 'pa_ia_li'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    registrado_por = Column(String, ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    ano = Column("año",String)
    mes = Column(String)
    fecha = Column(DateTime)
    comentarios = Column(String)

    pa_ia_le_items = relationship('PA_IA_LE', back_populates='lista_rel')
    registrado_por_rel = relationship('PA_PE_PE', back_populates='pa_ia_li_items')

class PA_IA_RA(Base):
    __tablename__ = 'pa_ia_ra'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    registrado_por = Column(String, ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    fecha = Column(DateTime)
    vigente = Column(Boolean, nullable=False)
    instalacion = Column(String)
    actividad_que_se_realizara = Column(String)
    comentario = Column(String)
    # item_de_ca_1 ... requisito_20
    item_de_ca_1 = Column(String(255))
    requisito_1 = Column(String(255))

    item_de_ca_2 = Column(String(255))
    requisito_2 = Column(String(255))

    item_de_ca_3 = Column("item_de_ca_3", String(255))
    requisito_3 = Column("requisito_3", String(255))

    item_de_ca_4 = Column("item_de_ca_4", String(255))
    requisito_4 = Column("requisito_4", String(255))

    item_de_ca_5 = Column("item_de_ca_5", String(255))
    requisito_5 = Column("requisito_5", String(255))

    item_de_ca_6 = Column("item_de_ca_6", String(255))
    requisito_6 = Column("requisito_6", String(255))

    item_de_ca_7 = Column("item_de_ca_7", String(255))
    requisito_7 = Column("requisito_7", String(255))

    item_de_ca_8 = Column("item_de_ca_8", String(255))
    requisito_8 = Column("requisito_8", String(255))

    item_de_ca_9 = Column("item_de_ca_9", String(255))
    requisito_9 = Column("requisito_9", String(255))

    item_de_ca_10 = Column("item_de_ca_10", String(255))
    requisito_10 = Column("requisito_10", String(255))

    item_de_ca_11 = Column("item_de_ca_11", String(255))
    requisito_11 = Column("requisito_11", String(255))

    item_de_ca_12 = Column("item_de_ca_12", String(255))
    requisito_12 = Column("requisito_12", String(255))

    item_de_ca_13 = Column("item_de_ca_13", String(255))
    requisito_13 = Column("requisito_13", String(255))

    item_de_ca_14 = Column("item_de_ca_14", String(255))
    requisito_14 = Column("requisito_14", String(255))

    item_de_ca_15 = Column("item_de_ca_15", String(255))
    requisito_15 = Column("requisito_15", String(255))

    item_de_ca_16 = Column("item_de_ca_16", String(255))
    requisito_16 = Column("requisito_16", String(255))

    item_de_ca_17 = Column("item_de_ca_17", String(255))
    requisito_17 = Column("requisito_17", String(255))

    item_de_ca_18 = Column("item_de_ca_18", String(255))
    requisito_18 = Column("requisito_18", String(255))

    item_de_ca_19 = Column("item_de_ca_19", String(255))
    requisito_19 = Column("requisito_19", String(255))

    item_de_ca_20 = Column("item_de_ca_20", String(255))
    requisito_20 = Column("requisito_20", String(255))


    registrado_por_rel = relationship('PA_PE_PE', back_populates='pa_ia_ra_items')
    pa_ia_sa_items = relationship('PA_IA_SA', back_populates='requisitos_ambientales_rel')

class PA_IA_RI(Base):
    __tablename__ = 'pa_ia_ri'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    registrado_por = Column(String, ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    fecha = Column(DateTime)
    vigente = Column(Boolean, nullable=False)
    instalacion = Column(String)
    actividad_que_se_realizara = Column(String)
    comentario = Column(String)
    
    item_de_instalacion_1 = Column("item_de_instalacion_1", String(255))
    requisito_1 = Column("requisito_1", String(255))

    item_de_instalacion_2 = Column("item_de_instalacion_2", String(255))
    requisito_2 = Column("requisito_2", String(255))

    item_de_instalacion_3 = Column("item_de_instalacion_3", String(255))
    requisito_3 = Column("requisito_3", String(255))

    item_de_instalacion_4 = Column("item_de_instalacion_4", String(255))
    requisito_4 = Column("requisito_4", String(255))

    item_de_instalacion_5 = Column("item_de_instalacion_5", String(255))
    requisito_5 = Column("requisito_5", String(255))

    item_de_instalacion_6 = Column("item_de_instalacion_6", String(255))
    requisito_6 = Column("requisito_6", String(255))

    item_de_instalacion_7 = Column("item_de_instalacion_7", String(255))
    requisito_7 = Column("requisito_7", String(255))

    item_de_instalacion_8 = Column("item_de_instalacion_8", String(255))
    requisito_8 = Column("requisito_8", String(255))

    item_de_instalacion_9 = Column("item_de_instalacion_9", String(255))
    requisito_9 = Column("requisito_9", String(255))

    item_de_instalacion_10 = Column("item_de_instalacion_10", String(255))
    requisito_10 = Column("requisito_10", String(255))

    item_de_instalacion_11 = Column("item_de_instalacion_11", String(255))
    requisito_11 = Column("requisito_11", String(255))

    item_de_instalacion_12 = Column("item_de_instalacion_12", String(255))
    requisito_12 = Column("requisito_12", String(255))

    item_de_instalacion_13 = Column("item_de_instalacion_13", String(255))
    requisito_13 = Column("requisito_13", String(255))

    item_de_instalacion_14 = Column("item_de_instalacion_14", String(255))
    requisito_14 = Column("requisito_14", String(255))

    item_de_instalacion_15 = Column("item_de_instalacion_15", String(255))
    requisito_15 = Column("requisito_15", String(255))

    item_de_instalacion_16 = Column("item_de_instalacion_16", String(255))
    requisito_16 = Column("requisito_16", String(255))

    item_de_instalacion_17 = Column("item_de_instalacion_17", String(255))
    requisito_17 = Column("requisito_17", String(255))

    item_de_instalacion_18 = Column("item_de_instalacion_18", String(255))
    requisito_18 = Column("requisito_18", String(255))

    item_de_instalacion_19 = Column("item_de_instalacion_19", String(255))
    requisito_19 = Column("requisito_19", String(255))

    item_de_instalacion_20 = Column("item_de_instalacion_20", String(255))
    requisito_20 = Column("requisito_20", String(255))

    registrado_por_rel = relationship('PA_PE_PE', back_populates='pa_ia_ri_items')
    pa_ia_si_items = relationship('PA_IA_SI', back_populates='requisitos_instalacion_rel')

class PA_IA_SA(Base):
    __tablename__ = 'pa_ia_sa'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    registrado_por = Column(String)
    fecha = Column(DateTime)
    id_requisitos_condiciones_ambientales = Column(Integer, ForeignKey('SGApp.pa_ia_ra.id'))
    comentario = Column(String)
    requiere_acciones = Column(Boolean, nullable=False)
    # evaluacion_requisito_1 ... conforme_20
    evaluacion_requisito_1 = Column("evaluacion_requisito_1", String(255))
    conforme_1 = Column("conforme_1", Boolean, default=False, nullable=False)

    evaluacion_requisito_2 = Column("evaluacion_requisito_2", String(255))
    conforme_2 = Column("conforme_2", Boolean, default=False, nullable=False)

    evaluacion_requisito_3 = Column("evaluacion_requisito_3", String(255))
    conforme_3 = Column("conforme_3", Boolean, default=False, nullable=False)

    evaluacion_requisito_4 = Column("evaluacion_requisito_4", String(255))
    conforme_4 = Column("conforme_4", Boolean, default=False, nullable=False)

    evaluacion_requisito_5 = Column("evaluacion_requisito_5", String(255))
    conforme_5 = Column("conforme_5", Boolean, default=False, nullable=False)

    evaluacion_requisito_6 = Column("evaluacion_requisito_6", String(255))
    conforme_6 = Column("conforme_6", Boolean, default=False, nullable=False)

    evaluacion_requisito_7 = Column("evaluacion_requisito_7", String(255))
    conforme_7 = Column("conforme_7", Boolean, default=False, nullable=False)

    evaluacion_requisito_8 = Column("evaluacion_requisito_8", String(255))
    conforme_8 = Column("conforme_8", Boolean, default=False, nullable=False)

    evaluacion_requisito_9 = Column("evaluacion_requisito_9", String(255))
    conforme_9 = Column("conforme_9", Boolean, default=False, nullable=False)

    evaluacion_requisito_10 = Column("evaluacion_requisito_10", String(255))
    conforme_10 = Column("conforme_10", Boolean, default=False, nullable=False)

    evaluacion_requisito_11 = Column("evaluacion_requisito_11", String(255))
    conforme_11 = Column("conforme_11", Boolean, default=False, nullable=False)

    evaluacion_requisito_12 = Column("evaluacion_requisito_12", String(255))
    conforme_12 = Column("conforme_12", Boolean, default=False, nullable=False)

    evaluacion_requisito_13 = Column("evaluacion_requisito_13", String(255))
    conforme_13 = Column("conforme_13", Boolean, default=False, nullable=False)

    evaluacion_requisito_14 = Column("evaluacion_requisito_14", String(255))
    conforme_14 = Column("conforme_14", Boolean, default=False, nullable=False)

    evaluacion_requisito_15 = Column("evaluacion_requisito_15", String(255))
    conforme_15 = Column("conforme_15", Boolean, default=False, nullable=False)

    evaluacion_requisito_16 = Column("evaluacion_requisito_16", String(255))
    conforme_16 = Column("conforme_16", Boolean, default=False, nullable=False)

    evaluacion_requisito_17 = Column("evaluacion_requisito_17", String(255))
    conforme_17 = Column("conforme_17", Boolean, default=False, nullable=False)

    evaluacion_requisito_18 = Column("evaluacion_requisito_18", String(255))
    conforme_18 = Column("conforme_18", Boolean, default=False, nullable=False)

    evaluacion_requisito_19 = Column("evaluacion_requisito_19", String(255))
    conforme_19 = Column("conforme_19", Boolean, default=False, nullable=False)

    evaluacion_requisito_20 = Column("evaluacion_requisito_20", String(255))
    conforme_20 = Column("conforme_20", Boolean, default=False, nullable=False)

    requisitos_ambientales_rel = relationship('PA_IA_RA', back_populates='pa_ia_sa_items')

class PA_IA_SI(Base):
    __tablename__ = 'pa_ia_si'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    registrado_por = Column(String, ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    fecha = Column(DateTime)
    id_requisitos_de_instalacion = Column(Integer, ForeignKey('SGApp.pa_ia_ri.id'))
    comentario = Column(String)
    requiere_acciones = Column(Boolean, nullable=False)
    # evaluacion_requisito_1 ... conforme_20

    requisitos_instalacion_rel = relationship('PA_IA_RI', back_populates='pa_ia_si_items')
    registrado_por_rel = relationship('PA_PE_PE', back_populates='pa_ia_si_items')

# ==========================================
# MÓDULO PERSONAL (PA_PE)
# ==========================================

class PA_PE_AU(Base):
    __tablename__ = 'pa_pe_au'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    autorizado_por = Column(String, ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    fecha = Column(DateTime)
    autorizado_a = Column(String, ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    cargo = Column(String, ForeignKey('SGApp.pa_pe_de.abreviacion'))
    autorizacion_a = Column(String)
    comentario = Column(String)

    autorizado_por_rel = relationship('PA_PE_PE', foreign_keys=[autorizado_por], back_populates='pa_pe_au_autorizado_items')
    autorizado_a_rel = relationship('PA_PE_PE', foreign_keys=[autorizado_a], back_populates='pa_pe_au_autorizado_a_items')
    cargo_rel = relationship('PA_PE_DE', back_populates='pa_pe_au_items')

class PA_PE_CV(Base):
    __tablename__ = 'pa_pe_cv'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    personal = Column(String, ForeignKey('SGApp.pa_pe_pe.abreviatura', onupdate="CASCADE", ondelete="CASCADE"))
    requisito_de_competencia = Column(String, ForeignKey('SGApp.pa_pe_ec.elemento_de_competencia', onupdate="CASCADE", ondelete="CASCADE"))
    carrera_curso_logro = Column(String)
    institucion = Column(String)
    fecha_inicio = Column(DateTime)
    fecha_final = Column(DateTime)
    carga_horaria = Column(Float)
    descripción = Column("descripción", String)
    respaldo = Column(String)

    personal_rel = relationship('PA_PE_PE', back_populates='pa_pe_cv_items')
    elemento_competencia_rel = relationship('PA_PE_EC', back_populates='pa_pe_cv_items')

class PA_PE_DE(Base):
    __tablename__ = 'pa_pe_de'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, server_default=FetchedValue(), nullable=False)
    cargo = Column(String)
    abreviacion = Column(String, primary_key=True, nullable=False)

    pa_pe_rq_items = relationship('PA_PE_RQ', back_populates='cargo_req_rel', cascade="all, delete-orphan")
    pa_pe_is_items = relationship('PA_PE_IS', back_populates='cargo_rel')
    pa_pe_se_items = relationship('PA_PE_SE', back_populates='cargo_rel')
    pa_pe_au_items = relationship('PA_PE_AU', back_populates='cargo_rel')
    pa_pe_sp_items = relationship('PA_PE_SP', back_populates='puesto_rel')
    pa_pe_pe_items = relationship('PA_PE_PE', back_populates='cargo_rel', cascade="all, delete-orphan")

class PA_PE_EC(Base):
    __tablename__ = 'pa_pe_ec'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, server_default=FetchedValue(), nullable=False)
    elemento_de_competencia = Column(String, primary_key=True, nullable=False)

    pa_pe_cv_items = relationship('PA_PE_CV', back_populates='elemento_competencia_rel', cascade="all, delete-orphan")

class PA_PE_EF(Base):
    __tablename__ = 'pa_pe_ef'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    id_plan = Column(Integer)
    fecha = Column(DateTime)
    # participantes ...
    participante_1 = Column("participante_1", String(255))
    participante_2 = Column("participante_2", String(255))
    participante_3 = Column("participante_3", String(255))
    participante_4 = Column("participante_4", String(255))
    participante_5 = Column("participante_5", String(255))
    participante_6 = Column("participante_6", String(255))
    participante_7 = Column("participante_7", String(255))
    participante_8 = Column("participante_8", String(255))
    participante_9 = Column("participante_9", String(255))
    participante_10 = Column("participante_10", String(255))

    comentarios_observaciones = Column(String)
    actividad_evaluacion = Column(String)
    conclusion_eficacia = Column(String)
    eficaz = Column(Boolean, nullable=False)
    cerrado = Column(Boolean, nullable=False)

class PA_PE_FG(Base):
    __tablename__ = 'pa_pe_fg'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    forma_de_generacion = Column(String)

    pa_pe_pl_items = relationship('PA_PE_PL', back_populates='forma_generacion_rel')

class PA_PE_IE(Base):
    __tablename__ = 'pa_pe_ie'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    id_is = Column(Integer, ForeignKey('SGApp.pa_pe_is.id'))
    cargo = Column(String, ForeignKey('SGApp.pa_pe_de.abreviacion'))
    item = Column(String)
    actividad = Column(String)

    induccion_rel = relationship('PA_PE_IS', back_populates='pa_pe_ie_items')

class PA_PE_IS(Base):
    __tablename__ = 'pa_pe_is'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    cargo = Column(String, ForeignKey('SGApp.pa_pe_de.abreviacion'))
    item = Column(String)
    comentarios = Column(String)

    cargo_rel = relationship('PA_PE_DE', back_populates='pa_pe_is_items')
    pa_pe_ie_items = relationship('PA_PE_IE', back_populates='induccion_rel')

class PA_PE_PE(Base):
    __tablename__ = 'pa_pe_pe'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, server_default=FetchedValue(), nullable=False)
    nombre = Column(String, nullable=False)
    abreviatura = Column(String, primary_key=True, nullable=False)
    cargo = Column(String, ForeignKey('SGApp.pa_pe_de.abreviacion', onupdate="CASCADE", ondelete="CASCADE"))
    fotografia = Column(String)
    fecha_de_nacimiento = Column(DateTime)
    direccion = Column(String)
    telefono_personal = Column(String)
    telefono_corporativo = Column(String)
    movil_personal = Column(String)
    movil_corporativo = Column(String)
    email_personal = Column(String)
    email_corporativo = Column(String)
    nacionalidad = Column(String)
    documento_de_identidad = Column(String)
    estado_civil = Column(String)
    categoria_de_licencia_de_conducir = Column(String)
    vigente = Column(Boolean, nullable=False)
    descripcion = Column(String)

    cargo_rel = relationship('PA_PE_DE', back_populates='pa_pe_pe_items')
    pa_ia_li_items = relationship('PA_IA_LI', back_populates='registrado_por_rel')
    pa_ia_ri_items = relationship('PA_IA_RI', back_populates='registrado_por_rel')
    pc_tc_tc_items = relationship('PC_TC_TC', back_populates='registrado_por_rel')
    pa_eq_ma_items = relationship('PA_EQ_MA', back_populates='registrado_por_rel')
    pa_ps_ad_items = relationship('PA_PS_AD', back_populates='registrado_por_rel')
    pa_di_ra_items = relationship('PA_DI_RA', back_populates='registrado_por_rel')
    pa_di_fa_items = relationship('PA_DI_FA', back_populates='registrado_por_rel')
    pa_eq_mo_items_pe = relationship('PA_EQ_MO', back_populates='registrado_por_rel')
    pa_ia_ah_items_pe = relationship('PA_IA_AH', back_populates='registrado_por_rel')
    pa_ia_ra_items = relationship('PA_IA_RA', back_populates='registrado_por_rel')
    pa_ia_ca_items = relationship('PA_IA_CA', back_populates='registrado_por_rel')
    pa_ia_si_items = relationship('PA_IA_SI', back_populates='registrado_por_rel')
    pa_eq_ve_items = relationship('PA_EQ_VE', back_populates='registrado_por_rel')
    pa_eq_pa_items = relationship('PA_EQ_PA', back_populates='registrado_por_rel')
    pa_pe_au_autorizado_items = relationship('PA_PE_AU', foreign_keys='PA_PE_AU.autorizado_por', back_populates='autorizado_por_rel')
    pa_pe_au_autorizado_a_items = relationship('PA_PE_AU', foreign_keys='PA_PE_AU.autorizado_a', back_populates='autorizado_a_rel')
    pa_pe_se_responsable_items = relationship('PA_PE_SE', foreign_keys='PA_PE_SE.responsable', back_populates='responsable_rel')
    pa_pe_se_personal_items = relationship('PA_PE_SE', foreign_keys='PA_PE_SE.personal', back_populates='personal_rel', cascade="all, delete-orphan")
    pa_pe_pl_asistentes_items = relationship('PA_PE_PL', foreign_keys='PA_PE_PL.asistentes', back_populates='asistentes_rel')
    pa_pe_pl_elaborado_items = relationship('PA_PE_PL', foreign_keys='PA_PE_PL.elaborado_por', back_populates='elaborado_por_rel')
    pc_re_of_items = relationship('PC_RE_OF', back_populates='revisado_por_rel')
    pc_re_pr_items = relationship('PC_RE_PR', back_populates='registrado_por_rel')
    pc_re_ac_items = relationship('PC_RE_AC', back_populates='responsable_muestra_rel')
    pc_qr_qu_items = relationship('PC_QR_QU', back_populates='registrado_por_rel')
    pc_es_es_items = relationship('PC_ES_ES', back_populates='pa_pe_pe_rel')
    pa_pe_sp_evaluadores_items = relationship('PA_PE_SP', back_populates='evaluadores_rel')
    pa_pe_rq_items = relationship('PA_PE_RQ', back_populates='responsable_rel')
    pa_pe_pr_registrado_items = relationship('PA_PE_PR', foreign_keys='PA_PE_PR.registrado_por', back_populates='registrado_por_rel')
    pa_pe_pr_dirigido_items = relationship('PA_PE_PR', foreign_keys='PA_PE_PR.dirigido_a', back_populates='dirigido_a_rel')
    pa_pe_cv_items = relationship('PA_PE_CV', back_populates='personal_rel', cascade="all, delete-orphan")
    pa_pe_su_supervisor_items = relationship('PA_PE_SU', foreign_keys='PA_PE_SU.supervisores', back_populates='supervisores_rel' )
    pa_pe_su_supervisado_items = relationship('PA_PE_SU',foreign_keys='PA_PE_SU.supervisados',back_populates='supervisados_rel')
    pe_pl_pi_items = relationship('PE_PL_PI', back_populates='registrado_por_rel')
    pe_pl_co_items = relationship('PE_PL_CO', back_populates='registrado_por_rel')
    pe_pl_es_items = relationship('PE_PL_ES', back_populates='registrado_por_rel')
    pe_pl_ob_items = relationship('PE_PL_OB', back_populates='registrado_por_rel')
    pe_pl_pc_items = relationship('PE_PL_PC', back_populates='responsable_rel')
    pe_se_ac_items = relationship('PE_SE_AC', back_populates='registrado_por_rel')
    pe_pl_ro_items = relationship('PE_PL_RO', back_populates='registrado_por_rel')

class PA_PE_PL(Base):
    __tablename__ = 'pa_pe_pl'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    item_del_programa = Column(Integer, ForeignKey('SGApp.pa_pe_pr.id', onupdate="CASCADE", ondelete="CASCADE"))
    elaborado_por = Column(String, ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    fecha_inicio = Column(DateTime)
    forma_generacion = Column(Integer, ForeignKey('SGApp.pa_pe_fg.id'))
    responsable_de_generacion_de_competencia = Column(String)
    tematica = Column(String)
    asistentes = Column(String, ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    comentarios_de_la_generacion_de_competencia = Column(String)
    evaluacion_si_aplica = Column(Float)
    conclusion = Column(String)
    respaldo1 = Column(String)
    respaldo2 = Column(String)
    respaldo3 = Column(String)
    competencia = Column("competencia adquirida",Boolean, nullable=False)
    fecha_final = Column(DateTime)

    programa_rel = relationship('PA_PE_PR', back_populates='pa_pe_pl_items')
    asistentes_rel = relationship('PA_PE_PE', foreign_keys=[asistentes], back_populates='pa_pe_pl_asistentes_items')
    elaborado_por_rel = relationship('PA_PE_PE', foreign_keys=[elaborado_por], back_populates='pa_pe_pl_elaborado_items')
    forma_generacion_rel = relationship('PA_PE_FG', back_populates='pa_pe_pl_items')

class PA_PE_PO(Base):
    __tablename__ = 'pa_pe_po'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    proceso_de_seleccion = Column(Integer, ForeignKey('SGApp.pa_pe_sp.id', onupdate="CASCADE", ondelete="CASCADE"))
    postulante = Column(String)
    educacion = Column(Float)
    formacion = Column(Float)
    experiencia = Column(Float)
    habilidades = Column(Float)
    conocimientotecnico = Column(Float)
    calificacion = Column(Float)
    resultado_cv = Column(Float)
    pasa_a_entrevista = Column(Boolean, nullable=False)
    # item_entrevista1...5
    item_entrevista1 = Column("item_entrevista1", Float, default=0)
    item_entrevista2 = Column("item_entrevista2", Float, default=0)
    item_entrevista3 = Column("item_entrevista3", Float, default=0)
    item_entrevista4 = Column("item_entrevista4", Float, default=0)
    item_entrevista5 = Column("item_entrevista5", Float, default=0)

    resultado_entrevista = Column(Float)
    seleccionado = Column(Boolean, nullable=False)

    seleccion_rel = relationship('PA_PE_SP', back_populates='pa_pe_po_items')

class PA_PE_PR(Base):
    __tablename__ = 'pa_pe_pr'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    registrado_por = Column(String, ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    dirigido_a = Column("dirigido_a", String, ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    actividad = Column(String)
    competencia_por_adquirir = Column(String)
    fecha_programada = Column(DateTime)
    comentarios = Column(String)

    registrado_por_rel = relationship('PA_PE_PE', foreign_keys=[registrado_por], back_populates='pa_pe_pr_registrado_items')
    dirigido_a_rel = relationship('PA_PE_PE', foreign_keys=[dirigido_a], back_populates='pa_pe_pr_dirigido_items')
    pa_pe_pl_items = relationship('PA_PE_PL', back_populates='programa_rel', cascade="all, delete-orphan")

class PA_PE_RQ(Base):
    __tablename__ = 'pa_pe_rq'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    fecha = Column(DateTime)
    cargo_req = Column(String, ForeignKey('SGApp.pa_pe_de.abreviacion', onupdate="CASCADE", ondelete="CASCADE"))
    responsable = Column(String, ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    # educacion1...10 etc
    educacion1 = Column(String)
    educacion2 = Column(String)
    educacion3 = Column(String)
    formacion1 = Column(String)
    formacion2 = Column(String)
    formacion3 = Column(String)
    formacion4 = Column(String)
    formacion5 = Column(String)
    formacion6 = Column(String)
    formacion7 = Column(String)
    formacion8 = Column(String)
    formacion9 = Column(String)
    formacion10 = Column(String)
    experiencia1 = Column(String)
    experiencia2 = Column(String)
    experiencia3 = Column(String)
    experiencia4 = Column(String)
    experiencia5 = Column(String)
    habilidades1 = Column(String)
    habilidades2 = Column(String)
    habilidades3 = Column(String)
    habilidades4 = Column(String)
    habilidades5 = Column(String)
    habilidades6 = Column(String)
    habilidades7 = Column(String)
    habilidades8 = Column(String)
    habilidades9 = Column(String)
    habilidades10 = Column(String)
    conocimiento1 = Column(String)
    conocimiento2 = Column(String)
    conocimiento3 = Column(String)
    conocimiento4 = Column(String)
    conocimiento5 = Column(String)
    conocimiento6 = Column(String)
    conocimiento7 = Column(String)
    conocimiento8 = Column(String)
    conocimiento9 = Column(String)
    conocimiento10 = Column(String)
    calificacion1 = Column(String)
    calificacion2 = Column(String)
    calificacion3 = Column(String)
    calificacion4 = Column(String)
    calificacion5 = Column(String)
    aprobado_vigente = Column(Boolean, nullable=False)
    comentarios = Column(String)
    # check fields bools...
    educacion1c = Column(Boolean, nullable=False)
    educacion2c = Column(Boolean, nullable=False)
    educacion3c = Column(Boolean, nullable=False)
    formacion1c = Column(Boolean, nullable=False)
    formacion2c = Column(Boolean, nullable=False)
    formacion3c = Column(Boolean, nullable=False)
    formacion4c = Column(Boolean, nullable=False)
    formacion5c = Column(Boolean, nullable=False)
    formacion6c = Column(Boolean, nullable=False)
    formacion7c = Column(Boolean, nullable=False)
    formacion8c = Column(Boolean, nullable=False)
    formacion9c = Column(Boolean, nullable=False)
    formacion10c = Column(Boolean, nullable=False)
    experiencia1c = Column(Boolean, nullable=False)
    experiencia2c = Column(Boolean, nullable=False)
    experiencia3c = Column(Boolean, nullable=False)
    experiencia4c = Column(Boolean, nullable=False)
    experiencia5c = Column(Boolean, nullable=False)
    habilidades1c = Column(Boolean, nullable=False)
    habilidades2c = Column(Boolean, nullable=False)
    habilidades3c = Column(Boolean, nullable=False)
    habilidades4c = Column(Boolean, nullable=False)
    habilidades5c = Column(Boolean, nullable=False)
    habilidades6c = Column(Boolean, nullable=False)
    habilidades7c = Column(Boolean, nullable=False)
    habilidades8c = Column(Boolean, nullable=False)
    habilidades9c = Column(Boolean, nullable=False)
    habilidades10c = Column(Boolean, nullable=False)
    conocimiento1c = Column(Boolean, nullable=False)
    conocimiento2c = Column(Boolean, nullable=False)
    conocimiento3c = Column(Boolean, nullable=False)
    conocimiento4c = Column(Boolean, nullable=False)
    conocimiento5c = Column(Boolean, nullable=False)
    conocimiento6c = Column(Boolean, nullable=False)
    conocimiento7c = Column(Boolean, nullable=False)
    conocimiento8c = Column(Boolean, nullable=False)
    conocimiento9c = Column(Boolean, nullable=False)
    conocimiento10c = Column(Boolean, nullable=False)
    calificacion1c = Column(Boolean, nullable=False)
    calificacion2c = Column(Boolean, nullable=False)
    calificacion3c = Column(Boolean, nullable=False)
    calificacion4c = Column(Boolean, nullable=False)
    calificacion5c = Column(Boolean, nullable=False)
    cargo_req_rel = relationship('PA_PE_DE', back_populates='pa_pe_rq_items')
    responsable_rel = relationship('PA_PE_PE', back_populates='pa_pe_rq_items')
    pa_pe_se_items = relationship('PA_PE_SE', back_populates='requisitos_rel', cascade="save-update, merge")

class PA_PE_SE(Base):
    __tablename__ = 'pa_pe_se'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    responsable = Column(String, ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    fecha = Column(DateTime)
    personal = Column(String, ForeignKey('SGApp.pa_pe_pe.abreviatura', ondelete="CASCADE"))
    cargo = Column(String, ForeignKey('SGApp.pa_pe_de.abreviacion'))
    # docs...
    doc1 = Column("doc1", LargeBinary)
    doc2 = Column("doc2", LargeBinary)
    doc3 = Column("doc3", LargeBinary)
    doc4 = Column("doc4", LargeBinary)
    doc5 = Column("doc5", LargeBinary)

    requisitos = Column(Integer, ForeignKey('SGApp.pa_pe_rq.id', onupdate="CASCADE"))
    # ev_educacion...
    # Educación
    ev_educacion1 = Column("ev_educacion1", String(255))
    cumple_educacion1 = Column("cumple_educacion1", Boolean, default=False, nullable=False)

    ev_educacion2 = Column("ev_educacion2", String(255))
    cumple_educacion2 = Column("cumple_educacion2", Boolean, default=False, nullable=False)

    ev_educacion3 = Column("ev_educacion3", String(255))
    cumple_educacion3 = Column("cumple_educacion3", Boolean, default=False, nullable=False)

    # Formación
    ev_formacion1 = Column("ev_formacion1", String(255))
    cumple_formacion1 = Column("cumple_formacion1", Boolean, default=False, nullable=False)

    ev_formacion2 = Column("ev_formacion2", String(255))
    cumple_formacion2 = Column("cumple_formacion2", Boolean, default=False, nullable=False)

    ev_formacion3 = Column("ev_formacion3", String(255))
    cumple_formacion3 = Column("cumple_formacion3", Boolean, default=False, nullable=False)

    ev_formacion4 = Column("ev_formacion4", String(255))
    cumple_formacion4 = Column("cumple_formacion4", Boolean, default=False, nullable=False)

    ev_formacion5 = Column("ev_formacion5", String(255))
    cumple_formacion5 = Column("cumple_formacion5", Boolean, default=False, nullable=False)

    ev_formacion6 = Column("ev_formacion6", String(255))
    cumple_formacion6 = Column("cumple_formacion6", Boolean, default=False, nullable=False)

    ev_formacion7 = Column("ev_formacion7", String(255))
    cumple_formacion7 = Column("cumple_formacion7", Boolean, default=False, nullable=False)

    ev_formacion8 = Column("ev_formacion8", String(255))
    cumple_formacion8 = Column("cumple_formacion8", Boolean, default=False, nullable=False)

    ev_formacion9 = Column("ev_formacion9", String(255))
    cumple_formacion9 = Column("cumple_formacion9", Boolean, default=False, nullable=False)

    ev_formacion10 = Column("ev_formacion10", String(255))
    cumple_formacion10 = Column("cumple_formacion10", Boolean, default=False, nullable=False)

    # Experiencia
    ev_experiencia1 = Column("ev_experiencia1", String(255))
    cumple_experiencia1 = Column("cumple_experiencia1", Boolean, default=False, nullable=False)

    ev_experiencia2 = Column("ev_experiencia2", String(255))
    cumple_experiencia2 = Column("cumple_experiencia2", Boolean, default=False, nullable=False)

    ev_experiencia3 = Column("ev_experiencia3", String(255))
    cumple_experiencia3 = Column("cumple_experiencia3", Boolean, default=False, nullable=False)

    ev_experiencia4 = Column("ev_experiencia4", String(255))
    cumple_experiencia4 = Column("cumple_experiencia4", Boolean, default=False, nullable=False)

    ev_experiencia5 = Column("ev_experiencia5", String(255))
    cumple_experiencia5 = Column("cumple_experiencia5", Boolean, default=False, nullable=False)

    # Habilidades
    ev_habilidades1 = Column("ev_habilidades1", String(255))
    cumple_habilidades1 = Column("cumple_habilidades1", Boolean, default=False, nullable=False)

    ev_habilidades2 = Column("ev_habilidades2", String(255))
    cumple_habilidades2 = Column("cumple_habilidades2", Boolean, default=False, nullable=False)

    ev_habilidades3 = Column("ev_habilidades3", String(255))
    cumple_habilidades3 = Column("cumple_habilidades3", Boolean, default=False, nullable=False)

    ev_habilidades4 = Column("ev_habilidades4", String(255))
    cumple_habilidades4 = Column("cumple_habilidades4", Boolean, default=False, nullable=False)

    ev_habilidades5 = Column("ev_habilidades5", String(255))
    cumple_habilidades5 = Column("cumple_habilidades5", Boolean, default=False, nullable=False)

    ev_habilidades6 = Column("ev_habilidades6", String(255))
    cumple_habilidades6 = Column("cumple_habilidades6", Boolean, default=False, nullable=False)

    ev_habilidades7 = Column("ev_habilidades7", String(255))
    cumple_habilidades7 = Column("cumple_habilidades7", Boolean, default=False, nullable=False)

    ev_habilidades8 = Column("ev_habilidades8", String(255))
    cumple_habilidades8 = Column("cumple_habilidades8", Boolean, default=False, nullable=False)

    ev_habilidades9 = Column("ev_habilidades9", String(255))
    cumple_habilidades9 = Column("cumple_habilidades9", Boolean, default=False, nullable=False)

    ev_habilidades10 = Column("ev_habilidades10", String(255))
    cumple_habilidades10 = Column("cumple_habilidades10", Boolean, default=False, nullable=False)

    # Conocimiento
    ev_conocimiento1 = Column("ev_conocimiento1", String(255))
    cumple_conocimiento1 = Column("cumple_conocimiento1", Boolean, default=False, nullable=False)

    ev_conocimiento2 = Column("ev_conocimiento2", String(255))
    cumple_conocimiento2 = Column("cumple_conocimiento2", Boolean, default=False, nullable=False)

    ev_conocimiento3 = Column("ev_conocimiento3", String(255))
    cumple_conocimiento3 = Column("cumple_conocimiento3", Boolean, default=False, nullable=False)

    ev_conocimiento4 = Column("ev_conocimiento4", String(255))
    cumple_conocimiento4 = Column("cumple_conocimiento4", Boolean, default=False, nullable=False)

    ev_conocimiento5 = Column("ev_conocimiento5", String(255))
    cumple_conocimiento5 = Column("cumple_conocimiento5", Boolean, default=False, nullable=False)

    ev_conocimiento6 = Column("ev_conocimiento6", String(255))
    cumple_conocimiento6 = Column("cumple_conocimiento6", Boolean, default=False, nullable=False)

    ev_conocimiento7 = Column("ev_conocimiento7", String(255))
    cumple_conocimiento7 = Column("cumple_conocimiento7", Boolean, default=False, nullable=False)

    ev_conocimiento8 = Column("ev_conocimiento8", String(255))
    cumple_conocimiento8 = Column("cumple_conocimiento8", Boolean, default=False, nullable=False)

    ev_conocimiento9 = Column("ev_conocimiento9", String(255))
    cumple_conocimiento9 = Column("cumple_conocimiento9", Boolean, default=False, nullable=False)

    ev_conocimiento10 = Column("ev_conocimiento10", String(255))
    cumple_conocimiento10 = Column("cumple_conocimiento10", Boolean, default=False, nullable=False)

    # Calificación
    ev_calificacion1 = Column("ev_calificacion1", String(255))
    cumple_calificacion1 = Column("cumple_calificacion1", Boolean, default=False, nullable=False)

    ev_calificacion2 = Column("ev_calificacion2", String(255))
    cumple_calificacion2 = Column("cumple_calificacion2", Boolean, default=False, nullable=False)

    ev_calificacion3 = Column("ev_calificacion3", String(255))
    cumple_calificacion3 = Column("cumple_calificacion3", Boolean, default=False, nullable=False)

    ev_calificacion4 = Column("ev_calificacion4", String(255))
    cumple_calificacion4 = Column("cumple_calificacion4", Boolean, default=False, nullable=False)

    ev_calificacion5 = Column("ev_calificacion5", String(255))
    cumple_calificacion5 = Column("cumple_calificacion5", Boolean, default=False, nullable=False)

    # Educación
    educacion1 = Column("educacion1", String(255))
    educacion1c = Column("educacion1c", Boolean, default=False, nullable=False)

    educacion2 = Column("educacion2", String(255))
    educacion2c = Column("educacion2c", Boolean, default=False, nullable=False)

    educacion3 = Column("educacion3", String(255))
    educacion3c = Column("educacion3c", Boolean, default=False, nullable=False)

    # Formación
    formacion1 = Column("formacion1", String(255))
    formacion1c = Column("formacion1c", Boolean, default=False, nullable=False)

    formacion2 = Column("formacion2", String(255))
    formacion2c = Column("formacion2c", Boolean, default=False, nullable=False)

    formacion3 = Column("formacion3", String(255))
    formacion3c = Column("formacion3c", Boolean, default=False, nullable=False)

    formacion4 = Column("formacion4", String(255))
    formacion4c = Column("formacion4c", Boolean, default=False, nullable=False)

    formacion5 = Column("formacion5", String(255))
    formacion5c = Column("formacion5c", Boolean, default=False, nullable=False)

    formacion6 = Column("formacion6", String(255))
    formacion6c = Column("formacion6c", Boolean, default=False, nullable=False)

    formacion7 = Column("formacion7", String(255))
    formacion7c = Column("formacion7c", Boolean, default=False, nullable=False)

    formacion8 = Column("formacion8", String(255))
    formacion8c = Column("formacion8c", Boolean, default=False, nullable=False)

    formacion9 = Column("formacion9", String(255))
    formacion9c = Column("formacion9c", Boolean, default=False, nullable=False)

    formacion10 = Column("formacion10", String(255))
    formacion10c = Column("formacion10c", Boolean, default=False, nullable=False)

    # Experiencia
    experiencia1 = Column("experiencia1", String(255))
    experiencia1c = Column("experiencia1c", Boolean, default=False, nullable=False)

    experiencia2 = Column("experiencia2", String(255))
    experiencia2c = Column("experiencia2c", Boolean, default=False, nullable=False)

    experiencia3 = Column("experiencia3", String(255))
    experiencia3c = Column("experiencia3c", Boolean, default=False, nullable=False)

    experiencia4 = Column("experiencia4", String(255))
    experiencia4c = Column("experiencia4c", Boolean, default=False, nullable=False)

    experiencia5 = Column("experiencia5", String(255))
    experiencia5c = Column("experiencia5c", Boolean, default=False, nullable=False)

    # Habilidades
    habilidades1 = Column("habilidades1", String(255))
    habilidades1c = Column("habilidades1c", Boolean, default=False, nullable=False)

    habilidades2 = Column("habilidades2", String(255))
    habilidades2c = Column("habilidades2c", Boolean, default=False, nullable=False)

    habilidades3 = Column("habilidades3", String(255))
    habilidades3c = Column("habilidades3c", Boolean, default=False, nullable=False)

    habilidades4 = Column("habilidades4", String(255))
    habilidades4c = Column("habilidades4c", Boolean, default=False, nullable=False)

    habilidades5 = Column("habilidades5", String(255))
    habilidades5c = Column("habilidades5c", Boolean, default=False, nullable=False)

    habilidades6 = Column("habilidades6", String(255))
    habilidades6c = Column("habilidades6c", Boolean, default=False, nullable=False)

    habilidades7 = Column("habilidades7", String(255))
    habilidades7c = Column("habilidades7c", Boolean, default=False, nullable=False)

    habilidades8 = Column("habilidades8", String(255))
    habilidades8c = Column("habilidades8c", Boolean, default=False, nullable=False)

    habilidades9 = Column("habilidades9", String(255))
    habilidades9c = Column("habilidades9c", Boolean, default=False, nullable=False)

    habilidades10 = Column("habilidades10", String(255))
    habilidades10c = Column("habilidades10c", Boolean, default=False, nullable=False)

    # Conocimiento
    conocimiento1 = Column("conocimiento1", String(255))
    conocimiento1c = Column("conocimiento1c", Boolean, default=False, nullable=False)

    conocimiento2 = Column("conocimiento2", String(255))
    conocimiento2c = Column("conocimiento2c", Boolean, default=False, nullable=False)

    conocimiento3 = Column("conocimiento3", String(255))
    conocimiento3c = Column("conocimiento3c", Boolean, default=False, nullable=False)

    conocimiento4 = Column("conocimiento4", String(255))
    conocimiento4c = Column("conocimiento4c", Boolean, default=False, nullable=False)

    conocimiento5 = Column("conocimiento5", String(255))
    conocimiento5c = Column("conocimiento5c", Boolean, default=False, nullable=False)

    conocimiento6 = Column("conocimiento6", String(255))
    conocimiento6c = Column("conocimiento6c", Boolean, default=False, nullable=False)

    conocimiento7 = Column("conocimiento7", String(255))
    conocimiento7c = Column("conocimiento7c", Boolean, default=False, nullable=False)

    conocimiento8 = Column("conocimiento8", String(255))
    conocimiento8c = Column("conocimiento8c", Boolean, default=False, nullable=False)

    conocimiento9 = Column("conocimiento9", String(255))
    conocimiento9c = Column("conocimiento9c", Boolean, default=False, nullable=False)

    conocimiento10 = Column("conocimiento10", String(255))
    conocimiento10c = Column("conocimiento10c", Boolean, default=False, nullable=False)

    # Calificación
    calificacion1 = Column("calificacion1", String(255))
    calificacion1c = Column("calificacion1c", Boolean, default=False, nullable=False)

    calificacion2 = Column("calificacion2", String(255))
    calificacion2c = Column("calificacion2c", Boolean, default=False, nullable=False)

    calificacion3 = Column("calificacion3", String(255))
    calificacion3c = Column("calificacion3c", Boolean, default=False, nullable=False)

    calificacion4 = Column("calificacion4", String(255))
    calificacion4c = Column("calificacion4c", Boolean, default=False, nullable=False)

    calificacion5 = Column("calificacion5", String(255))
    calificacion5c = Column("calificacion5c", Boolean, default=False, nullable=False)

    # Educación (numérica)
    educacion1n = Column("educacion1n", Integer, default=0)
    educacion2n = Column("educacion2n", Integer, default=0)
    educacion3n = Column("educacion3n", Integer, default=0)

    # Formación (numérica)
    formacion1n = Column("formacion1n", Integer, default=0)
    formacion2n = Column("formacion2n", Integer, default=0)
    formacion3n = Column("formacion3n", Integer, default=0)
    formacion4n = Column("formacion4n", Integer, default=0)
    formacion5n = Column("formacion5n", Integer, default=0)
    formacion6n = Column("formacion6n", Integer, default=0)
    formacion7n = Column("formacion7n", Integer, default=0)
    formacion8n = Column("formacion8n", Integer, default=0)
    formacion9n = Column("formacion9n", Integer, default=0)
    formacion10n = Column("formacion10n", Integer, default=0)

    # Experiencia (numérica)
    experiencia1n = Column("experiencia1n", Integer, default=0)
    experiencia2n = Column("experiencia2n", Integer, default=0)
    experiencia3n = Column("experiencia3n", Integer, default=0)
    experiencia4n = Column("experiencia4n", Integer, default=0)
    experiencia5n = Column("experiencia5n", Integer, default=0)

    # Habilidades (numérica)
    habilidades1n = Column("habilidades1n", Integer, default=0)
    habilidades2n = Column("habilidades2n", Integer, default=0)
    habilidades3n = Column("habilidades3n", Integer, default=0)
    habilidades4n = Column("habilidades4n", Integer, default=0)
    habilidades5n = Column("habilidades5n", Integer, default=0)
    habilidades6n = Column("habilidades6n", Integer, default=0)
    habilidades7n = Column("habilidades7n", Integer, default=0)
    habilidades8n = Column("habilidades8n", Integer, default=0)
    habilidades9n = Column("habilidades9n", Integer, default=0)
    habilidades10n = Column("habilidades10n", Integer, default=0)

    # Conocimiento (numérico)
    conocimiento1n = Column("conocimiento1n", Integer, default=0)
    conocimiento2n = Column("conocimiento2n", Integer, default=0)
    conocimiento3n = Column("conocimiento3n", Integer, default=0)
    conocimiento4n = Column("conocimiento4n", Integer, default=0)
    conocimiento5n = Column("conocimiento5n", Integer, default=0)
    conocimiento6n = Column("conocimiento6n", Integer, default=0)
    conocimiento7n = Column("conocimiento7n", Integer, default=0)
    conocimiento8n = Column("conocimiento8n", Integer, default=0)
    conocimiento9n = Column("conocimiento9n", Integer, default=0)
    conocimiento10n = Column("conocimiento10n", Integer, default=0)

    # Calificación (numérica)
    calificacion1n = Column("calificacion1n", Integer, default=0)
    calificacion2n = Column("calificacion2n", Integer, default=0)
    calificacion3n = Column("calificacion3n", Integer, default=0)
    calificacion4n = Column("calificacion4n", Integer, default=0)
    calificacion5n = Column("calificacion5n", Integer, default=0)

    # Promedio y escala
    promedio = Column("promedio", Float, default=0)
    escala = Column("escala", Integer, default=0)

    conclusion = Column(String)
    competencia_asegurada = Column(Boolean, nullable=False)
    
    requisitos_rel = relationship('PA_PE_RQ', back_populates='pa_pe_se_items')
    personal_rel = relationship('PA_PE_PE', foreign_keys=[personal], back_populates='pa_pe_se_personal_items')
    responsable_rel = relationship('PA_PE_PE', foreign_keys=[responsable], back_populates='pa_pe_se_responsable_items')
    cargo_rel = relationship('PA_PE_DE', back_populates='pa_pe_se_items')

class PA_PE_SP(Base):
    __tablename__ = 'pa_pe_sp'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    puesto = Column(String, ForeignKey('SGApp.pa_pe_de.abreviacion', onupdate="CASCADE"))
    fecha_inicial = Column(DateTime)
    evaluadores = Column(String, ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    # ponderaciones...

    # Ponderaciones generales
    ponderacion_educacion = Column("ponderacion_educacion", Float, default=0)
    ponderacion_formacion = Column("ponderacion_formacion", Float, default=0)
    ponderacion_habilidades = Column("ponderacion_habilidades", Float, default=0)
    ponderacion_experiencia = Column("ponderacion_experiencia", Float, default=0)
    ponderacion_conocimientotecnico = Column("ponderacion_conocimientotecnico", Float, default=0)
    ponderacion_calificacion = Column("ponderacion_calificacion", Float, default=0)
    ponderacion_minima_cv = Column("ponderacion_minima_cv", Float, default=0)

    # Conclusión del CV
    conclusion_cv = Column("conclusion_cv", Text)

    # Entrevista con ponderaciones
    item_entrevista_1 = Column("item_entrevista_1", String(255))
    ponderacion_entrevista_1 = Column("ponderacion_entrevista_1", Float, default=0)

    item_entrevista_2 = Column("item_entrevista_2", String(255))
    ponderacion_entrevista_2 = Column("ponderacion_entrevista_2", Float, default=0)

    item_entrevista_3 = Column("item_entrevista_3", String(255))
    ponderacion_entrevista_3 = Column("ponderacion_entrevista_3", Float, default=0)

    item_entrevista_4 = Column("item_entrevista_4", String(255))
    ponderacion_entrevista_4 = Column("ponderacion_entrevista_4", Float, default=0)

    item_entrevista_5 = Column("item_entrevista_5", String(255))
    ponderacion_entrevista_5 = Column("ponderacion_entrevista_5", Float, default=0)

    # Ponderación mínima entrevista
    ponderacion_minima_entrevista = Column("ponderacion_minima_entrevista", Float, default=0)

    conclusion_entrevista = Column(String)
    fecha_final = Column(DateTime)

    pa_pe_po_items = relationship('PA_PE_PO', back_populates='seleccion_rel', cascade="all, delete-orphan")
    puesto_rel = relationship('PA_PE_DE', back_populates='pa_pe_sp_items')
    evaluadores_rel = relationship('PA_PE_PE', back_populates='pa_pe_sp_evaluadores_items')

# En app/db/all_models.py

class PA_PE_SU(Base):
    __tablename__ = 'pa_pe_su'
    __table_args__ = {'schema': 'SGApp'}
    
    id = Column(Integer, primary_key=True, nullable=False)
    fecha = Column(DateTime)
    
    # 1. Supervisor (Quien evalúa)
    supervisores = Column(String, ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    
    # 2. Supervisado (A quien evalúan) - AGREGAMOS LA FK
    supervisados = Column(String, ForeignKey('SGApp.pa_pe_pe.abreviatura'))

    # Items de supervisión (1 al 10)
    item_de_supervision_1 = Column(String)
    supervision_exitosa_1 = Column(Boolean, default=False)
    item_de_supervision_2 = Column(String)
    supervision_exitosa_2 = Column(Boolean, default=False)
    item_de_supervision_3 = Column(String)
    supervision_exitosa_3 = Column(Boolean, default=False)
    item_de_supervision_4 = Column(String)
    supervision_exitosa_4 = Column(Boolean, default=False)
    item_de_supervision_5 = Column(String)
    supervision_exitosa_5 = Column(Boolean, default=False)
    item_de_supervision_6 = Column(String)
    supervision_exitosa_6 = Column(Boolean, default=False)
    item_de_supervision_7 = Column(String)
    supervision_exitosa_7 = Column(Boolean, default=False)
    item_de_supervision_8 = Column(String)
    supervision_exitosa_8 = Column(Boolean, default=False)
    item_de_supervision_9 = Column(String)
    supervision_exitosa_9 = Column(Boolean, default=False)
    item_de_supervision_10 = Column(String)
    supervision_exitosa_10 = Column(Boolean, default=False)

    comentarios = Column(String)
    
    # Campo Crítico de Alerta
    requiere_adquirir_o_aumentar_competencia = Column(Boolean, default=False)
    
    cargo = Column(String)
    item = Column(String) # Actividad realizada

    # RELACIONES EXPLÍCITAS (Para evitar error de ambigüedad)
    supervisores_rel = relationship(
        'PA_PE_PE', 
        foreign_keys=[supervisores], 
        back_populates='pa_pe_su_supervisor_items'
    )
    
    supervisados_rel = relationship(
        'PA_PE_PE', 
        foreign_keys=[supervisados], 
        back_populates='pa_pe_su_supervisado_items'
    )

class PA_PE_TP(Base):
    __tablename__ = 'pa_pe_tp'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    nombre = Column(String)
    cargo = Column(String)
    parametro_a_evaluar = Column(Integer)
    codigo_material = Column(Integer)
    valor_de_referencia = Column(Integer)
    valor_medido = Column(Integer)
    incertidumbre = Column(Integer)
    incertidumbre_muestra = Column(Integer)
    dispersión = Column("dispersión", Integer)
    z = Column(Integer)
    evaluador = Column(String)
    cargo_evaluador = Column(String)
    fecha = Column(DateTime)
    comentarios_dispersión = Column("comentarios_dispersión", String)
    # ...

# ==========================================
# MÓDULO COMPRAS (PA_PS)
# ==========================================

class PA_PS_AD(Base):
    __tablename__ = 'pa_ps_ad'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    registrado_por = Column(String, ForeignKey('SGApp.pa_pe_pe.abreviatura'), nullable=False)
    fecha = Column("fecha_recepción", DateTime)
    producto_o_servicio = Column(String, ForeignKey('SGApp.pa_ps_ps.producto_servicio'))
    proveedor_seleccionado = Column(Integer)
    precio_unitario = Column(Float)
    cantidad = Column(Float)
    # ...
    # Documentos y comunicaciones
    doc_1 = Column("doc_1", LargeBinary)
    doc_2 = Column("doc_2", LargeBinary)
    comunicacion_1 = Column("comunicacion_1", LargeBinary)
    comunicacion_2 = Column("comunicacion_2", LargeBinary)
    doc_3 = Column("doc_3", LargeBinary)
    doc_4 = Column("doc_4", LargeBinary)

    # Fecha y observaciones
    observaciones = Column("observaciones", Text)

    # Relación con requisitos
    id_requisitos_de_productos_y_servicios = Column("id_requisitos_de_productos_y_servicios", Integer)

    # Especificaciones y cumplimiento
    especificacion_1 = Column("especificacion_1", String(255))
    comentario_esp_1 = Column("comentario_esp_1", Text)
    cumple_esp_1 = Column("cumple_esp_1", Boolean, nullable=False, default=False)

    especificacion_2 = Column("especificacion_2", String(255))
    comentario_esp_2 = Column("comentario_esp_2", Text)
    cumple_esp_2 = Column("cumple_esp_2", Boolean, nullable=False, default=False)

    especificacion_3 = Column("especificacion_3", String(255))
    comentario_esp_3 = Column("comentario_esp_3", Text)
    cumple_esp_3 = Column("cumple_esp_3", Boolean, nullable=False, default=False)

    especificacion_4 = Column("especificacion_4", String(255))
    comentario_esp_4 = Column("comentario_esp_4", Text)
    cumple_esp_4 = Column("cumple_esp_4", Boolean, nullable=False, default=False)

    especificacion_5 = Column("especificacion_5", String(255))
    comentario_esp_5 = Column("comentario_esp_5", Text)
    cumple_esp_5 = Column("cumple_esp_5", Boolean, nullable=False, default=False)

    # Conclusión y reclamos
    conclusion_evaluacion = Column("conclusión_evaluación", Text)
    reclamo_observacion_proveedor = Column("reclamo_u_observación_al_proveedor", Text)
    
    recursos_requeridos_bs = Column("recursos_requeridos_bs", Float, default=0)

    id_requisitos_de_productos_y_servicios = Column(Integer, ForeignKey('SGApp.pa_ps_ps.id'), nullable=False)
    retroalimentacion_realizada = Column(Boolean, nullable=False)
    cerrado_eficazmente = Column(Boolean, nullable=False)

    pa_ps_ev_items = relationship('PA_PS_EV', back_populates='adquisicion_rel')
    pa_ps_os_items = relationship('PA_PS_OS', back_populates='adquisicion_rel', cascade="all, delete-orphan")
    requisitos_ps_rel = relationship('PA_PS_PS', foreign_keys=[id_requisitos_de_productos_y_servicios], back_populates='pa_ps_ad_items')
    producto_servicio_rel = relationship('PA_PS_PS', foreign_keys=[producto_o_servicio], back_populates='pa_ps_ad_producto_items')
    registrado_por_rel = relationship('PA_PE_PE', back_populates='pa_ps_ad_items')
    pa_eq_mo_items = relationship('PA_EQ_MO', back_populates='adquisicion_rel')

class PA_PS_CR(Base):
    __tablename__ = 'pa_ps_cr'
    __table_args__ = {'schema': 'SGApp'}
    id_criterio = Column(Integer, primary_key=True, nullable=False)
    criterio = Column(String)
    categoria = Column(String)
    ponderacion = Column(Float)

    pa_ps_de_items = relationship('PA_PS_DE', back_populates='criterio_rel')

class PA_PS_DE(Base):
    __tablename__ = 'pa_ps_de'
    __table_args__ = {'schema': 'SGApp'}
    id_detalle = Column(Integer, primary_key=True, nullable=False)
    id_evaluacion = Column(Integer, ForeignKey('SGApp.pa_ps_ev.id_evaluacion'))
    id_criterio = Column(Integer, ForeignKey('SGApp.pa_ps_cr.id_criterio'))
    puntuacion = Column(Integer)

    evaluacion_rel = relationship('PA_PS_EV', back_populates='pa_ps_de_items')
    criterio_rel = relationship('PA_PS_CR', back_populates='pa_ps_de_items')

class PA_PS_EV(Base):
    __tablename__ = 'pa_ps_ev'
    __table_args__ = {'schema': 'SGApp'}
    id_evaluacion = Column(Integer, primary_key=True, nullable=False)
    id_proveedor = Column(Integer, ForeignKey('SGApp.pa_ps_pr.id'))
    id_adquisicion = Column(Integer, ForeignKey('SGApp.pa_ps_ad.id'))
    id_productoservicio = Column(Integer)
    fecha_evaluacion = Column(DateTime)
    tipo_evaluacion = Column(String)
    puntaje_final = Column(Float)
    calificacion_final = Column(String)
    observacion_general = Column(String)

    adquisicion_rel = relationship('PA_PS_AD', back_populates='pa_ps_ev_items')
    proveedor_rel = relationship('PA_PS_PR', back_populates='pa_ps_ev_items')
    pa_ps_de_items = relationship('PA_PS_DE', back_populates='evaluacion_rel')

class PA_PS_OS(Base):
    __tablename__ = 'pa_ps_os'
    __table_args__ = {'schema': 'SGApp'}
    id_os = Column(Integer, primary_key=True, nullable=False)
    id_ad = Column(Integer, ForeignKey('SGApp.pa_ps_ad.id'), nullable=False)
    descripcion = Column(String)
    cantidad = Column(Float)
    precio_unitario = Column(Float)
    importe = Column(Float)

    adquisicion_rel = relationship('PA_PS_AD', back_populates='pa_ps_os_items')

class PA_PS_PR(Base):
    __tablename__ = 'pa_ps_pr'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, nullable=False)
    proveedor = Column(String, primary_key=True, nullable=False)
    razon_social = Column(String)
    nit = Column(String)
    # ...
    # Información de contacto
    direccion = Column("dirección", String(255))
    telefono_celular = Column("teléfono_celular", String(255))
    correo_electronico = Column("correo_electrónico", String(255))
    persona_de_contacto = Column("persona_de_contacto", String(255))
    comentario_observacion = Column("comentario_observación", String(255))

    # Documentos del proveedor
    doc_prov_1 = Column("doc_prov_1", LargeBinary)
    doc_prov_2 = Column("doc_prov_2", LargeBinary)
    doc_prov_3 = Column("doc_prov_3", LargeBinary)

    
    pa_ps_ev_items = relationship('PA_PS_EV', back_populates='proveedor_rel')

class PA_PS_PS(Base):
    __tablename__ = 'pa_ps_ps'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    producto_servicio = Column(String, nullable=False, unique=True)
    comentario = Column(String)
    # especificaciones...
    # Datos generales
    rango_valor_nominal = Column("rango_valor_nominal", String(255))
    resolucion_o_clase = Column("resolución_o_clase", String(255))
    contenedor_estuche = Column("contenedor_estuche", String(255))
    accesorios = Column("accesorios", String(255))

    # Especificaciones
    especificacion_1 = Column("especificacion_1", String(255))
    especificacion_2 = Column("especificacion_2", String(255))
    especificacion_3 = Column("especificacion_3", String(255))
    especificacion_4 = Column("especificacion_4", String(255))
    especificacion_5 = Column("especificacion_5", String(255))

    # Observaciones
    observaciones = Column("observaciones", Text)

    # Adjuntos
    adjunto1 = Column("adjunto1", LargeBinary)
    adjunto2 = Column("adjunto2", LargeBinary)
    adjunto3 = Column("adjunto3", LargeBinary)

    vigente = Column(Boolean, nullable=False)

    pa_ps_ad_items = relationship('PA_PS_AD', foreign_keys='PA_PS_AD.id_requisitos_de_productos_y_servicios', back_populates='requisitos_ps_rel')
    pa_ps_ad_producto_items = relationship('PA_PS_AD', foreign_keys='PA_PS_AD.producto_o_servicio', back_populates='producto_servicio_rel')

# ==========================================
# MÓDULO CONTROL CALIDAD Y LABORATORIO (PC)
# ==========================================

class PC_ES_ES(Base):
    __tablename__ = 'pc_es_es'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    responsable = Column(String, ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    fecha = Column(DateTime)
    ensayo = Column(String)
    # Tipo de SR
    tipo_de_sr = Column("tipo_de_sr", String(255))

    # Valores numéricos
    a = Column("a", Float, default=0)
    b = Column("b", Float, default=0)
    c = Column("c", Float, default=0)
    d = Column("d", Float, default=0)

    rr = Column("rr", Float, default=0)
    rrv = Column("rrv", Float, default=0)
    srrv = Column("srrv", Float, default=0)

    rrp3 = Column("rrp3", Float)
    rrp2 = Column("rrp2", Float)
    rrl3 = Column("rrl3", Float)
    rrl2 = Column("rrl2", Float)

    vigente = Column(Boolean, nullable=False)
    comentarios = Column(String)
    # ...
    # Datos generales
    mr = Column("mr", String(255))
    rre = Column("rre", Float, default=0)
    balanza = Column("balanza", String(255))
    termohigrometro = Column("termohigrometro", String(255))

    # Valores de temperatura y humedad inicial/final
    tli = Column("tli", Float, default=0)   # Temperatura inicial límite
    hli = Column("hli", Float, default=0)   # Humedad inicial límite
    tlf = Column("tlf", Float, default=0)   # Temperatura final límite
    hlf = Column("hlf", Float, default=0)   # Humedad final límite

    ti = Column("ti", Float, default=0)     # Temperatura inicial
    hi = Column("hi", Float, default=0)     # Humedad inicial
    tf = Column("tf", Float, default=0)     # Temperatura final
    hf = Column("hf", Float, default=0)     # Humedad final

    # Diferencias
    delta_t = Column("delta_t", Float, default=0)
    delta_h = Column("delta_h", Float, default=0)

    # Resultados de aceptación
    aceptado_t = Column("aceptado_t", String(255))
    aceptado_h = Column("aceptado_h", String(255))

    pa_pe_pe_rel = relationship('PA_PE_PE', back_populates='pc_es_es_items')

class PC_LAB_PATRONES(Base):
    __tablename__ = 'pc_lab_patrones'
    __table_args__ = {'schema': 'SGApp'}
    codigo_patron = Column(String, primary_key=True, nullable=False)
    descripcion = Column(String)
    valor_verdadero = Column(Float)
    incertidumbre = Column(Float)

class PC_LAB_SOLUCIONES(Base):
    __tablename__ = 'pc_lab_soluciones'
    __table_args__ = {'schema': 'SGApp'}
    id_solucion = Column(Integer, primary_key=True, nullable=False)
    nombre_solucion = Column(String)
    lote_interno = Column(String)
    fecha_preparacion = Column(DateTime)
    fecha_vencimiento = Column(DateTime)
    normalidad_teorica = Column(Float)
    factor_correcion = Column(Float)
    estado = Column(String)

class PC_LAB_SOLUCIONES_DET(Base):
    __tablename__ = 'pc_lab_soluciones_det'
    __table_args__ = {'schema': 'SGApp'}
    id_replica = Column(Integer, primary_key=True, nullable=False)
    id_solucion = Column(Integer)
    masa_patron = Column(Float)
    volumen_gasto = Column(Float)
    factor_calculado = Column(Float)

class PC_LAB_VALIDACIONMETODOS(Base):
    __tablename__ = 'pc_lab_validacionmetodos'
    __table_args__ = {'schema': 'SGApp'}
    id_metodo = Column(Integer, primary_key=True, nullable=False)
    nombre_metodo = Column(String)
    limite_cuantificacion = Column(Float)
    limite_deteccion = Column(Float)
    decimales_reporte = Column(Integer)
    modelo_repetibilidad = Column(String)

class PC_QR_QU(Base):
    __tablename__ = 'pc_qr_qu'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    registrado_por = Column(String, ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    fecha = Column(DateTime)
    codigo_servicio = Column(String)
    contacto = Column(String)
    # Evaluación y acciones
    evaluacion_entrevistas = Column("evaluacion_entrevistas", Text)
    acciones_a_tomar = Column("acciones_a_tomar", Text)

    # Comunicación y medios
    comunicacion_tratamiento = Column("comunicación_tratamiento", Text)
    medio_tratamiento = Column("medio_tratamiento", String(255))

    comunicacion_cierre = Column("comunicación_cierre", Text)
    medio_cierre = Column("medio_cierre", String(255))

    # Seguimiento y comunicación
    seguimiento_por = Column("seguimiento_por", String(255))
    comunicado_por = Column("comunicado_por", String(255))

    descripcion = Column("descripción", String)
    recibido_via = Column("recibido_vía", String)
    procede = Column(Boolean, nullable=False)
    queja_cerrada = Column(Boolean, nullable=False)
    queja_con_probabilidad_de_que_se_repita = Column(Boolean, nullable=False)

    registrado_por_rel = relationship('PA_PE_PE', back_populates='pc_qr_qu_items')

class PC_RE_AC(Base):
    __tablename__ = 'pc_re_ac'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    # id_ac = Column(Integer, ForeignKey('SGApp.pc_re_mu.id_ac')) # Circular dependency removed
    registrado_y_recepcionado_por = Column(String)
    fecha_de_registro = Column(DateTime)
    n_registro = Column(String)
    proforma = Column(Integer, ForeignKey('SGApp.pc_re_pr.id'))
    cliente = Column(Integer, ForeignKey('SGApp.pc_re_cl.id'))
    contacto = Column(Integer, ForeignKey('SGApp.pc_re_cc.id'))
    responsable_de_muestra = Column(String, ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    servicio_global = Column(Integer, ForeignKey('SGApp.pc_re_sg.id'))
    servicio = Column(Integer, ForeignKey('SGApp.pc_re_se.id'))
    fecha_de_recepcion = Column(DateTime)
    # ... aquí falta
    
    pc_re_mu_items = relationship('PC_RE_MU', back_populates='actividad_rel', cascade="all, delete-orphan")
    servicio_global_rel = relationship('PC_RE_SG', back_populates='pc_re_ac_items')
    contacto_rel = relationship('PC_RE_CC', back_populates='pc_re_ac_items')
    proforma_rel = relationship('PC_RE_PR', back_populates='pc_re_ac_items')
    cliente_rel = relationship('PC_RE_CL', back_populates='pc_re_ac_items')
    servicio_rel = relationship('PC_RE_SE', back_populates='pc_re_ac_items')
    responsable_muestra_rel = relationship('PA_PE_PE', back_populates='pc_re_ac_items')

class PC_RE_ANALISIS(Base):
    __tablename__ = 'pc_re_analisis'
    __table_args__ = {'schema': 'SGApp'}
    id_analisis = Column(Integer, primary_key=True, nullable=False)
    id_ac = Column(Integer)
    id_muestra = Column(Integer)
    codigo_muestra = Column(String)
    ensayo_solicitado = Column(String)
    metodo_nombre = Column(String)
    # ... aquí falta

class PC_RE_CC(Base):
    __tablename__ = 'pc_re_cc'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    id_cl = Column(Integer, ForeignKey('SGApp.pc_re_cl.id'))
    contacto = Column(String)
    celular = Column(String)
    e_mail = Column('e-mail', String)

    cliente_rel = relationship('PC_RE_CL', back_populates='pc_re_cc_items')
    pc_re_ac_items = relationship('PC_RE_AC', back_populates='contacto_rel')

class PC_RE_CL(Base):
    __tablename__ = 'pc_re_cl'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    cliente = Column(String)
    nit = Column(String)
    direccion = Column(String)
    ciudad = Column(String)
    pais = Column(String)
    telefono = Column(String)
    e_mail = Column('e-mail', String)

    pc_re_cc_items = relationship('PC_RE_CC', back_populates='cliente_rel')
    pc_re_ac_items = relationship('PC_RE_AC', back_populates='cliente_rel')

class PC_RE_CO(Base):
    __tablename__ = 'pc_re_co'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    fecha = Column(DateTime)
    revisado_por = Column(String)
    informacion_por_revisar = Column(String)
    revision = Column(String)
    informacion_revisada = Column(String)

class PC_RE_MU(Base):
    __tablename__ = 'pc_re_mu'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    id_ac = Column(Integer, ForeignKey('SGApp.pc_re_ac.id'), nullable=False)
    codigo = Column(String)
    tipo_de_muestra = Column(String)
    # ... aquí falta

    actividad_rel = relationship('PC_RE_AC', back_populates='pc_re_mu_items')

class PC_RE_OF(Base):
    __tablename__ = 'pc_re_of'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    fecha = Column(DateTime)
    revisado_por = Column(String, ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    informacion_por_revisar = Column(String)
    revision = Column(String)
    informacion_revisada = Column(String)

    revisado_por_rel = relationship('PA_PE_PE', back_populates='pc_re_of_items')

class PC_RE_PI(Base):
    __tablename__ = 'pc_re_pi'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    id_pr = Column(Integer, ForeignKey('SGApp.pc_re_pr.id'))
    tipo_de_muestra = Column(String)
    servicio = Column(Integer, ForeignKey('SGApp.pc_re_se.id'))
    metodo = Column(String)
    precio = Column(Float)
    cantidad = Column(Integer)
    precio_total = Column(Float)

    proforma_rel = relationship('PC_RE_PR', back_populates='pc_re_pi_items')
    servicio_rel = relationship('PC_RE_SE', back_populates='pc_re_pi_items')

class PC_RE_PR(Base):
    __tablename__ = 'pc_re_pr'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    area = Column(String)
    registrado_por = Column(String, ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    fecha = Column(DateTime)
    hora = Column(DateTime)
    total_a_cancelar = Column(Float)
    # ... aquí falta

    pc_re_pi_items = relationship('PC_RE_PI', back_populates='proforma_rel', cascade="all, delete-orphan")
    pc_re_ac_items = relationship('PC_RE_AC', back_populates='proforma_rel')
    registrado_por_rel = relationship('PA_PE_PE', back_populates='pc_re_pr_items')

class PC_RE_SE(Base):
    __tablename__ = 'pc_re_se'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    area = Column(String)
    servicio = Column(String)
    metodo = Column(String)
    unidades = Column(String)
    precio = Column(Float)
    comentario = Column(String)

    pc_re_sh_items = relationship('PC_RE_SH', back_populates='servicio_rel')
    pc_re_ac_items = relationship('PC_RE_AC', back_populates='servicio_rel')
    pc_re_pi_items = relationship('PC_RE_PI', back_populates='servicio_rel')

class PC_RE_SG(Base):
    __tablename__ = 'pc_re_sg'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    servicio_global = Column(String)
    area = Column(String)

    pc_re_ac_items = relationship('PC_RE_AC', back_populates='servicio_global_rel')
    pc_re_sh_items = relationship('PC_RE_SH', back_populates='servicio_global_rel')

class PC_RE_SH(Base):
    __tablename__ = 'pc_re_sh'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    id_sg = Column(Integer, ForeignKey('SGApp.pc_re_sg.id'))
    servicio = Column(Integer, ForeignKey('SGApp.pc_re_se.id'))

    servicio_global_rel = relationship('PC_RE_SG', back_populates='pc_re_sh_items')
    servicio_rel = relationship('PC_RE_SE', back_populates='pc_re_sh_items')

class PC_RE_SO(Base):
    __tablename__ = 'pc_re_so'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    fecha = Column(DateTime)
    revisado_por = Column(String)
    informacion_por_revisar = Column(String)
    revision = Column(String)
    informacion_revisada = Column(String)

class PC_TC_TC(Base):
    __tablename__ = 'pc_tc_tc'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    registrado_por = Column(String, ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    fecha = Column(DateTime)
    area_de_tnc = Column(String)
    servicio = Column(String)
    descripcion = Column(String)
    detencion = Column(Boolean, nullable=False)
    retencion_de_informes = Column(Boolean, nullable=False)
    cierre_tcnc = Column(Boolean, nullable=False)
    # ... aquí falta
    registrado_por_rel = relationship('PA_PE_PE', back_populates='pc_tc_tc_items')

# ==========================================
# MÓDULO ESTRATEGIA Y PLANIFICACIÓN (PE)
# ==========================================

class PE_PL_AC(Base):
    __tablename__ = 'pe_pl_ac'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    riesgo_oportunidad = Column(Integer, ForeignKey('SGApp.pe_pl_ro.id'))
    correciones = Column(Integer, ForeignKey('SGApp.pe_se_ac.id'))
    acciones_correctivas = Column(Integer, ForeignKey('SGApp.pe_se_ac.id'))
    acciones_de_mejora = Column(Integer, ForeignKey('SGApp.pe_se_me.id'))
    acciones_abordar = Column(String)
    realizado = Column(Boolean, nullable=False)

    mejora_rel = relationship('PE_SE_ME', back_populates='pe_pl_ac_items')
    accion_correctiva_rel = relationship('PE_SE_AC', foreign_keys=[acciones_correctivas], back_populates='pe_pl_ac_correctivas_items')
    riesgo_oportunidad_rel = relationship('PE_PL_RO', back_populates='pe_pl_ac_riesgo_items')
    correccion_rel = relationship('PE_SE_AC', foreign_keys=[correciones], back_populates='pe_pl_ac_correciones_items')

class PE_PL_CO(Base):
    __tablename__ = 'pe_pl_co'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    registrado_por = Column(String, ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    fecha = Column(DateTime)
    contexto = Column(String)
    tipo = Column(String)
    descripción = Column(String)
    vigente = Column(Boolean, nullable=False)

    registrado_por_rel = relationship('PA_PE_PE', back_populates='pe_pl_co_items')

class PE_PL_ES(Base):
    __tablename__ = 'pe_pl_es'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    registrado_por = Column(String, ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    fecha = Column(DateTime)
    contexto_interno = Column(Integer)
    contexto_externo = Column(Integer)
    estrategia = Column(String)
    vigente = Column(Boolean, nullable=False)

    registrado_por_rel = relationship('PA_PE_PE', back_populates='pe_pl_es_items')
    pe_pl_ob_items = relationship('PE_PL_OB', back_populates='estrategia_rel')

class PE_PL_OB(Base):
    __tablename__ = 'pe_pl_ob'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    estrategia_1 = Column(Integer, ForeignKey('SGApp.pe_pl_es.id'))
    estrategia_2 = Column(Integer)
    registrado_por = Column(String, ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    fecha = Column(DateTime)
    objetivo = Column(String, nullable=False)
    indicador = Column(String)
    meta = Column(String)
    vigente = Column(Boolean, nullable=False)

    estrategia_rel = relationship('PE_PL_ES', back_populates='pe_pl_ob_items')
    registrado_por_rel = relationship('PA_PE_PE', back_populates='pe_pl_ob_items')
    pe_pl_pl_items = relationship('PE_PL_PL', back_populates='objetivo_rel')

class PE_PL_PC(Base):
    __tablename__ = 'pe_pl_pc'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    responsable = Column(String, ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    fecha = Column(DateTime)
    riesgo_oportunidad = Column(Integer, ForeignKey('SGApp.pe_pl_ro.id'))
    actividad_contingecia = Column(String)
    vigente = Column(Boolean, nullable=False)
    comentario = Column(String)

    riesgo_oportunidad_rel = relationship('PE_PL_RO', back_populates='pe_pl_pc_items')
    responsable_rel = relationship('PA_PE_PE', back_populates='pe_pl_pc_items')

class PE_PL_PI(Base):
    __tablename__ = 'pe_pl_pi'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    registrado_por = Column(String, ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    fecha = Column(DateTime)
    tipo = Column(String)
    parte_interesada = Column(String)
    requisito1 = Column(String)
    vigente = Column(Boolean, nullable=False)

    registrado_por_rel = relationship('PA_PE_PE', back_populates='pe_pl_pi_items')

class PE_PL_PL(Base):
    __tablename__ = 'pe_pl_pl'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    objetivo = Column(Integer, ForeignKey('SGApp.pe_pl_ob.id'))
    actividad = Column(String)
    recursos = Column(String)
    plazo = Column(DateTime)
    cumplido = Column(Boolean, nullable=False)

    objetivo_rel = relationship('PE_PL_OB', back_populates='pe_pl_pl_items')
    pe_pl_ro_items = relationship('PE_PL_RO', back_populates='planificacion_rel')

class PE_PL_RO(Base):
    __tablename__ = 'pe_pl_ro'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    actividad_de_planificacion = Column(Integer, ForeignKey('SGApp.pe_pl_pl.id'))
    registrado_por = Column(String, ForeignKey('SGApp.pa_pe_pe.abreviatura'))
    fecha = Column(DateTime)
    evento = Column(String)
    consecuencia = Column(String)
    riesgo_oportunidad = Column(String)
    ctrl_existente = Column(String)
    probabilidad = Column(Integer)
    impacto = Column(Integer)
    valor_de_riesgo = Column(Integer)
    vigente = Column(Boolean, nullable=False)
    abordaje = Column(Boolean, nullable=False)

    planificacion_rel = relationship('PE_PL_PL', back_populates='pe_pl_ro_items')
    registrado_por_rel = relationship('PA_PE_PE', back_populates='pe_pl_ro_items')
    pe_pl_ac_riesgo_items = relationship('PE_PL_AC', back_populates='riesgo_oportunidad_rel')
    pe_pl_pc_items = relationship('PE_PL_PC', back_populates='riesgo_oportunidad_rel')

class PE_SE_AC(Base):
    __tablename__ = 'pe_se_ac'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    fecha_registro = Column(DateTime)
    registrado_por = Column(String, ForeignKey('SGApp.pa_pe_pe.abreviatura'), nullable=False)
    descripcion_de_la_no_conformidad = Column(String)
    causa = Column(String)
    eficaz = Column(Boolean, nullable=False)
    cerrado = Column(Boolean, nullable=False)

    registrado_por_rel = relationship('PA_PE_PE', back_populates='pe_se_ac_items')
    pe_se_co_items = relationship('PE_SE_CO', back_populates='accion_correctiva_rel')
    pe_pl_ac_correctivas_items = relationship('PE_PL_AC', foreign_keys='PE_PL_AC.acciones_correctivas', back_populates='accion_correctiva_rel')
    pe_pl_ac_correciones_items = relationship('PE_PL_AC', foreign_keys='PE_PL_AC.correciones', back_populates='correccion_rel')
    pe_se_ca_items = relationship('PE_SE_CA', back_populates='accion_correctiva_rel')

class PE_SE_CA(Base):
    __tablename__ = 'pe_se_ca'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    acciones_correctivas = Column(Integer, ForeignKey('SGApp.pe_se_ac.id'))
    acciones_abordar = Column(String)
    realizado = Column(Boolean, nullable=False)

    accion_correctiva_rel = relationship('PE_SE_AC', back_populates='pe_se_ca_items')

class PE_SE_CO(Base):
    __tablename__ = 'pe_se_co'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    correcciones = Column(Integer, ForeignKey('SGApp.pe_se_ac.id'))
    acciones_abordar = Column(String)
    realizado = Column(Boolean, nullable=False)

    accion_correctiva_rel = relationship('PE_SE_AC', back_populates='pe_se_co_items')

class PE_SE_EE(Base):
    __tablename__ = 'pe_se_ee'
    __table_args__ = {'schema': 'SGApp'}
    entradas = Column(String, primary_key=True)

    pe_se_en_items = relationship('PE_SE_EN', back_populates='entrada_tipo_rel')

class PE_SE_EN(Base):
    __tablename__ = 'pe_se_en'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    id_re = Column(Integer, ForeignKey('SGApp.pe_se_re.id'), nullable=False)
    entrada = Column(String, ForeignKey('SGApp.pe_se_ee.entradas'))
    fuente = Column(String)
    conveniente = Column(Boolean, nullable=False)
    adecuado = Column(Boolean, nullable=False)
    eficaz = Column(Boolean, nullable=False)

    revision_rel = relationship('PE_SE_RE', back_populates='pe_se_en_items')
    entrada_tipo_rel = relationship('PE_SE_EE', back_populates='pe_se_en_items')

class PE_SE_MA(Base):
    __tablename__ = 'pe_se_ma'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    acciones_de_mejora = Column(Integer, ForeignKey('SGApp.pe_se_me.id'))
    acciones_abordar = Column(String)
    realizado = Column(Boolean, nullable=False)

    mejora_rel = relationship('PE_SE_ME', back_populates='pe_se_ma_items')

class PE_SE_ME(Base):
    __tablename__ = 'pe_se_me'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    fecha_registro = Column(DateTime)
    registrado_por = Column(String)
    oportunidad_de_mejora = Column(String)
    oportunidad_de_mejora_seleccionada = Column(Boolean, nullable=False)
    eficaz = Column(Boolean, nullable=False)
    cerrado = Column(Boolean, nullable=False)

    pe_se_ma_items = relationship('PE_SE_MA', back_populates='mejora_rel')
    pe_pl_ac_items = relationship('PE_PL_AC', back_populates='mejora_rel')

class PE_SE_RE(Base):
    __tablename__ = 'pe_se_re'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    # participantes...
    fecha = Column(DateTime)
    medio_de_reunión = Column(String)
    tipo_de_revisión = Column(String)
    comentarios_y_observaciones = Column(String)
    
    pe_se_sa_items = relationship('PE_SE_SA', back_populates='revision_rel')
    pe_se_en_items = relationship('PE_SE_EN', back_populates='revision_rel')

class PE_SE_SA(Base):
    __tablename__ = 'pe_se_sa'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    id_re = Column(Integer, ForeignKey('SGApp.pe_se_re.id'), nullable=False)
    salida = Column(String, ForeignKey('SGApp.pe_se_ss.salidas'))
    decisión = Column(String)
    acciones = Column(String)

    revision_rel = relationship('PE_SE_RE', back_populates='pe_se_sa_items')
    salida_tipo_rel = relationship('PE_SE_SS', back_populates='pe_se_sa_items')

class PE_SE_SS(Base):
    __tablename__ = 'pe_se_ss'
    __table_args__ = {'schema': 'SGApp'}
    salidas = Column(String, primary_key=True)

    pe_se_sa_items = relationship('PE_SE_SA', back_populates='salida_tipo_rel')

class SYS_FACTORESK(Base):
    __tablename__ = 'sys_factoresk'
    __table_args__ = {'schema': 'SGApp'}
    id = Column(Integer, primary_key=True, nullable=False)
    descripcion = Column(String)
    factor = Column(Float)

class TBL_LUGARES(Base):
    __tablename__ = 'tbl_lugares'
    __table_args__ = {'schema': 'SGApp'}
    lugarid = Column(Integer, primary_key=True, nullable=False)
    ciudad = Column(String)
    departamento = Column(String)
    altitud = Column(Integer)
    presionref_hpa = Column(Integer)
    humedadref_pct = Column(Integer)
    prioridad = Column(Integer)

class TBL_POSICIONES_HORNO(Base):
    __tablename__ = 'tbl_posiciones_horno'
    __table_args__ = {'schema': 'SGApp'}
    posicionid = Column(Integer, primary_key=True, nullable=False)
    clasedeequipo = Column(String)
    nombreposicion = Column(String)