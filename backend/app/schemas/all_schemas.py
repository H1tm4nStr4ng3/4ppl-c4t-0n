from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import datetime

class PA_DI_FABase(BaseModel):
    id: Optional[int] = None
    registrado_por: Optional[str] = None
    fecha: Optional[datetime] = None
    evento: Optional[str] = None
    resuelto: Optional[bool] = None
    # trial814: Optional[str] = None

class PA_DI_FACreate(PA_DI_FABase): pass
class PA_DI_FAUpdate(PA_DI_FABase): pass
class PA_DI_FA(PA_DI_FABase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PA_DI_PRBase(BaseModel):
    codigo_del_proceso: Optional[str] = None
    proceso: Optional[str] = None
    vigente: Optional[bool] = None
    # trial814: Optional[str] = None

class PA_DI_PRCreate(PA_DI_PRBase): pass
class PA_DI_PRUpdate(PA_DI_PRBase): pass
class PA_DI_PR(PA_DI_PRBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PA_DI_RABase(BaseModel):
    fecha_de_apertura: Optional[datetime] = None
    registrado_por: Optional[str] = None
    origen_de_documento: Optional[str] = None
    tipo_de_documento: Optional[str] = None
    proceso: Optional[int] = None
    codigo_de_documento_global: Optional[str] = None
    codigo_particular: Optional[str] = None
    documento: Optional[str] = None
    revisado_por: Optional[str] = None
    modificaciones: Optional[str] = None
    numerales_afectados: Optional[str] = None
    observaciones: Optional[str] = None
    aprobado_por: Optional[str] = None
    version_nueva: Optional[str] = None
    aprobado: Optional[bool] = None
    aplica_comprobacion: Optional[bool] = None
    comentarios_de_comprobacion: Optional[str] = None
    comprobado: Optional[bool] = None
    ubicacion: Optional[str] = None
    fecha_de_cierre: Optional[datetime] = None
    # trial814: Optional[str] = None

class PA_DI_RACreate(PA_DI_RABase): pass
class PA_DI_RAUpdate(PA_DI_RABase): pass
class PA_DI_RA(PA_DI_RABase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PA_EQ_ACBase(BaseModel):
    id: Optional[int] = None
    descripci_n: Optional[str] = None
    # trial814: Optional[str] = None

class PA_EQ_ACCreate(PA_EQ_ACBase): pass
class PA_EQ_ACUpdate(PA_EQ_ACBase): pass
class PA_EQ_AC(PA_EQ_ACBase):
    actividad: str
    model_config = ConfigDict(from_attributes=True)

class PA_EQ_CABase(BaseModel):
    id_equi: Optional[int] = None
    registrado_por: Optional[str] = None
    fecha: Optional[datetime] = None
    equipamiento: Optional[str] = None
    ente_calibrador: Optional[str] = None
    fecha_de_calibracion: Optional[datetime] = None
    unidades: Optional[str] = None
    observaciones: Optional[str] = None
    apto: Optional[bool] = None
    regla: Optional[str] = None
    # trial814: Optional[str] = None

class PA_EQ_CACreate(PA_EQ_CABase): pass
class PA_EQ_CAUpdate(PA_EQ_CABase): pass
class PA_EQ_CA(PA_EQ_CABase):
    certificado: str
    model_config = ConfigDict(from_attributes=True)

class PA_EQ_CBBase(BaseModel):
    id_ci: Optional[int] = None
    tipoprueba: Optional[str] = None
    pesapatron_id: Optional[str] = None
    posicion: Optional[str] = None
    lectura_balanza: Optional[float] = None
    lectura_corregida: Optional[float] = None
    # trial814: Optional[str] = None

class PA_EQ_CBCreate(PA_EQ_CBBase): pass
class PA_EQ_CBUpdate(PA_EQ_CBBase): pass
class PA_EQ_CB(PA_EQ_CBBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PA_EQ_CHBase(BaseModel):
    id_ci: Optional[int] = None
    posicion: Optional[str] = None
    temppatron_leida: Optional[float] = None
    tempequipo_leida: Optional[float] = None
    diferencia: Optional[float] = None
    resultadopunto: Optional[str] = None
    # trial814: Optional[str] = None

class PA_EQ_CHCreate(PA_EQ_CHBase): pass
class PA_EQ_CHUpdate(PA_EQ_CHBase): pass
class PA_EQ_CH(PA_EQ_CHBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PA_EQ_CIBase(BaseModel):
    id_equi: Optional[int] = None
    registrado_por: Optional[str] = None
    fecha: Optional[datetime] = None
    equipamiento: Optional[str] = None
    balanza_utilizada: Optional[str] = None
    unidades: Optional[str] = None
    observaciones: Optional[str] = None
    promedio: Optional[float] = None
    desv_est: Optional[float] = None
    tol_sistematico: Optional[float] = None
    conclusion_sistematico: Optional[str] = None
    temperatura: Optional[float] = None
    lugar: Optional[str] = None
    presion_hpa: Optional[float] = None
    humedad_relativa: Optional[float] = None
    en: Optional[float] = None
    conclusion_en: Optional[str] = None
    volumen_nominal: Optional[float] = None
    valor: Optional[float] = None
    incertidumbre: Optional[float] = None
    tipo_comprobacion: Optional[str] = None
    tempprogramada: Optional[float] = None
    termometro_id: Optional[str] = None
    cg: Optional[float] = None
    cgk: Optional[float] = None
    # trial814: Optional[str] = None

class PA_EQ_CICreate(PA_EQ_CIBase): pass
class PA_EQ_CIUpdate(PA_EQ_CIBase): pass
class PA_EQ_CI(PA_EQ_CIBase):
    model_config = ConfigDict(from_attributes=True)

class PA_EQ_CVBase(BaseModel):
    id_ci: Optional[int] = None
    matraz_vacio: Optional[float] = None
    corr1: Optional[float] = None
    matraz_lleno: Optional[float] = None
    corr2: Optional[float] = None
    masa_h2o: Optional[float] = None
    densidad: Optional[float] = None
    volumen: Optional[float] = None
    # trial814: Optional[str] = None

class PA_EQ_CVCreate(PA_EQ_CVBase): pass
class PA_EQ_CVUpdate(PA_EQ_CVBase): pass
class PA_EQ_CV(PA_EQ_CVBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PA_EQ_DCBase(BaseModel):
    id_ca: Optional[str] = None
    valor_nominal: Optional[float] = None
    referencia: Optional[str] = None
    correccion_reportada: Optional[float] = None
    incertidumbre: Optional[float] = None
    tolerancia_de_medicion: Optional[float] = None
    conformidad: Optional[str] = None
    # trial814: Optional[str] = None

class PA_EQ_DCCreate(PA_EQ_DCBase): pass
class PA_EQ_DCUpdate(PA_EQ_DCBase): pass
class PA_EQ_DC(PA_EQ_DCBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PA_EQ_EQBase(BaseModel):
    id: Optional[int] = None
    equipamiento: Optional[str] = None
    c_digo_interno: Optional[str] = None
    marca: Optional[str] = None
    serie: Optional[str] = None
    material: Optional[str] = None
    n_mero: Optional[str] = None
    max_vn: Optional[str] = None
    d: Optional[str] = None
    clase_de_exactitud: Optional[str] = None
    ubicacion: Optional[str] = None
    comentarios: Optional[str] = None
    puesta_en_funcionamiento: Optional[datetime] = None
    estado: Optional[str] = None
    requiere: Optional[str] = None
    frecuencia_de_calibracion: Optional[str] = None
    frecuencia_de_mantenimiento: Optional[str] = None
    frecuencia_de_comprobacion_intermedia: Optional[str] = None
    frecuencia_de_calificacion: Optional[str] = None
    # trial814: Optional[str] = None

class PA_EQ_EQCreate(PA_EQ_EQBase): pass
class PA_EQ_EQUpdate(PA_EQ_EQBase): pass
class PA_EQ_EQ(PA_EQ_EQBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PA_EQ_EXBase(BaseModel):
    id_ca: Optional[str] = None
    carga: Optional[float] = None
    posicion: Optional[float] = None
    diferencia_reportada: Optional[float] = None
    tolerancia: Optional[float] = None
    conformidad: Optional[str] = None
    # trial814: Optional[str] = None

class PA_EQ_EXCreate(PA_EQ_EXBase): pass
class PA_EQ_EXUpdate(PA_EQ_EXBase): pass
class PA_EQ_EX(PA_EQ_EXBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PA_EQ_HMBase(BaseModel):
    id_ca: Optional[str] = None
    temperatura_nominal: Optional[float] = None
    en_el_tiempo: Optional[float] = None
    incertidumbre_expandida: Optional[float] = None
    tolerancia_en_el_tiempo: Optional[float] = None
    conformidad_tiempo: Optional[str] = None
    en_el_espacio: Optional[float] = None
    tolerancia_en_el_espacio: Optional[float] = None
    conformidad_espacio: Optional[str] = None
    # trial814: Optional[str] = None

class PA_EQ_HMCreate(PA_EQ_HMBase): pass
class PA_EQ_HMUpdate(PA_EQ_HMBase): pass
class PA_EQ_HM(PA_EQ_HMBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PA_EQ_LEBase(BaseModel):
    id: Optional[int] = None
    # trial814: Optional[str] = None

class PA_EQ_LECreate(PA_EQ_LEBase): pass
class PA_EQ_LEUpdate(PA_EQ_LEBase): pass
class PA_EQ_LE(PA_EQ_LEBase):
    lista_de_equipos: str
    model_config = ConfigDict(from_attributes=True)

class PA_EQ_MABase(BaseModel):
    registrado_por: Optional[str] = None
    fecha: Optional[datetime] = None
    equipamiento: Optional[str] = None
    tipo_de_mantenimiento: Optional[str] = None
    comentarios_de_mantenimiento: Optional[str] = None
    apto: Optional[bool] = None
    # trial814: Optional[str] = None

class PA_EQ_MACreate(PA_EQ_MABase): pass
class PA_EQ_MAUpdate(PA_EQ_MABase): pass
class PA_EQ_MA(PA_EQ_MABase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PA_EQ_MOBase(BaseModel):
    id_reactivo: Optional[int] = None
    fecha_movimiento: Optional[datetime] = None
    tipo_movimiento: Optional[str] = None
    cantidad: Optional[float] = None
    saldo: Optional[float] = None
    id_adquisicion: Optional[int] = None
    registrado_por: Optional[str] = None
    observaciones: Optional[str] = None
    # trial814: Optional[str] = None

class PA_EQ_MOCreate(PA_EQ_MOBase): pass
class PA_EQ_MOUpdate(PA_EQ_MOBase): pass
class PA_EQ_MO(PA_EQ_MOBase):
    id_movimiento: int
    model_config = ConfigDict(from_attributes=True)

class PA_EQ_MRBase(BaseModel):
    id: Optional[int] = None
    equipamiento: Optional[str] = None
    c_digo_interno: Optional[str] = None
    tipo: Optional[str] = None
    certificado: Optional[str] = None
    fecha_de_certificado: Optional[datetime] = None
    codigo_original: Optional[str] = None
    productor_del_material_de_referencia: Optional[str] = None
    procedencia: Optional[str] = None
    serie: Optional[str] = None
    material: Optional[str] = None
    ubicacion: Optional[str] = None
    comentarios: Optional[str] = None
    fecha_de_apertura: Optional[datetime] = None
    fecha_de_vencimiento: Optional[datetime] = None
    estado: Optional[str] = None
    # trial814: Optional[str] = None

class PA_EQ_MRCreate(PA_EQ_MRBase): pass
class PA_EQ_MRUpdate(PA_EQ_MRBase): pass
class PA_EQ_MR(PA_EQ_MRBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PA_EQ_MVBase(BaseModel):
    id_mr: Optional[str] = None
    parametro: Optional[str] = None
    valor: Optional[float] = None
    incertidumbre: Optional[float] = None
    unidad: Optional[str] = None
    # trial817: Optional[str] = None

class PA_EQ_MVCreate(PA_EQ_MVBase): pass
class PA_EQ_MVUpdate(PA_EQ_MVBase): pass
class PA_EQ_MV(PA_EQ_MVBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PA_EQ_PABase(BaseModel):
    gesti_n: Optional[str] = None
    registrado_por: Optional[str] = None
    fecha: Optional[datetime] = None
    comentarios: Optional[str] = None
    # trial817: Optional[str] = None

class PA_EQ_PACreate(PA_EQ_PABase): pass
class PA_EQ_PAUpdate(PA_EQ_PABase): pass
class PA_EQ_PA(PA_EQ_PABase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PA_EQ_PRBase(BaseModel):
    id_prog: Optional[int] = None
    id_pa: Optional[int] = None
    mes: Optional[str] = None
    actividad: Optional[str] = None
    equipamiento: Optional[str] = None
    realizado: Optional[bool] = None
    anulado: Optional[bool] = None
    comentarios: Optional[str] = None
    # trial817: Optional[str] = None

class PA_EQ_PRCreate(PA_EQ_PRBase): pass
class PA_EQ_PRUpdate(PA_EQ_PRBase): pass
class PA_EQ_PR(PA_EQ_PRBase):
    model_config = ConfigDict(from_attributes=True)

class PA_EQ_REBase(BaseModel):
    nombre_reactivo: Optional[str] = None
    proveedor: Optional[str] = None
    unidad_almacen: Optional[str] = None
    stock_minimo: Optional[int] = None
    ubicacion: Optional[str] = None
    marca: Optional[str] = None
    serie: Optional[str] = None
    codigo_interno: Optional[str] = None
    no_articulo: Optional[str] = None
    valor: Optional[float] = None
    unidad: Optional[str] = None
    grado_calidad: Optional[str] = None
    estado: Optional[str] = None
    fecha_de_apertura: Optional[datetime] = None
    fecha_de_vencimiento: Optional[datetime] = None
    sustancia_controlada: Optional[bool] = None
    comentarios: Optional[str] = None
    # trial814: Optional[str] = None

class PA_EQ_RECreate(PA_EQ_REBase): pass
class PA_EQ_REUpdate(PA_EQ_REBase): pass
class PA_EQ_RE(PA_EQ_REBase):
    id_reactivo: int
    model_config = ConfigDict(from_attributes=True)

class PA_EQ_RPBase(BaseModel):
    id_ca: Optional[str] = None
    carga: Optional[float] = None
    desv_est: Optional[float] = None
    tolerancia: Optional[float] = None
    conformidad: Optional[str] = None
    # trial817: Optional[str] = None

class PA_EQ_RPCreate(PA_EQ_RPBase): pass
class PA_EQ_RPUpdate(PA_EQ_RPBase): pass
class PA_EQ_RP(PA_EQ_RPBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PA_EQ_VEBase(BaseModel):
    id: Optional[int] = None
    fecha: Optional[datetime] = None
    registrado_por: Optional[str] = None
    set_patr_n: Optional[str] = None
    set_comparado: Optional[str] = None
    objeto__tem_medio: Optional[str] = None
    _tem_1: Optional[str] = None
    res_patr_n_1: Optional[float] = None
    u_patr_n_1: Optional[float] = None
    res_comparado_1: Optional[float] = None
    u_comparado_1: Optional[float] = None
    en_1: Optional[float] = None
    _tem_2: Optional[str] = None
    res_patr_n_2: Optional[float] = None
    u_patr_n_2: Optional[float] = None
    res_comparado_2: Optional[float] = None
    u_comparado_2: Optional[float] = None
    en_2: Optional[float] = None
    _tem_3: Optional[str] = None
    res_patr_n_3: Optional[float] = None
    u_patr_n_3: Optional[float] = None
    res_comparado_3: Optional[float] = None
    u_comparado_3: Optional[float] = None
    en_3: Optional[float] = None
    _tem_4: Optional[str] = None
    res_patr_n_4: Optional[float] = None
    u_patr_n_4: Optional[float] = None
    res_comparado_4: Optional[float] = None
    u_comparado_4: Optional[float] = None
    en_4: Optional[float] = None
    _tem_5: Optional[str] = None
    res_patr_n_5: Optional[float] = None
    u_patr_n_5: Optional[float] = None
    res_comparado_5: Optional[float] = None
    u_comparado_5: Optional[float] = None
    en_5: Optional[float] = None
    _tem_6: Optional[str] = None
    res_patr_n_6: Optional[float] = None
    u_patr_n_6: Optional[float] = None
    res_comparado_6: Optional[float] = None
    u_comparado_6: Optional[float] = None
    en_6: Optional[float] = None
    _tem_7: Optional[str] = None
    res_patr_n_7: Optional[float] = None
    u_patr_n_7: Optional[float] = None
    res_comparado_7: Optional[float] = None
    u_comparado_7: Optional[float] = None
    en_7: Optional[float] = None
    _tem_8: Optional[str] = None
    res_patr_n_8: Optional[float] = None
    u_patr_n_8: Optional[float] = None
    res_comparado_8: Optional[float] = None
    u_comparado_8: Optional[float] = None
    en_8: Optional[float] = None
    _tem_9: Optional[str] = None
    res_patr_n_9: Optional[float] = None
    u_patr_n_9: Optional[float] = None
    res_comparado_9: Optional[float] = None
    u_comparado_9: Optional[float] = None
    en_9: Optional[float] = None
    _tem_10: Optional[str] = None
    res_patr_n_10: Optional[float] = None
    u_patr_n_10: Optional[float] = None
    res_comparado_10: Optional[float] = None
    u_comparado_10: Optional[float] = None
    en_10: Optional[float] = None
    _tem_11: Optional[str] = None
    res_patr_n_11: Optional[float] = None
    u_patr_n_11: Optional[float] = None
    res_comparado_11: Optional[float] = None
    u_comparado_11: Optional[float] = None
    en_11: Optional[float] = None
    _tem_12: Optional[str] = None
    res_patr_n_12: Optional[float] = None
    u_patr_n_12: Optional[float] = None
    res_comparado_12: Optional[float] = None
    u_comparado_12: Optional[float] = None
    en_12: Optional[float] = None
    _tem_13: Optional[str] = None
    res_patr_n_13: Optional[float] = None
    u_patr_n_13: Optional[float] = None
    res_comparado_13: Optional[float] = None
    u_comparado_13: Optional[float] = None
    en_13: Optional[float] = None
    _tem_14: Optional[str] = None
    res_patr_n_14: Optional[float] = None
    u_patr_n_14: Optional[float] = None
    res_comparado_14: Optional[float] = None
    u_comparado_14: Optional[float] = None
    en_14: Optional[float] = None
    _tem_15: Optional[str] = None
    res_patr_n_15: Optional[float] = None
    u_patr_n_15: Optional[float] = None
    res_comparado_15: Optional[float] = None
    u_comparado_15: Optional[float] = None
    en_15: Optional[float] = None
    _tem_16: Optional[str] = None
    res_patr_n_16: Optional[float] = None
    u_patr_n_16: Optional[float] = None
    res_comparado_16: Optional[float] = None
    u_comparado_16: Optional[float] = None
    en_16: Optional[float] = None
    _tem_17: Optional[str] = None
    res_patr_n_17: Optional[float] = None
    u_patr_n_17: Optional[float] = None
    res_comparado_17: Optional[float] = None
    u_comparado_17: Optional[float] = None
    en_17: Optional[float] = None
    _tem_18: Optional[str] = None
    res_patr_n_18: Optional[float] = None
    u_patr_n_18: Optional[float] = None
    res_comparado_18: Optional[float] = None
    u_comparado_18: Optional[float] = None
    en_18: Optional[float] = None
    _tem_19: Optional[str] = None
    res_patr_n_19: Optional[float] = None
    u_patr_n_19: Optional[float] = None
    res_comparado_19: Optional[float] = None
    u_comparado_19: Optional[float] = None
    en_19: Optional[float] = None
    _tem_20: Optional[str] = None
    res_patr_n_20: Optional[float] = None
    u_patr_n_20: Optional[float] = None
    res_comparado_20: Optional[float] = None
    u_comparado_20: Optional[float] = None
    en_20: Optional[float] = None
    _tem_21: Optional[str] = None
    res_patr_n_21: Optional[float] = None
    u_patr_n_21: Optional[float] = None
    res_comparado_21: Optional[float] = None
    u_comparado_21: Optional[float] = None
    en_21: Optional[float] = None
    _tem_22: Optional[str] = None
    res_patr_n_22: Optional[float] = None
    u_patr_n_22: Optional[float] = None
    res_comparado_22: Optional[float] = None
    u_comparado_22: Optional[float] = None
    en_22: Optional[float] = None
    _tem_23: Optional[str] = None
    res_patr_n_23: Optional[float] = None
    u_patr_n_23: Optional[float] = None
    res_comparado_23: Optional[float] = None
    u_comparado_23: Optional[float] = None
    en_23: Optional[float] = None
    _tem_24: Optional[str] = None
    res_patr_n_24: Optional[float] = None
    u_patr_n_24: Optional[float] = None
    res_comparado_24: Optional[float] = None
    u_comparado_24: Optional[float] = None
    en_24: Optional[float] = None
    _tem_25: Optional[str] = None
    res_patr_n_25: Optional[float] = None
    u_patr_n_25: Optional[float] = None
    res_comparado_25: Optional[float] = None
    u_comparado_25: Optional[float] = None
    en_25: Optional[float] = None
    conclusi_n: Optional[str] = None
    observaciones: Optional[str] = None
    # trial817: Optional[str] = None

class PA_EQ_VECreate(PA_EQ_VEBase): pass
class PA_EQ_VEUpdate(PA_EQ_VEBase): pass
class PA_EQ_VE(PA_EQ_VEBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PA_IA_AHBase(BaseModel):
    id_am: Optional[int] = None
    registrado_por: Optional[str] = None
    servicio: Optional[str] = None
    til: Optional[float] = None
    hil: Optional[float] = None
    fecha_y_hora_inicio: Optional[datetime] = None
    ti: Optional[float] = None
    hi: Optional[float] = None
    tfl: Optional[float] = None
    hfl: Optional[float] = None
    fecha_y_hora_final: Optional[datetime] = None
    tf: Optional[float] = None
    hf: Optional[float] = None
    delta_t: Optional[float] = None
    delta_h: Optional[float] = None
    aceptado_t: Optional[str] = None
    aceptado_h: Optional[str] = None
    comentario: Optional[str] = None
    # trial817: Optional[str] = None

class PA_IA_AHCreate(PA_IA_AHBase): pass
class PA_IA_AHUpdate(PA_IA_AHBase): pass
class PA_IA_AH(PA_IA_AHBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PA_IA_AMBase(BaseModel):
    area: Optional[int] = None
    instrumento: Optional[str] = None
    tmin: Optional[float] = None
    tmax: Optional[float] = None
    hmin: Optional[float] = None
    hmax: Optional[float] = None
    delta_t_max: Optional[float] = None
    delta_h_max: Optional[float] = None
    # trial817: Optional[str] = None

class PA_IA_AMCreate(PA_IA_AMBase): pass
class PA_IA_AMUpdate(PA_IA_AMBase): pass
class PA_IA_AM(PA_IA_AMBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PA_IA_ARBase(BaseModel):
    area: Optional[str] = None
    # trial817: Optional[str] = None

class PA_IA_ARCreate(PA_IA_ARBase): pass
class PA_IA_ARUpdate(PA_IA_ARBase): pass
class PA_IA_AR(PA_IA_ARBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PA_IA_CABase(BaseModel):
    registrado_por: Optional[str] = None
    fecha: Optional[datetime] = None
    instalacion_condicion_ambiental: Optional[str] = None
    elemento: Optional[str] = None
    descripcion_del_control: Optional[str] = None
    control_eficaz: Optional[bool] = None
    # trial817: Optional[str] = None

class PA_IA_CACreate(PA_IA_CABase): pass
class PA_IA_CAUpdate(PA_IA_CABase): pass
class PA_IA_CA(PA_IA_CABase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PA_IA_LEBase(BaseModel):
    id_li: Optional[int] = None
    area: Optional[str] = None
    que: Optional[str] = None
    frecuencia: Optional[str] = None
    como: Optional[str] = None
    D1: Optional[str] = None
    D2: Optional[str] = None
    D3: Optional[str] = None
    D4: Optional[str] = None
    D5: Optional[str] = None
    D6: Optional[str] = None
    D7: Optional[str] = None
    D8: Optional[str] = None
    D9: Optional[str] = None
    D10: Optional[str] = None
    D11: Optional[str] = None
    D12: Optional[str] = None
    D13: Optional[str] = None
    D14: Optional[str] = None
    D15: Optional[str] = None
    D16: Optional[str] = None
    D17: Optional[str] = None
    D18: Optional[str] = None
    D19: Optional[str] = None
    D20: Optional[str] = None
    D21: Optional[str] = None
    D22: Optional[str] = None
    D23: Optional[str] = None
    D24: Optional[str] = None
    D25: Optional[str] = None
    D26: Optional[str] = None
    D27: Optional[str] = None
    D28: Optional[str] = None
    D29: Optional[str] = None
    D30: Optional[str] = None
    D31: Optional[str] = None
    # trial817: Optional[str] = None

class PA_IA_LECreate(PA_IA_LEBase): pass
class PA_IA_LEUpdate(PA_IA_LEBase): pass
class PA_IA_LE(PA_IA_LEBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PA_IA_LIBase(BaseModel):
    registrado_por: Optional[str] = None
    a_o: Optional[str] = None
    mes: Optional[str] = None
    fecha: Optional[datetime] = None
    comentarios: Optional[str] = None
    # trial817: Optional[str] = None

class PA_IA_LICreate(PA_IA_LIBase): pass
class PA_IA_LIUpdate(PA_IA_LIBase): pass
class PA_IA_LI(PA_IA_LIBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PA_IA_RABase(BaseModel):
    registrado_por: Optional[str] = None
    fecha: Optional[datetime] = None
    vigente: Optional[bool] = None
    instalacion: Optional[str] = None
    actividad_que_se_realizara: Optional[str] = None
    comentario: Optional[str] = None
    item_de_ca_1: Optional[str] = None
    requisito_1: Optional[str] = None
    item_de_ca_2: Optional[str] = None
    requisito_2: Optional[str] = None
    item_de_ca_3: Optional[str] = None
    requisito_3: Optional[str] = None
    item_de_ca_4: Optional[str] = None
    requisito_4: Optional[str] = None
    item_de_ca_5: Optional[str] = None
    requisito_5: Optional[str] = None
    item_de_ca_6: Optional[str] = None
    requisito_6: Optional[str] = None
    item_de_ca_7: Optional[str] = None
    requisito_7: Optional[str] = None
    item_de_ca_8: Optional[str] = None
    requisito_8: Optional[str] = None
    item_de_ca_9: Optional[str] = None
    requisito_9: Optional[str] = None
    item_de_ca_10: Optional[str] = None
    requisito_10: Optional[str] = None
    item_de_ca_11: Optional[str] = None
    requisito_11: Optional[str] = None
    item_de_ca_12: Optional[str] = None
    requisito_12: Optional[str] = None
    item_de_ca_13: Optional[str] = None
    requisito_13: Optional[str] = None
    item_de_ca_14: Optional[str] = None
    requisito_14: Optional[str] = None
    item_de_ca_15: Optional[str] = None
    requisito_15: Optional[str] = None
    item_de_ca_16: Optional[str] = None
    requisito_16: Optional[str] = None
    item_de_ca_17: Optional[str] = None
    requisito_17: Optional[str] = None
    item_de_ca_18: Optional[str] = None
    requisito_18: Optional[str] = None
    item_de_ca_19: Optional[str] = None
    requisito_19: Optional[str] = None
    item_de_ca_20: Optional[str] = None
    requisito_20: Optional[str] = None
    # trial817: Optional[str] = None

class PA_IA_RACreate(PA_IA_RABase): pass
class PA_IA_RAUpdate(PA_IA_RABase): pass
class PA_IA_RA(PA_IA_RABase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PA_IA_RIBase(BaseModel):
    registrado_por: Optional[str] = None
    fecha: Optional[datetime] = None
    vigente: Optional[bool] = None
    instalacion: Optional[str] = None
    actividad_que_se_realizara: Optional[str] = None
    comentario: Optional[str] = None
    item_de_instalacion_1: Optional[str] = None
    requisito_1: Optional[str] = None
    item_de_instalacion_2: Optional[str] = None
    requisito_2: Optional[str] = None
    item_de_instalacion_3: Optional[str] = None
    requisito_3: Optional[str] = None
    item_de_instalacion_4: Optional[str] = None
    requisito_4: Optional[str] = None
    item_de_instalacion_5: Optional[str] = None
    requisito_5: Optional[str] = None
    item_de_instalacion_6: Optional[str] = None
    requisito_6: Optional[str] = None
    item_de_instalacion_7: Optional[str] = None
    requisito_7: Optional[str] = None
    item_de_instalacion_8: Optional[str] = None
    requisito_8: Optional[str] = None
    item_de_instalacion_9: Optional[str] = None
    requisito_9: Optional[str] = None
    item_de_instalacion_10: Optional[str] = None
    requisito_10: Optional[str] = None
    item_de_instalacion_11: Optional[str] = None
    requisito_11: Optional[str] = None
    item_de_instalacion_12: Optional[str] = None
    requisito_12: Optional[str] = None
    item_de_instalacion_13: Optional[str] = None
    requisito_13: Optional[str] = None
    item_de_instalacion_14: Optional[str] = None
    requisito_14: Optional[str] = None
    item_de_instalacion_15: Optional[str] = None
    requisito_15: Optional[str] = None
    item_de_instalacion_16: Optional[str] = None
    requisito_16: Optional[str] = None
    item_de_instalacion_17: Optional[str] = None
    requisito_17: Optional[str] = None
    item_de_instalacion_18: Optional[str] = None
    requisito_18: Optional[str] = None
    item_de_instalacion_19: Optional[str] = None
    requisito_19: Optional[str] = None
    item_de_instalacion_20: Optional[str] = None
    requisito_20: Optional[str] = None
    # trial820: Optional[str] = None

class PA_IA_RICreate(PA_IA_RIBase): pass
class PA_IA_RIUpdate(PA_IA_RIBase): pass
class PA_IA_RI(PA_IA_RIBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PA_IA_SABase(BaseModel):
    registrado_por: Optional[str] = None
    fecha: Optional[datetime] = None
    id_requisitos_condiciones_ambientales: Optional[int] = None
    comentario: Optional[str] = None
    requiere_acciones: Optional[bool] = None
    evaluacion_requisito_1: Optional[str] = None
    conforme_1: Optional[bool] = None
    evaluacion_requisito_2: Optional[str] = None
    conforme_2: Optional[bool] = None
    evaluacion_requisito_3: Optional[str] = None
    conforme_3: Optional[bool] = None
    evaluacion_requisito_4: Optional[str] = None
    conforme_4: Optional[bool] = None
    evaluacion_requisito_5: Optional[str] = None
    conforme_5: Optional[bool] = None
    evaluacion_requisito_6: Optional[str] = None
    conforme_6: Optional[bool] = None
    evaluacion_requisito_7: Optional[str] = None
    conforme_7: Optional[bool] = None
    evaluacion_requisito_8: Optional[str] = None
    conforme_8: Optional[bool] = None
    evaluacion_requisito_9: Optional[str] = None
    conforme_9: Optional[bool] = None
    evaluacion_requisito_10: Optional[str] = None
    conforme_10: Optional[bool] = None
    evaluacion_requisito_11: Optional[str] = None
    conforme_11: Optional[bool] = None
    evaluacion_requisito_12: Optional[str] = None
    conforme_12: Optional[bool] = None
    evaluacion_requisito_13: Optional[str] = None
    conforme_13: Optional[bool] = None
    evaluacion_requisito_14: Optional[str] = None
    conforme_14: Optional[bool] = None
    evaluacion_requisito_15: Optional[str] = None
    conforme_15: Optional[bool] = None
    evaluacion_requisito_16: Optional[str] = None
    conforme_16: Optional[bool] = None
    evaluacion_requisito_17: Optional[str] = None
    conforme_17: Optional[bool] = None
    evaluacion_requisito_18: Optional[str] = None
    conforme_18: Optional[bool] = None
    evaluacion_requisito_19: Optional[str] = None
    conforme_19: Optional[bool] = None
    evaluacion_requisito_20: Optional[str] = None
    conforme_20: Optional[bool] = None
    # trial820: Optional[str] = None

class PA_IA_SACreate(PA_IA_SABase): pass
class PA_IA_SAUpdate(PA_IA_SABase): pass
class PA_IA_SA(PA_IA_SABase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PA_IA_SIBase(BaseModel):
    registrado_por: Optional[str] = None
    fecha: Optional[datetime] = None
    id_requisitos_de_instalacion: Optional[int] = None
    comentario: Optional[str] = None
    requiere_acciones: Optional[bool] = None
    evaluacion_requisito_1: Optional[str] = None
    conforme_1: Optional[bool] = None
    evaluacion_requisito_2: Optional[str] = None
    conforme_2: Optional[bool] = None
    evaluacion_requisito_3: Optional[str] = None
    conforme_3: Optional[bool] = None
    evaluacion_requisito_4: Optional[str] = None
    conforme_4: Optional[bool] = None
    evaluacion_requisito_5: Optional[str] = None
    conforme_5: Optional[bool] = None
    evaluacion_requisito_6: Optional[str] = None
    conforme_6: Optional[bool] = None
    evaluacion_requisito_7: Optional[str] = None
    conforme_7: Optional[bool] = None
    evaluacion_requisito_8: Optional[str] = None
    conforme_8: Optional[bool] = None
    evaluacion_requisito_9: Optional[str] = None
    conforme_9: Optional[bool] = None
    evaluacion_requisito_10: Optional[str] = None
    conforme_10: Optional[bool] = None
    evaluacion_requisito_11: Optional[str] = None
    conforme_11: Optional[bool] = None
    evaluacion_requisito_12: Optional[str] = None
    conforme_12: Optional[bool] = None
    evaluacion_requisito_13: Optional[str] = None
    conforme_13: Optional[bool] = None
    evaluacion_requisito_14: Optional[str] = None
    conforme_14: Optional[bool] = None
    evaluacion_requisito_15: Optional[str] = None
    conforme_15: Optional[bool] = None
    evaluacion_requisito_16: Optional[str] = None
    conforme_16: Optional[bool] = None
    evaluacion_requisito_17: Optional[str] = None
    conforme_17: Optional[bool] = None
    evaluacion_requisito_18: Optional[str] = None
    conforme_18: Optional[bool] = None
    evaluacion_requisito_19: Optional[str] = None
    conforme_19: Optional[bool] = None
    evaluacion_requisito_20: Optional[str] = None
    conforme_20: Optional[bool] = None
    # trial820: Optional[str] = None

class PA_IA_SICreate(PA_IA_SIBase): pass
class PA_IA_SIUpdate(PA_IA_SIBase): pass
class PA_IA_SI(PA_IA_SIBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PA_PE_AUBase(BaseModel):
    autorizado_por: Optional[str] = None
    fecha: Optional[datetime] = None
    autorizado_a: Optional[str] = None
    cargo: Optional[str] = None
    autorizacion_a: Optional[str] = None
    comentario: Optional[str] = None
    # trial820: Optional[str] = None

class PA_PE_AUCreate(PA_PE_AUBase): pass
class PA_PE_AUUpdate(PA_PE_AUBase): pass
class PA_PE_AU(PA_PE_AUBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PA_PE_CVBase(BaseModel):
    personal: Optional[str] = None
    requisito_de_competencia: Optional[str] = None
    carrera_curso_logro: Optional[str] = None
    institucion: Optional[str] = None
    fecha_inicio: Optional[datetime] = None
    fecha_final: Optional[datetime] = None
    carga_horaria: Optional[float] = None
    descripci_n: Optional[str] = None
    respaldo: Optional[str] = None
    # trial820: Optional[str] = None

class PA_PE_CVCreate(PA_PE_CVBase): pass
class PA_PE_CVUpdate(PA_PE_CVBase): pass
class PA_PE_CV(PA_PE_CVBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PA_PE_DEBase(BaseModel):
    id: Optional[int] = None
    cargo: Optional[str] = None
    # trial811: Optional[str] = None

class PA_PE_DECreate(PA_PE_DEBase): pass
class PA_PE_DEUpdate(PA_PE_DEBase): pass
class PA_PE_DE(PA_PE_DEBase):
    abreviacion: str
    model_config = ConfigDict(from_attributes=True)

class PA_PE_ECBase(BaseModel):
    id: Optional[int] = None
    # trial820: Optional[str] = None

class PA_PE_ECCreate(PA_PE_ECBase): pass
class PA_PE_ECUpdate(PA_PE_ECBase): pass
class PA_PE_EC(PA_PE_ECBase):
    elemento_de_competencia: str
    model_config = ConfigDict(from_attributes=True)

class PA_PE_EFBase(BaseModel):
    id_plan: Optional[int] = None
    fecha: Optional[datetime] = None
    participante_1: Optional[str] = None
    participante_2: Optional[str] = None
    participante_3: Optional[str] = None
    participante_4: Optional[str] = None
    participante_5: Optional[str] = None
    participante_6: Optional[str] = None
    participante_7: Optional[str] = None
    participante_8: Optional[str] = None
    participante_9: Optional[str] = None
    participante_10: Optional[str] = None
    comentarios_observaciones: Optional[str] = None
    actividad_evaluacion: Optional[str] = None
    conclusion_eficacia: Optional[str] = None
    eficaz: Optional[bool] = None
    cerrado: Optional[bool] = None
    # trial820: Optional[str] = None

class PA_PE_EFCreate(PA_PE_EFBase): pass
class PA_PE_EFUpdate(PA_PE_EFBase): pass
class PA_PE_EF(PA_PE_EFBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PA_PE_FGBase(BaseModel):
    forma_de_generacion: Optional[str] = None
    # trial820: Optional[str] = None

class PA_PE_FGCreate(PA_PE_FGBase): pass
class PA_PE_FGUpdate(PA_PE_FGBase): pass
class PA_PE_FG(PA_PE_FGBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PA_PE_IEBase(BaseModel):
    id_is: Optional[int] = None
    cargo: Optional[str] = None
    item: Optional[str] = None
    actividad: Optional[str] = None
    # trial820: Optional[str] = None

class PA_PE_IECreate(PA_PE_IEBase): pass
class PA_PE_IEUpdate(PA_PE_IEBase): pass
class PA_PE_IE(PA_PE_IEBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PA_PE_ISBase(BaseModel):
    cargo: Optional[str] = None
    item: Optional[str] = None
    comentarios: Optional[str] = None
    # trial820: Optional[str] = None

class PA_PE_ISCreate(PA_PE_ISBase): pass
class PA_PE_ISUpdate(PA_PE_ISBase): pass
class PA_PE_IS(PA_PE_ISBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PA_PE_PEBase(BaseModel):
    id: Optional[int] = None
    nombre: Optional[str] = None
    cargo: Optional[str] = None
    fotografia: Optional[str] = None
    fecha_de_nacimiento: Optional[datetime] = None
    direccion: Optional[str] = None
    telefono_personal: Optional[str] = None
    telefono_corporativo: Optional[str] = None
    movil_personal: Optional[str] = None
    movil_corporativo: Optional[str] = None
    email_personal: Optional[str] = None
    email_corporativo: Optional[str] = None
    nacionalidad: Optional[str] = None
    documento_de_identidad: Optional[str] = None
    estado_civil: Optional[str] = None
    categoria_de_licencia_de_conducir: Optional[str] = None
    vigente: Optional[bool] = None
    descripcion: Optional[str] = None
    # trial814: Optional[str] = None

class PA_PE_PECreate(PA_PE_PEBase): pass
class PA_PE_PEUpdate(PA_PE_PEBase): pass
class PA_PE_PE(PA_PE_PEBase):
    abreviatura: str
    model_config = ConfigDict(from_attributes=True)

class PA_PE_PLBase(BaseModel):
    item_del_programa: Optional[int] = None
    elaborado_por: Optional[str] = None
    fecha_inicio: Optional[datetime] = None
    forma_generacion: Optional[str] = None
    responsable_de_generacion_de_competencia: Optional[str] = None
    tematica: Optional[str] = None
    asistentes: Optional[str] = None
    comentarios_de_la_generacion_de_competencia: Optional[str] = None
    evaluacion_si_aplica: Optional[float] = None
    conclusion: Optional[str] = None
    respaldo1: Optional[str] = None
    respaldo2: Optional[str] = None
    respaldo3: Optional[str] = None
    competencia: Optional[bool] = None
    fecha_final: Optional[datetime] = None
    # trial820: Optional[str] = None

class PA_PE_PLCreate(PA_PE_PLBase): pass
class PA_PE_PLUpdate(PA_PE_PLBase): pass
class PA_PE_PL(PA_PE_PLBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PA_PE_POBase(BaseModel):
    proceso_de_seleccion: Optional[int] = None
    postulante: Optional[str] = None
    educacion: Optional[float] = None
    formacion: Optional[float] = None
    experiencia: Optional[float] = None
    habilidades: Optional[float] = None
    conocimientotecnico: Optional[float] = None
    calificacion: Optional[float] = None
    resultado_cv: Optional[float] = None
    pasa_a_entrevista: Optional[bool] = None
    item_entrevista1: Optional[float] = None
    item_entrevista2: Optional[float] = None
    item_entrevista3: Optional[float] = None
    item_entrevista4: Optional[float] = None
    item_entrevista5: Optional[float] = None
    resultado_entrevista: Optional[float] = None
    seleccionado: Optional[bool] = None
    # trial820: Optional[str] = None

class PA_PE_POCreate(PA_PE_POBase): pass
class PA_PE_POUpdate(PA_PE_POBase): pass
class PA_PE_PO(PA_PE_POBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PA_PE_PRBase(BaseModel):
    registrado_por: Optional[str] = None
    actividad: Optional[str] = None
    dirigido_a: Optional[str] = None
    competencia_por_adquirir: Optional[str] = None
    fecha_programada: Optional[datetime] = None
    comentarios: Optional[str] = None
    # trial820: Optional[str] = None

class PA_PE_PRCreate(PA_PE_PRBase): pass
class PA_PE_PRUpdate(PA_PE_PRBase): pass
class PA_PE_PR(PA_PE_PRBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PA_PE_RQBase(BaseModel):
    fecha: Optional[datetime] = None
    responsable: Optional[str] = None
    cargo_req: Optional[str] = None
    educacion1: Optional[str] = None
    educacion2: Optional[str] = None
    educacion3: Optional[str] = None
    formacion1: Optional[str] = None
    formacion2: Optional[str] = None
    formacion3: Optional[str] = None
    formacion4: Optional[str] = None
    formacion5: Optional[str] = None
    formacion6: Optional[str] = None
    formacion7: Optional[str] = None
    formacion8: Optional[str] = None
    formacion9: Optional[str] = None
    formacion10: Optional[str] = None
    experiencia1: Optional[str] = None
    experiencia2: Optional[str] = None
    experiencia3: Optional[str] = None
    experiencia4: Optional[str] = None
    experiencia5: Optional[str] = None
    habilidades1: Optional[str] = None
    habilidades2: Optional[str] = None
    habilidades3: Optional[str] = None
    habilidades4: Optional[str] = None
    habilidades5: Optional[str] = None
    habilidades6: Optional[str] = None
    habilidades7: Optional[str] = None
    habilidades8: Optional[str] = None
    habilidades9: Optional[str] = None
    habilidades10: Optional[str] = None
    conocimiento1: Optional[str] = None
    conocimiento2: Optional[str] = None
    conocimiento3: Optional[str] = None
    conocimiento4: Optional[str] = None
    conocimiento5: Optional[str] = None
    conocimiento6: Optional[str] = None
    conocimiento7: Optional[str] = None
    conocimiento8: Optional[str] = None
    conocimiento9: Optional[str] = None
    conocimiento10: Optional[str] = None
    calificacion1: Optional[str] = None
    calificacion2: Optional[str] = None
    calificacion3: Optional[str] = None
    calificacion4: Optional[str] = None
    calificacion5: Optional[str] = None
    aprobado_vigente: Optional[bool] = None
    comentarios: Optional[str] = None
    educacion1c: Optional[bool] = None
    educacion2c: Optional[bool] = None
    educacion3c: Optional[bool] = None
    formacion1c: Optional[bool] = None
    formacion2c: Optional[bool] = None
    formacion3c: Optional[bool] = None
    formacion4c: Optional[bool] = None
    formacion5c: Optional[bool] = None
    formacion6c: Optional[bool] = None
    formacion7c: Optional[bool] = None
    formacion8c: Optional[bool] = None
    formacion9c: Optional[bool] = None
    formacion10c: Optional[bool] = None
    experiencia1c: Optional[bool] = None
    experiencia2c: Optional[bool] = None
    experiencia3c: Optional[bool] = None
    experiencia4c: Optional[bool] = None
    experiencia5c: Optional[bool] = None
    habilidades1c: Optional[bool] = None
    habilidades2c: Optional[bool] = None
    habilidades3c: Optional[bool] = None
    habilidades4c: Optional[bool] = None
    habilidades5c: Optional[bool] = None
    habilidades6c: Optional[bool] = None
    habilidades7c: Optional[bool] = None
    habilidades8c: Optional[bool] = None
    habilidades9c: Optional[bool] = None
    habilidades10c: Optional[bool] = None
    conocimiento1c: Optional[bool] = None
    conocimiento2c: Optional[bool] = None
    conocimiento3c: Optional[bool] = None
    conocimiento4c: Optional[bool] = None
    conocimiento5c: Optional[bool] = None
    conocimiento6c: Optional[bool] = None
    conocimiento7c: Optional[bool] = None
    conocimiento8c: Optional[bool] = None
    conocimiento9c: Optional[bool] = None
    conocimiento10c: Optional[bool] = None
    calificacion1c: Optional[bool] = None
    calificacion2c: Optional[bool] = None
    calificacion3c: Optional[bool] = None
    calificacion4c: Optional[bool] = None
    calificacion5c: Optional[bool] = None
    # trial820: Optional[str] = None

class PA_PE_RQCreate(PA_PE_RQBase): pass
class PA_PE_RQUpdate(PA_PE_RQBase): pass
class PA_PE_RQ(PA_PE_RQBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PA_PE_SEBase(BaseModel):
    responsable: Optional[str] = None
    fecha: Optional[datetime] = None
    personal: Optional[str] = None
    cargo: Optional[str] = None
    doc1: Optional[str] = None
    doc2: Optional[str] = None
    doc3: Optional[str] = None
    doc4: Optional[str] = None
    doc5: Optional[str] = None
    requisitos: Optional[int] = None
    ev_educacion1: Optional[str] = None
    cumple_educacion1: Optional[bool] = None
    ev_educacion2: Optional[str] = None
    cumple_educacion2: Optional[bool] = None
    ev_educacion3: Optional[str] = None
    cumple_educacion3: Optional[bool] = None
    ev_formacion1: Optional[str] = None
    cumple_formacion1: Optional[bool] = None
    ev_formacion2: Optional[str] = None
    cumple_formacion2: Optional[bool] = None
    ev_formacion3: Optional[str] = None
    cumple_formacion3: Optional[bool] = None
    ev_formacion4: Optional[str] = None
    cumple_formacion4: Optional[bool] = None
    ev_formacion5: Optional[str] = None
    cumple_formacion5: Optional[bool] = None
    ev_formacion6: Optional[str] = None
    cumple_formacion6: Optional[bool] = None
    ev_formacion7: Optional[str] = None
    cumple_formacion7: Optional[bool] = None
    ev_formacion8: Optional[str] = None
    cumple_formacion8: Optional[bool] = None
    ev_formacion9: Optional[str] = None
    cumple_formacion9: Optional[bool] = None
    ev_formacion10: Optional[str] = None
    cumple_formacion10: Optional[bool] = None
    ev_experiencia1: Optional[str] = None
    cumple_experiencia1: Optional[bool] = None
    ev_experiencia2: Optional[str] = None
    cumple_experiencia2: Optional[bool] = None
    ev_experiencia3: Optional[str] = None
    cumple_experiencia3: Optional[bool] = None
    ev_experiencia4: Optional[str] = None
    cumple_experiencia4: Optional[bool] = None
    ev_experiencia5: Optional[str] = None
    cumple_experiencia5: Optional[bool] = None
    ev_habilidades1: Optional[str] = None
    cumple_habilidades1: Optional[bool] = None
    ev_habilidades2: Optional[str] = None
    cumple_habilidades2: Optional[bool] = None
    ev_habilidades3: Optional[str] = None
    cumple_habilidades3: Optional[bool] = None
    ev_habilidades4: Optional[str] = None
    cumple_habilidades4: Optional[bool] = None
    ev_habilidades5: Optional[str] = None
    cumple_habilidades5: Optional[bool] = None
    ev_habilidades6: Optional[str] = None
    cumple_habilidades6: Optional[bool] = None
    ev_habilidades7: Optional[str] = None
    cumple_habilidades7: Optional[bool] = None
    ev_habilidades8: Optional[str] = None
    cumple_habilidades8: Optional[bool] = None
    ev_habilidades9: Optional[str] = None
    cumple_habilidades9: Optional[bool] = None
    ev_habilidades10: Optional[str] = None
    cumple_habilidades10: Optional[bool] = None
    ev_conocimiento1: Optional[str] = None
    cumple_conocimiento1: Optional[bool] = None
    ev_conocimiento2: Optional[str] = None
    cumple_conocimiento2: Optional[bool] = None
    ev_conocimiento3: Optional[str] = None
    cumple_conocimiento3: Optional[bool] = None
    ev_conocimiento4: Optional[str] = None
    cumple_conocimiento4: Optional[bool] = None
    ev_conocimiento5: Optional[str] = None
    cumple_conocimiento5: Optional[bool] = None
    ev_conocimiento6: Optional[str] = None
    cumple_conocimiento6: Optional[bool] = None
    ev_conocimiento7: Optional[str] = None
    cumple_conocimiento7: Optional[bool] = None
    ev_conocimiento8: Optional[str] = None
    cumple_conocimiento8: Optional[bool] = None
    ev_conocimiento9: Optional[str] = None
    cumple_conocimiento9: Optional[bool] = None
    ev_conocimiento10: Optional[str] = None
    cumple_conocimiento10: Optional[bool] = None
    ev_calificacion1: Optional[str] = None
    cumple_calificacion1: Optional[bool] = None
    ev_calificacion2: Optional[str] = None
    cumple_calificacion2: Optional[bool] = None
    ev_calificacion3: Optional[str] = None
    cumple_calificacion3: Optional[bool] = None
    ev_calificacion4: Optional[str] = None
    cumple_calificacion4: Optional[bool] = None
    ev_calificacion5: Optional[str] = None
    cumple_calificacion5: Optional[bool] = None
    conclusion: Optional[str] = None
    competencia_asegurada: Optional[bool] = None
    educacion1: Optional[str] = None
    educacion1c: Optional[bool] = None
    educacion2: Optional[str] = None
    educacion2c: Optional[bool] = None
    educacion3: Optional[str] = None
    educacion3c: Optional[bool] = None
    formacion1: Optional[str] = None
    formacion1c: Optional[bool] = None
    formacion2: Optional[str] = None
    formacion2c: Optional[bool] = None
    formacion3: Optional[str] = None
    formacion3c: Optional[bool] = None
    formacion4: Optional[str] = None
    formacion4c: Optional[bool] = None
    formacion5: Optional[str] = None
    formacion5c: Optional[bool] = None
    formacion6: Optional[str] = None
    formacion6c: Optional[bool] = None
    formacion7: Optional[str] = None
    formacion7c: Optional[bool] = None
    formacion8: Optional[str] = None
    formacion8c: Optional[bool] = None
    formacion9: Optional[str] = None
    formacion9c: Optional[bool] = None
    formacion10: Optional[str] = None
    formacion10c: Optional[bool] = None
    experiencia1: Optional[str] = None
    experiencia1c: Optional[bool] = None
    experiencia2: Optional[str] = None
    experiencia2c: Optional[bool] = None
    experiencia3: Optional[str] = None
    experiencia3c: Optional[bool] = None
    experiencia4: Optional[str] = None
    experiencia4c: Optional[bool] = None
    experiencia5: Optional[str] = None
    experiencia5c: Optional[bool] = None
    habilidades1: Optional[str] = None
    habilidades1c: Optional[bool] = None
    habilidades2: Optional[str] = None
    habilidades2c: Optional[bool] = None
    habilidades3: Optional[str] = None
    habilidades3c: Optional[bool] = None
    habilidades4: Optional[str] = None
    habilidades4c: Optional[bool] = None
    habilidades5: Optional[str] = None
    habilidades5c: Optional[bool] = None
    habilidades6: Optional[str] = None
    habilidades6c: Optional[bool] = None
    habilidades7: Optional[str] = None
    habilidades7c: Optional[bool] = None
    habilidades8: Optional[str] = None
    habilidades8c: Optional[bool] = None
    habilidades9: Optional[str] = None
    habilidades9c: Optional[bool] = None
    habilidades10: Optional[str] = None
    habilidades10c: Optional[bool] = None
    conocimiento1: Optional[str] = None
    conocimiento1c: Optional[bool] = None
    conocimiento2: Optional[str] = None
    conocimiento2c: Optional[bool] = None
    conocimiento3: Optional[str] = None
    conocimiento3c: Optional[bool] = None
    conocimiento4: Optional[str] = None
    conocimiento4c: Optional[bool] = None
    conocimiento5: Optional[str] = None
    conocimiento5c: Optional[bool] = None
    conocimiento6: Optional[str] = None
    conocimiento6c: Optional[bool] = None
    conocimiento7: Optional[str] = None
    conocimiento7c: Optional[bool] = None
    conocimiento8: Optional[str] = None
    conocimiento8c: Optional[bool] = None
    conocimiento9: Optional[str] = None
    conocimiento9c: Optional[bool] = None
    conocimiento10: Optional[str] = None
    conocimiento10c: Optional[bool] = None
    calificacion1: Optional[str] = None
    calificacion1c: Optional[bool] = None
    calificacion2: Optional[str] = None
    calificacion2c: Optional[bool] = None
    calificacion3: Optional[str] = None
    calificacion3c: Optional[bool] = None
    calificacion4: Optional[str] = None
    calificacion4c: Optional[bool] = None
    calificacion5: Optional[str] = None
    calificacion5c: Optional[bool] = None
    educacion1n: Optional[int] = None
    educacion2n: Optional[int] = None
    educacion3n: Optional[int] = None
    formacion1n: Optional[int] = None
    formacion2n: Optional[int] = None
    formacion3n: Optional[int] = None
    formacion4n: Optional[int] = None
    formacion5n: Optional[int] = None
    formacion6n: Optional[int] = None
    formacion7n: Optional[int] = None
    formacion8n: Optional[int] = None
    formacion9n: Optional[int] = None
    formacion10n: Optional[int] = None
    experiencia1n: Optional[int] = None
    experiencia2n: Optional[int] = None
    experiencia3n: Optional[int] = None
    experiencia4n: Optional[int] = None
    experiencia5n: Optional[int] = None
    habilidades1n: Optional[int] = None
    habilidades2n: Optional[int] = None
    habilidades3n: Optional[int] = None
    habilidades4n: Optional[int] = None
    habilidades5n: Optional[int] = None
    habilidades6n: Optional[int] = None
    habilidades7n: Optional[int] = None
    habilidades8n: Optional[int] = None
    habilidades9n: Optional[int] = None
    habilidades10n: Optional[int] = None
    conocimiento1n: Optional[int] = None
    conocimiento2n: Optional[int] = None
    conocimiento3n: Optional[int] = None
    conocimiento4n: Optional[int] = None
    conocimiento5n: Optional[int] = None
    conocimiento6n: Optional[int] = None
    conocimiento7n: Optional[int] = None
    conocimiento8n: Optional[int] = None
    conocimiento9n: Optional[int] = None
    conocimiento10n: Optional[int] = None
    calificacion1n: Optional[int] = None
    calificacion2n: Optional[int] = None
    calificacion3n: Optional[int] = None
    calificacion4n: Optional[int] = None
    calificacion5n: Optional[int] = None
    promedio: Optional[int] = None
    escala: Optional[int] = None
    # trial820: Optional[str] = None

class PA_PE_SECreate(PA_PE_SEBase): pass
class PA_PE_SEUpdate(PA_PE_SEBase): pass
class PA_PE_SE(PA_PE_SEBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PA_PE_SPBase(BaseModel):
    puesto: Optional[str] = None
    fecha_inicial: Optional[datetime] = None
    evaluadores: Optional[str] = None
    ponderacion_educacion: Optional[float] = None
    ponderacion_formacion: Optional[float] = None
    ponderacion_habilidades: Optional[float] = None
    ponderacion_experiencia: Optional[float] = None
    ponderacion_conocimientotecnico: Optional[float] = None
    ponderacion_calificacion: Optional[float] = None
    ponderacion_minima_cv: Optional[float] = None
    conclusion_cv: Optional[str] = None
    item_entrevista_1: Optional[str] = None
    ponderacion_entrevista_1: Optional[float] = None
    item_entrevista_2: Optional[str] = None
    ponderacion_entrevista_2: Optional[float] = None
    item_entrevista_3: Optional[str] = None
    ponderacion_entrevista_3: Optional[float] = None
    item_entrevista_4: Optional[str] = None
    ponderacion_entrevista_4: Optional[float] = None
    item_entrevista_5: Optional[str] = None
    ponderacion_entrevista_5: Optional[float] = None
    ponderacion_minima_entrevista: Optional[float] = None
    conclusion_entrevista: Optional[str] = None
    fecha_final: Optional[datetime] = None
    # trial820: Optional[str] = None

class PA_PE_SPCreate(PA_PE_SPBase): pass
class PA_PE_SPUpdate(PA_PE_SPBase): pass
class PA_PE_SP(PA_PE_SPBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PA_PE_SUBase(BaseModel):
    fecha: Optional[datetime] = None
    supervisores: Optional[str] = None
    supervisados: Optional[str] = None
    item_de_supervision_1: Optional[str] = None
    supervision_exitosa_1: Optional[bool] = None
    item_de_supervision_2: Optional[str] = None
    supervision_exitosa_2: Optional[bool] = None
    item_de_supervision_3: Optional[str] = None
    supervision_exitosa_3: Optional[bool] = None
    item_de_supervision_4: Optional[str] = None
    supervision_exitosa_4: Optional[bool] = None
    item_de_supervision_5: Optional[str] = None
    supervision_exitosa_5: Optional[bool] = None
    item_de_supervision_6: Optional[str] = None
    supervision_exitosa_6: Optional[bool] = None
    item_de_supervision_7: Optional[str] = None
    supervision_exitosa_7: Optional[bool] = None
    item_de_supervision_8: Optional[str] = None
    supervision_exitosa_8: Optional[bool] = None
    item_de_supervision_9: Optional[str] = None
    supervision_exitosa_9: Optional[bool] = None
    item_de_supervision_10: Optional[str] = None
    supervision_exitosa_10: Optional[bool] = None
    comentarios: Optional[str] = None
    requiere_adquirir_o_aumentar_competencia: Optional[bool] = None
    cargo: Optional[str] = None
    item: Optional[str] = None
    # trial820: Optional[str] = None

class PA_PE_SUCreate(PA_PE_SUBase): pass
class PA_PE_SUUpdate(PA_PE_SUBase): pass
class PA_PE_SU(PA_PE_SUBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PA_PE_TPBase(BaseModel):
    nombre: Optional[str] = None
    cargo: Optional[str] = None
    parametro_a_evaluar: Optional[int] = None
    codigo_material: Optional[int] = None
    valor_de_referencia: Optional[int] = None
    valor_medido: Optional[int] = None
    incertidumbre: Optional[int] = None
    incertidumbre_muestra: Optional[int] = None
    dispersi_n: Optional[int] = None
    z: Optional[int] = None
    evaluador: Optional[str] = None
    cargo_evaluador: Optional[str] = None
    fecha: Optional[datetime] = None
    comentarios_dispersi_n: Optional[str] = None
    # trial824: Optional[str] = None

class PA_PE_TPCreate(PA_PE_TPBase): pass
class PA_PE_TPUpdate(PA_PE_TPBase): pass
class PA_PE_TP(PA_PE_TPBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PA_PS_ADBase(BaseModel):
    registrado_por: Optional[str] = None
    fecha: Optional[datetime] = None
    producto_o_servicio: Optional[str] = None
    proveedor_seleccionado: Optional[int] = None
    precio_unitario: Optional[float] = None
    cantidad: Optional[float] = None
    recursos_requeridos_bs: Optional[float] = None
    doc_1: Optional[str] = None
    doc_2: Optional[str] = None
    comunicacion_1: Optional[str] = None
    comunicacion_2: Optional[str] = None
    fecha_recepci_n: Optional[datetime] = None
    observaciones: Optional[str] = None
    id_requisitos_de_productos_y_servicios: Optional[int] = None
    especificacion_1: Optional[str] = None
    comentario_esp_1: Optional[str] = None
    cumple_esp_1: Optional[bool] = None
    especificacion_2: Optional[str] = None
    comentario_esp_2: Optional[str] = None
    cumple_esp_2: Optional[bool] = None
    especificacion_3: Optional[str] = None
    comentario_esp_3: Optional[str] = None
    cumple_esp_3: Optional[bool] = None
    especificacion_4: Optional[str] = None
    comentario_esp_4: Optional[str] = None
    cumple_esp_4: Optional[bool] = None
    especificacion_5: Optional[str] = None
    comentario_esp_5: Optional[str] = None
    cumple_esp_5: Optional[bool] = None
    conclusi_n_evaluaci_n: Optional[str] = None
    reclamo_u_observaci_n_al_proveedor: Optional[str] = None
    doc_3: Optional[str] = None
    doc_4: Optional[str] = None
    retroalimentacion_realizada: Optional[bool] = None
    retroalimentacion: Optional[str] = None
    cerrado_eficazmente: Optional[bool] = None
    # trial814: Optional[str] = None

class PA_PS_ADCreate(PA_PS_ADBase): pass
class PA_PS_ADUpdate(PA_PS_ADBase): pass
class PA_PS_AD(PA_PS_ADBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PA_PS_CRBase(BaseModel):
    criterio: Optional[str] = None
    categoria: Optional[str] = None
    ponderacion: Optional[float] = None
    # trial824: Optional[str] = None

class PA_PS_CRCreate(PA_PS_CRBase): pass
class PA_PS_CRUpdate(PA_PS_CRBase): pass
class PA_PS_CR(PA_PS_CRBase):
    id_criterio: int
    model_config = ConfigDict(from_attributes=True)

class PA_PS_DEBase(BaseModel):
    id_evaluacion: Optional[int] = None
    id_criterio: Optional[int] = None
    puntuacion: Optional[int] = None
    # trial824: Optional[str] = None

class PA_PS_DECreate(PA_PS_DEBase): pass
class PA_PS_DEUpdate(PA_PS_DEBase): pass
class PA_PS_DE(PA_PS_DEBase):
    id_detalle: int
    model_config = ConfigDict(from_attributes=True)

class PA_PS_EVBase(BaseModel):
    id_evaluacion: Optional[int] = None
    id_proveedor: Optional[int] = None
    id_adquisicion: Optional[int] = None
    id_productoservicio: Optional[int] = None
    fecha_evaluacion: Optional[datetime] = None
    tipo_evaluacion: Optional[str] = None
    puntaje_final: Optional[float] = None
    calificacion_final: Optional[str] = None
    observacion_general: Optional[str] = None
    # trial824: Optional[str] = None

class PA_PS_EVCreate(PA_PS_EVBase): pass
class PA_PS_EVUpdate(PA_PS_EVBase): pass
class PA_PS_EV(PA_PS_EVBase):
    model_config = ConfigDict(from_attributes=True)

class PA_PS_OSBase(BaseModel):
    id_ad: Optional[int] = None
    descripcion: Optional[str] = None
    cantidad: Optional[float] = None
    precio_unitario: Optional[float] = None
    importe: Optional[float] = None
    # trial824: Optional[str] = None

class PA_PS_OSCreate(PA_PS_OSBase): pass
class PA_PS_OSUpdate(PA_PS_OSBase): pass
class PA_PS_OS(PA_PS_OSBase):
    id_os: int
    model_config = ConfigDict(from_attributes=True)

class PA_PS_PRBase(BaseModel):
    id: Optional[int] = None
    razon_social: Optional[str] = None
    nit: Optional[str] = None
    direcci_n: Optional[str] = None
    tel_fono_celular: Optional[str] = None
    correo_electr_nico: Optional[str] = None
    persona_de_contacto: Optional[str] = None
    comentario_observaci_n: Optional[str] = None
    doc_prov_1: Optional[str] = None
    doc_prov_2: Optional[str] = None
    doc_prov_3: Optional[str] = None
    # trial824: Optional[str] = None

class PA_PS_PRCreate(PA_PS_PRBase): pass
class PA_PS_PRUpdate(PA_PS_PRBase): pass
class PA_PS_PR(PA_PS_PRBase):
    proveedor: str
    model_config = ConfigDict(from_attributes=True)

class PA_PS_PSBase(BaseModel):
    producto_servicio: Optional[str] = None
    comentario: Optional[str] = None
    rango_valor_nominal: Optional[str] = None
    resoluci_n_o_clase: Optional[str] = None
    contenedor_estuche: Optional[str] = None
    accesorios: Optional[str] = None
    especificacion_1: Optional[str] = None
    especificacion_2: Optional[str] = None
    especificacion_3: Optional[str] = None
    especificacion_4: Optional[str] = None
    especificacion_5: Optional[str] = None
    observaciones: Optional[str] = None
    adjunto1: Optional[str] = None
    adjunto2: Optional[str] = None
    adjunto3: Optional[str] = None
    vigente: Optional[bool] = None
    # trial814: Optional[str] = None

class PA_PS_PSCreate(PA_PS_PSBase): pass
class PA_PS_PSUpdate(PA_PS_PSBase): pass
class PA_PS_PS(PA_PS_PSBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PC_ES_ESBase(BaseModel):
    id: Optional[int] = None
    responsable: Optional[str] = None
    fecha: Optional[datetime] = None
    ensayo: Optional[str] = None
    tipo_de_sr: Optional[str] = None
    a: Optional[float] = None
    b: Optional[float] = None
    c: Optional[float] = None
    d: Optional[float] = None
    rr: Optional[float] = None
    rrv: Optional[float] = None
    srrv: Optional[float] = None
    rrp3: Optional[float] = None
    rrp2: Optional[float] = None
    rrl3: Optional[float] = None
    rrl2: Optional[float] = None
    vigente: Optional[bool] = None
    comentarios: Optional[str] = None
    mr: Optional[str] = None
    rre: Optional[float] = None
    balanza: Optional[str] = None
    termohigrometro: Optional[str] = None
    tli: Optional[float] = None
    hli: Optional[float] = None
    tlf: Optional[float] = None
    hlf: Optional[float] = None
    ti: Optional[float] = None
    hi: Optional[float] = None
    tf: Optional[float] = None
    hf: Optional[float] = None
    delta_t: Optional[float] = None
    delta_h: Optional[float] = None
    aceptado_t: Optional[str] = None
    aceptado_h: Optional[str] = None
    # trial824: Optional[str] = None

class PC_ES_ESCreate(PC_ES_ESBase): pass
class PC_ES_ESUpdate(PC_ES_ESBase): pass
class PC_ES_ES(PC_ES_ESBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PC_LAB_PATRONESBase(BaseModel):
    descripcion: Optional[str] = None
    valor_verdadero: Optional[float] = None
    incertidumbre: Optional[float] = None
    # trial824: Optional[str] = None

class PC_LAB_PATRONESCreate(PC_LAB_PATRONESBase): pass
class PC_LAB_PATRONESUpdate(PC_LAB_PATRONESBase): pass
class PC_LAB_PATRONES(PC_LAB_PATRONESBase):
    codigo_patron: str
    model_config = ConfigDict(from_attributes=True)

class PC_LAB_SOLUCIONESBase(BaseModel):
    nombre_solucion: Optional[str] = None
    lote_interno: Optional[str] = None
    fecha_preparacion: Optional[datetime] = None
    fecha_vencimiento: Optional[datetime] = None
    normalidad_teorica: Optional[float] = None
    factor_correcion: Optional[float] = None
    estado: Optional[str] = None
    peso_equivalente_patron: Optional[float] = None
    rsd_obtenido: Optional[float] = None
    # trial824: Optional[str] = None

class PC_LAB_SOLUCIONESCreate(PC_LAB_SOLUCIONESBase): pass
class PC_LAB_SOLUCIONESUpdate(PC_LAB_SOLUCIONESBase): pass
class PC_LAB_SOLUCIONES(PC_LAB_SOLUCIONESBase):
    id_solucion: int
    model_config = ConfigDict(from_attributes=True)

class PC_LAB_SOLUCIONES_DETBase(BaseModel):
    id_solucion: Optional[int] = None
    masa_patron: Optional[float] = None
    volumen_gasto: Optional[float] = None
    factor_calculado: Optional[float] = None
    # trial824: Optional[str] = None

class PC_LAB_SOLUCIONES_DETCreate(PC_LAB_SOLUCIONES_DETBase): pass
class PC_LAB_SOLUCIONES_DETUpdate(PC_LAB_SOLUCIONES_DETBase): pass
class PC_LAB_SOLUCIONES_DET(PC_LAB_SOLUCIONES_DETBase):
    id_replica: int
    model_config = ConfigDict(from_attributes=True)

class PC_LAB_VALIDACIONMETODOSBase(BaseModel):
    nombre_metodo: Optional[str] = None
    limite_cuantificacion: Optional[float] = None
    limite_deteccion: Optional[float] = None
    decimales_reporte: Optional[int] = None
    modelo_repetibilidad: Optional[str] = None
    coef_a: Optional[float] = None
    coef_b: Optional[float] = None
    coef_c: Optional[float] = None
    limite_sesgo: Optional[float] = None
    # trial824: Optional[str] = None

class PC_LAB_VALIDACIONMETODOSCreate(PC_LAB_VALIDACIONMETODOSBase): pass
class PC_LAB_VALIDACIONMETODOSUpdate(PC_LAB_VALIDACIONMETODOSBase): pass
class PC_LAB_VALIDACIONMETODOS(PC_LAB_VALIDACIONMETODOSBase):
    id_metodo: int
    model_config = ConfigDict(from_attributes=True)

class PC_QR_QUBase(BaseModel):
    id: Optional[int] = None
    registrado_por: Optional[str] = None
    fecha: Optional[datetime] = None
    codigo_servicio: Optional[str] = None
    contacto: Optional[str] = None
    descripci_n: Optional[str] = None
    recibido_v_a: Optional[str] = None
    procede: Optional[bool] = None
    evaluacion_entrevistas: Optional[str] = None
    acciones_a_tomar: Optional[str] = None
    comunicaci_n_tratamiento: Optional[str] = None
    medio_tratamiento: Optional[str] = None
    comunicaci_n_cierre: Optional[str] = None
    medio_cierre: Optional[str] = None
    queja_cerrada: Optional[bool] = None
    seguimiento_por: Optional[str] = None
    comunicado_por: Optional[str] = None
    queja_con_probabilidad_de_que_se_repita: Optional[bool] = None
    # trial824: Optional[str] = None

class PC_QR_QUCreate(PC_QR_QUBase): pass
class PC_QR_QUUpdate(PC_QR_QUBase): pass
class PC_QR_QU(PC_QR_QUBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PC_RE_ACBase(BaseModel):
    registrado_y_recepcionado_por: Optional[str] = None
    fecha_de_registro: Optional[datetime] = None
    n_registro: Optional[str] = None
    proforma: Optional[int] = None
    cliente: Optional[int] = None
    direccion: Optional[str] = None
    ciudad: Optional[str] = None
    pais: Optional[str] = None
    contacto: Optional[int] = None
    celular: Optional[str] = None
    e_mail: Optional[str] = None
    personal: Optional[bool] = None
    inst_cond_amb: Optional[bool] = None
    equipamiento: Optional[bool] = None
    metodo: Optional[bool] = None
    tiempo_capacidad: Optional[bool] = None
    comentarios_de_recursos: Optional[str] = None
    responsable_de_muestra: Optional[str] = None
    nro_de_muestras: Optional[int] = None
    insertar_muestras: Optional[bool] = None
    servicio_global: Optional[int] = None
    todos_global: Optional[bool] = None
    enviar_global: Optional[bool] = None
    servicio: Optional[int] = None
    todos: Optional[bool] = None
    enviar: Optional[bool] = None
    fecha_de_recepcion: Optional[datetime] = None
    dias_de_entrega: Optional[int] = None
    fecha_estimada_de_entrega: Optional[datetime] = None
    entregado_por: Optional[str] = None
    ot: Optional[str] = None
    registro_ot: Optional[str] = None
    numero_de_muestras: Optional[int] = None
    fecha_de_entrega_a_ensayo: Optional[datetime] = None
    fecha_de_entrega_de_resultados_al_area: Optional[datetime] = None
    fecha_de_descarte_de_la_muestra: Optional[datetime] = None
    fecha_de_inicio_del_analisis: Optional[datetime] = None
    fecha_de_entrega_de_los_resultados: Optional[datetime] = None
    analista_responsable: Optional[str] = None
    tipo_de_muestra: Optional[str] = None
    producto: Optional[str] = None
    marca: Optional[str] = None
    cantidad: Optional[str] = None
    tipo_de_envase: Optional[str] = None
    vencimiento: Optional[str] = None
    caracteristicas: Optional[str] = None
    tipo_de_muestra_todos: Optional[bool] = None
    producto_todos: Optional[bool] = None
    marca_todos: Optional[bool] = None
    cantidad_todos: Optional[bool] = None
    tipo_de_envase_todos: Optional[bool] = None
    vencimiento_todos: Optional[bool] = None
    caracteristicas_todos: Optional[bool] = None
    tipo_de_muestra_enviar: Optional[bool] = None
    producto_enviar: Optional[bool] = None
    marca_enviar: Optional[bool] = None
    cantidad_enviar: Optional[bool] = None
    tipo_de_envase_enviar: Optional[bool] = None
    vencimiento_enviar: Optional[bool] = None
    caracteristicas_enviar: Optional[bool] = None
    # trial824: Optional[str] = None

class PC_RE_ACCreate(PC_RE_ACBase): pass
class PC_RE_ACUpdate(PC_RE_ACBase): pass
class PC_RE_AC(PC_RE_ACBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PC_RE_ANALISISBase(BaseModel):
    id_ac: Optional[int] = None
    id_muestra: Optional[int] = None
    codigo_muestra: Optional[str] = None
    ensayo_solicitado: Optional[str] = None
    metodo_nombre: Optional[str] = None
    unidades_reporte: Optional[str] = None
    estado: Optional[str] = None
    fecha_analisis: Optional[datetime] = None
    analista: Optional[str] = None
    tipo_registro: Optional[str] = None
    referencia_qa: Optional[str] = None
    id_termohigrometro: Optional[str] = None
    temp_ini: Optional[float] = None
    hum_ini: Optional[float] = None
    temp_fin: Optional[float] = None
    hum_fin: Optional[float] = None
    id_balanza: Optional[str] = None
    id_bureta: Optional[str] = None
    id_solucion: Optional[int] = None
    r1_masa_lectura: Optional[float] = None
    r1_masa_real: Optional[float] = None
    r1_vol_lectura: Optional[float] = None
    r1_vol_real: Optional[float] = None
    r2_masa_lectura: Optional[float] = None
    r2_masa_real: Optional[float] = None
    r2_vol_lectura: Optional[float] = None
    r2_vol_real: Optional[float] = None
    r3_masa_lectura: Optional[float] = None
    r3_masa_real: Optional[float] = None
    r3_vol_lectura: Optional[float] = None
    r3_vol_real: Optional[float] = None
    factor11: Optional[float] = None
    factor12: Optional[float] = None
    factor13: Optional[float] = None
    factor14: Optional[float] = None
    factor15: Optional[float] = None
    resultado_promedio: Optional[float] = None
    desviacion_s: Optional[float] = None
    resultado_final_reporte: Optional[str] = None
    conformidad: Optional[str] = None
    factor11_real: Optional[float] = None
    factor12_real: Optional[float] = None
    factor13_real: Optional[float] = None
    factor14_real: Optional[float] = None
    factor15_real: Optional[float] = None
    # trial827: Optional[str] = None

class PC_RE_ANALISISCreate(PC_RE_ANALISISBase): pass
class PC_RE_ANALISISUpdate(PC_RE_ANALISISBase): pass
class PC_RE_ANALISIS(PC_RE_ANALISISBase):
    id_analisis: int
    model_config = ConfigDict(from_attributes=True)

class PC_RE_CCBase(BaseModel):
    id_cl: Optional[int] = None
    contacto: Optional[str] = None
    celular: Optional[str] = None
    e_mail: Optional[str] = None
    # trial824: Optional[str] = None

class PC_RE_CCCreate(PC_RE_CCBase): pass
class PC_RE_CCUpdate(PC_RE_CCBase): pass
class PC_RE_CC(PC_RE_CCBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PC_RE_CLBase(BaseModel):
    cliente: Optional[str] = None
    nit: Optional[str] = None
    direccion: Optional[str] = None
    ciudad: Optional[str] = None
    pais: Optional[str] = None
    telefono: Optional[str] = None
    e_mail: Optional[str] = None
    # trial824: Optional[str] = None

class PC_RE_CLCreate(PC_RE_CLBase): pass
class PC_RE_CLUpdate(PC_RE_CLBase): pass
class PC_RE_CL(PC_RE_CLBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PC_RE_COBase(BaseModel):
    fecha: Optional[datetime] = None
    revisado_por: Optional[str] = None
    informacion_por_revisar: Optional[str] = None
    revision: Optional[str] = None
    informacion_revisada: Optional[str] = None
    # trial827: Optional[str] = None

class PC_RE_COCreate(PC_RE_COBase): pass
class PC_RE_COUpdate(PC_RE_COBase): pass
class PC_RE_CO(PC_RE_COBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PC_RE_MUBase(BaseModel):
    id_ac: Optional[int] = None
    codigo: Optional[str] = None
    tipo_de_muestra: Optional[str] = None
    producto: Optional[str] = None
    marca: Optional[str] = None
    cantidad: Optional[str] = None
    tipo_de_envase: Optional[str] = None
    vencimiento: Optional[str] = None
    caracteristicas: Optional[str] = None
    ensayo01: Optional[str] = None
    unidades01: Optional[str] = None
    metodo01: Optional[str] = None
    ensayo02: Optional[str] = None
    unidades02: Optional[str] = None
    metodo02: Optional[str] = None
    ensayo03: Optional[str] = None
    unidades03: Optional[str] = None
    metodo03: Optional[str] = None
    ensayo04: Optional[str] = None
    unidades04: Optional[str] = None
    metodo04: Optional[str] = None
    ensayo05: Optional[str] = None
    unidades05: Optional[str] = None
    metodo05: Optional[str] = None
    ensayo06: Optional[str] = None
    unidades06: Optional[str] = None
    metodo06: Optional[str] = None
    ensayo07: Optional[str] = None
    unidades07: Optional[str] = None
    metodo07: Optional[str] = None
    ensayo08: Optional[str] = None
    unidades08: Optional[str] = None
    metodo08: Optional[str] = None
    ensayo09: Optional[str] = None
    unidades09: Optional[str] = None
    metodo09: Optional[str] = None
    ensayo10: Optional[str] = None
    unidades10: Optional[str] = None
    metodo10: Optional[str] = None
    ensayo11: Optional[str] = None
    unidades11: Optional[str] = None
    metodo11: Optional[str] = None
    ensayo12: Optional[str] = None
    unidades12: Optional[str] = None
    metodo12: Optional[str] = None
    ensayo13: Optional[str] = None
    unidades13: Optional[str] = None
    metodo13: Optional[str] = None
    ensayo14: Optional[str] = None
    unidades14: Optional[str] = None
    metodo14: Optional[str] = None
    ensayo15: Optional[str] = None
    unidades15: Optional[str] = None
    metodo15: Optional[str] = None
    ensayo16: Optional[str] = None
    unidades16: Optional[str] = None
    metodo16: Optional[str] = None
    ensayo17: Optional[str] = None
    unidades17: Optional[str] = None
    metodo17: Optional[str] = None
    ensayo18: Optional[str] = None
    unidades18: Optional[str] = None
    metodo18: Optional[str] = None
    ensayo19: Optional[str] = None
    unidades19: Optional[str] = None
    metodo19: Optional[str] = None
    ensayo20: Optional[str] = None
    unidades20: Optional[str] = None
    metodo20: Optional[str] = None
    ensayo21: Optional[str] = None
    unidades21: Optional[str] = None
    metodo21: Optional[str] = None
    ensayo22: Optional[str] = None
    unidades22: Optional[str] = None
    metodo22: Optional[str] = None
    ensayo23: Optional[str] = None
    unidades23: Optional[str] = None
    metodo23: Optional[str] = None
    ensayo24: Optional[str] = None
    unidades24: Optional[str] = None
    metodo24: Optional[str] = None
    ensayo25: Optional[str] = None
    unidades25: Optional[str] = None
    metodo25: Optional[str] = None
    cod_cliente: Optional[str] = None
    # trial827: Optional[str] = None

class PC_RE_MUCreate(PC_RE_MUBase): pass
class PC_RE_MUUpdate(PC_RE_MUBase): pass
class PC_RE_MU(PC_RE_MUBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PC_RE_OFBase(BaseModel):
    fecha: Optional[datetime] = None
    revisado_por: Optional[str] = None
    informacion_por_revisar: Optional[str] = None
    revision: Optional[str] = None
    informacion_revisada: Optional[str] = None
    # trial827: Optional[str] = None

class PC_RE_OFCreate(PC_RE_OFBase): pass
class PC_RE_OFUpdate(PC_RE_OFBase): pass
class PC_RE_OF(PC_RE_OFBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PC_RE_PIBase(BaseModel):
    id_pr: Optional[int] = None
    tipo_de_muestra: Optional[str] = None
    servicio: Optional[int] = None
    metodo: Optional[str] = None
    precio: Optional[float] = None
    cantidad: Optional[int] = None
    precio_total: Optional[float] = None
    # trial827: Optional[str] = None

class PC_RE_PICreate(PC_RE_PIBase): pass
class PC_RE_PIUpdate(PC_RE_PIBase): pass
class PC_RE_PI(PC_RE_PIBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PC_RE_PRBase(BaseModel):
    area: Optional[str] = None
    registro: Optional[str] = None
    registrado_por: Optional[str] = None
    fecha: Optional[datetime] = None
    hora: Optional[datetime] = None
    cliente: Optional[str] = None
    solicitante: Optional[str] = None
    subtotal: Optional[float] = None
    nro_muestras: Optional[int] = None
    porcentaje_de_descuento: Optional[float] = None
    descuento: Optional[float] = None
    total_a_cancelar: Optional[float] = None
    tiempo_de_entrega: Optional[int] = None
    comentarios_observaciones: Optional[str] = None
    factura: Optional[str] = None
    fecha_de_factura: Optional[datetime] = None
    forma_de_pago: Optional[str] = None
    pago: Optional[str] = None
    valido_hasta: Optional[datetime] = None
    cantidad_minima_requerida: Optional[str] = None
    condiciones_de_la_muestra: Optional[str] = None
    # trial824: Optional[str] = None

class PC_RE_PRCreate(PC_RE_PRBase): pass
class PC_RE_PRUpdate(PC_RE_PRBase): pass
class PC_RE_PR(PC_RE_PRBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PC_RE_SEBase(BaseModel):
    area: Optional[str] = None
    servicio: Optional[str] = None
    metodo: Optional[str] = None
    unidades: Optional[str] = None
    precio: Optional[float] = None
    comentario: Optional[str] = None
    # trial824: Optional[str] = None

class PC_RE_SECreate(PC_RE_SEBase): pass
class PC_RE_SEUpdate(PC_RE_SEBase): pass
class PC_RE_SE(PC_RE_SEBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PC_RE_SGBase(BaseModel):
    servicio_global: Optional[str] = None
    area: Optional[str] = None
    # trial824: Optional[str] = None

class PC_RE_SGCreate(PC_RE_SGBase): pass
class PC_RE_SGUpdate(PC_RE_SGBase): pass
class PC_RE_SG(PC_RE_SGBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PC_RE_SHBase(BaseModel):
    id_sg: Optional[int] = None
    servicio: Optional[int] = None
    # trial827: Optional[str] = None

class PC_RE_SHCreate(PC_RE_SHBase): pass
class PC_RE_SHUpdate(PC_RE_SHBase): pass
class PC_RE_SH(PC_RE_SHBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PC_RE_SOBase(BaseModel):
    fecha: Optional[datetime] = None
    revisado_por: Optional[str] = None
    informacion_por_revisar: Optional[str] = None
    revision: Optional[str] = None
    informacion_revisada: Optional[str] = None
    # trial827: Optional[str] = None

class PC_RE_SOCreate(PC_RE_SOBase): pass
class PC_RE_SOUpdate(PC_RE_SOBase): pass
class PC_RE_SO(PC_RE_SOBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PC_TC_TCBase(BaseModel):
    registrado_por: Optional[str] = None
    fecha: Optional[datetime] = None
    area_de_tnc: Optional[str] = None
    servicio: Optional[str] = None
    descripcion: Optional[str] = None
    detencion: Optional[bool] = None
    retencion_de_informes: Optional[bool] = None
    porque: Optional[str] = None
    tipo_de_tnc: Optional[str] = None
    accion: Optional[str] = None
    responsable_de_reanudacion_del_trabajo: Optional[str] = None
    autorizacion_de_reanudacion: Optional[bool] = None
    se_puede_repetir: Optional[bool] = None
    repetici_n_del_tnc: Optional[bool] = None
    abrir_otro_tnc: Optional[bool] = None
    comunicacion_al_cliente: Optional[bool] = None
    comunicacion_realizada_al_cliente: Optional[str] = None
    decision_del_cliente: Optional[str] = None
    el_trabajo_se_acepta: Optional[bool] = None
    anulacion_del_trabajo: Optional[bool] = None
    requiere_accion_correctiva: Optional[bool] = None
    observaciones: Optional[str] = None
    cierre_tcnc: Optional[bool] = None
    # trial827: Optional[str] = None

class PC_TC_TCCreate(PC_TC_TCBase): pass
class PC_TC_TCUpdate(PC_TC_TCBase): pass
class PC_TC_TC(PC_TC_TCBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PE_PL_ACBase(BaseModel):
    id: Optional[int] = None
    riesgo_oportunidad: Optional[int] = None
    correciones: Optional[int] = None
    acciones_correctivas: Optional[int] = None
    acciones_de_mejora: Optional[int] = None
    acciones_abordar: Optional[str] = None
    responsable_actividades: Optional[str] = None
    recursos: Optional[str] = None
    fecha_frecuencia_actividad: Optional[datetime] = None
    resultado_esperado: Optional[str] = None
    fecha_seguimiento: Optional[datetime] = None
    responsable_seguimiento: Optional[str] = None
    probabilidadrev: Optional[int] = None
    impactorev: Optional[int] = None
    valorrev: Optional[int] = None
    conclusi_n_seguimiento: Optional[str] = None
    realizado: Optional[bool] = None
    # trial827: Optional[str] = None

class PE_PL_ACCreate(PE_PL_ACBase): pass
class PE_PL_ACUpdate(PE_PL_ACBase): pass
class PE_PL_AC(PE_PL_ACBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PE_PL_COBase(BaseModel):
    id: Optional[int] = None
    registrado_por: Optional[str] = None
    fecha: Optional[datetime] = None
    contexto: Optional[str] = None
    tipo: Optional[str] = None
    descripci_n: Optional[str] = None
    vigente: Optional[bool] = None
    # trial827: Optional[str] = None

class PE_PL_COCreate(PE_PL_COBase): pass
class PE_PL_COUpdate(PE_PL_COBase): pass
class PE_PL_CO(PE_PL_COBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PE_PL_ESBase(BaseModel):
    id: Optional[int] = None
    registrado_por: Optional[str] = None
    fecha: Optional[datetime] = None
    contexto_interno: Optional[int] = None
    contexto_externo: Optional[int] = None
    estrategia: Optional[str] = None
    comentario: Optional[str] = None
    vigente: Optional[bool] = None
    # trial827: Optional[str] = None

class PE_PL_ESCreate(PE_PL_ESBase): pass
class PE_PL_ESUpdate(PE_PL_ESBase): pass
class PE_PL_ES(PE_PL_ESBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PE_PL_OBBase(BaseModel):
    id: Optional[int] = None
    estrategia_1: Optional[int] = None
    estrategia_2: Optional[int] = None
    estrategia_3: Optional[int] = None
    estrategia_4: Optional[int] = None
    registrado_por: Optional[str] = None
    fecha: Optional[datetime] = None
    objetivo: Optional[str] = None
    indicador: Optional[str] = None
    meta: Optional[str] = None
    tiempo: Optional[str] = None
    propietario: Optional[str] = None
    vigente: Optional[bool] = None
    comentarios: Optional[str] = None
    # trial827: Optional[str] = None

class PE_PL_OBCreate(PE_PL_OBBase): pass
class PE_PL_OBUpdate(PE_PL_OBBase): pass
class PE_PL_OB(PE_PL_OBBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PE_PL_PCBase(BaseModel):
    id: Optional[int] = None
    responsable: Optional[str] = None
    fecha: Optional[datetime] = None
    riesgo_oportunidad: Optional[int] = None
    actividad_contingecia: Optional[str] = None
    responsable_contingencia: Optional[str] = None
    vigente: Optional[bool] = None
    comentario: Optional[str] = None
    # trial827: Optional[str] = None

class PE_PL_PCCreate(PE_PL_PCBase): pass
class PE_PL_PCUpdate(PE_PL_PCBase): pass
class PE_PL_PC(PE_PL_PCBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PE_PL_PIBase(BaseModel):
    id: Optional[int] = None
    registrado_por: Optional[str] = None
    fecha: Optional[datetime] = None
    tipo: Optional[str] = None
    parte_interesada: Optional[str] = None
    requisito1: Optional[str] = None
    requisito2: Optional[str] = None
    requisito3: Optional[str] = None
    requisito4: Optional[str] = None
    descripcion_de_la_relacion: Optional[str] = None
    vigente: Optional[bool] = None
    # trial827: Optional[str] = None

class PE_PL_PICreate(PE_PL_PIBase): pass
class PE_PL_PIUpdate(PE_PL_PIBase): pass
class PE_PL_PI(PE_PL_PIBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PE_PL_PLBase(BaseModel):
    id: Optional[int] = None
    objetivo: Optional[int] = None
    actividad: Optional[str] = None
    recursos: Optional[str] = None
    plazo: Optional[datetime] = None
    resultado_esperado: Optional[str] = None
    responsable_seguimiento: Optional[str] = None
    comentarios_observaciones: Optional[str] = None
    cumplido: Optional[bool] = None
    # trial827: Optional[str] = None

class PE_PL_PLCreate(PE_PL_PLBase): pass
class PE_PL_PLUpdate(PE_PL_PLBase): pass
class PE_PL_PL(PE_PL_PLBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PE_PL_ROBase(BaseModel):
    actividad_de_planificacion: Optional[int] = None
    registrado_por: Optional[str] = None
    fecha: Optional[datetime] = None
    evento: Optional[str] = None
    consecuencia: Optional[str] = None
    riesgo_oportunidad: Optional[str] = None
    ctrl_existente: Optional[str] = None
    probabilidad: Optional[int] = None
    impacto: Optional[int] = None
    valor_de_riesgo: Optional[int] = None
    comentario: Optional[str] = None
    vigente: Optional[bool] = None
    abordaje: Optional[bool] = None
    probabilidad_rev: Optional[int] = None
    impacto_rev: Optional[int] = None
    valor_de_riesgo_rev: Optional[int] = None
    eficacia_de_acciones: Optional[str] = None
    conclusion_de_seguimiento: Optional[str] = None
    # trial827: Optional[str] = None

class PE_PL_ROCreate(PE_PL_ROBase): pass
class PE_PL_ROUpdate(PE_PL_ROBase): pass
class PE_PL_RO(PE_PL_ROBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PE_SE_ACBase(BaseModel):
    id: Optional[int] = None
    fecha_registro: Optional[datetime] = None
    registrado_por: Optional[str] = None
    descripcion_de_la_no_conformidad: Optional[str] = None
    evidencia: Optional[str] = None
    requisito_o_criterio_implicado: Optional[str] = None
    analisis_de_la_no_conformidad: Optional[str] = None
    por_qu_1: Optional[str] = None
    por_qu_2: Optional[str] = None
    por_qu_3: Optional[str] = None
    por_qu_4: Optional[str] = None
    por_qu_5: Optional[str] = None
    no_conformidad_similar_o_potencial: Optional[str] = None
    causa: Optional[str] = None
    responsable_de_seguimiento: Optional[str] = None
    fecha_de_seguimiento_de_eficacia_de_acciones: Optional[datetime] = None
    efecto_deseado: Optional[str] = None
    seguimiento: Optional[str] = None
    eficaz: Optional[bool] = None
    fecha_seguimiento: Optional[datetime] = None
    observaciones: Optional[str] = None
    cerrado: Optional[bool] = None
    # trial827: Optional[str] = None

class PE_SE_ACCreate(PE_SE_ACBase): pass
class PE_SE_ACUpdate(PE_SE_ACBase): pass
class PE_SE_AC(PE_SE_ACBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PE_SE_CABase(BaseModel):
    id: Optional[int] = None
    acciones_correctivas: Optional[int] = None
    acciones_abordar: Optional[str] = None
    responsable_actividades: Optional[str] = None
    recursos: Optional[str] = None
    fecha_frecuencia_actividad: Optional[datetime] = None
    resultado_esperado: Optional[str] = None
    fecha_seguimiento: Optional[datetime] = None
    responsable_seguimiento: Optional[str] = None
    conclusi_n_seguimiento: Optional[str] = None
    realizado: Optional[bool] = None
    # trial827: Optional[str] = None

class PE_SE_CACreate(PE_SE_CABase): pass
class PE_SE_CAUpdate(PE_SE_CABase): pass
class PE_SE_CA(PE_SE_CABase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PE_SE_COBase(BaseModel):
    id: Optional[int] = None
    correcciones: Optional[int] = None
    acciones_abordar: Optional[str] = None
    responsable_actividades: Optional[str] = None
    recursos: Optional[str] = None
    fecha_frecuencia_actividad: Optional[datetime] = None
    resultado_esperado: Optional[str] = None
    fecha_seguimiento: Optional[datetime] = None
    responsable_seguimiento: Optional[str] = None
    conclusi_n_seguimiento: Optional[str] = None
    realizado: Optional[bool] = None
    # trial827: Optional[str] = None

class PE_SE_COCreate(PE_SE_COBase): pass
class PE_SE_COUpdate(PE_SE_COBase): pass
class PE_SE_CO(PE_SE_COBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PE_SE_EEBase(BaseModel):
    entradas: Optional[str] = None
    # trial827: Optional[str] = None

class PE_SE_EECreate(PE_SE_EEBase): pass
class PE_SE_EEUpdate(PE_SE_EEBase): pass
class PE_SE_EE(PE_SE_EEBase):
    model_config = ConfigDict(from_attributes=True)

class PE_SE_ENBase(BaseModel):
    id: Optional[int] = None
    id_re: Optional[int] = None
    entrada: Optional[str] = None
    fuente: Optional[str] = None
    link: Optional[str] = None
    conveniencia: Optional[str] = None
    conveniente: Optional[bool] = None
    adecuaci_n: Optional[str] = None
    adecuado: Optional[bool] = None
    eficacia: Optional[str] = None
    eficaz: Optional[bool] = None
    # trial827: Optional[str] = None

class PE_SE_ENCreate(PE_SE_ENBase): pass
class PE_SE_ENUpdate(PE_SE_ENBase): pass
class PE_SE_EN(PE_SE_ENBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PE_SE_MABase(BaseModel):
    id: Optional[int] = None
    acciones_de_mejora: Optional[int] = None
    acciones_abordar: Optional[str] = None
    responsable_actividades: Optional[str] = None
    recursos: Optional[str] = None
    fecha_frecuencia_actividad: Optional[datetime] = None
    resultado_esperado: Optional[str] = None
    fecha_seguimiento: Optional[datetime] = None
    responsable_seguimiento: Optional[str] = None
    conclusi_n_seguimiento: Optional[str] = None
    realizado: Optional[bool] = None
    # trial827: Optional[str] = None

class PE_SE_MACreate(PE_SE_MABase): pass
class PE_SE_MAUpdate(PE_SE_MABase): pass
class PE_SE_MA(PE_SE_MABase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PE_SE_MEBase(BaseModel):
    fecha_registro: Optional[datetime] = None
    registrado_por: Optional[str] = None
    oportunidad_de_mejora: Optional[str] = None
    descripcion_de_oportunidad_de_mejora: Optional[str] = None
    analisis_de_la_oportunidad_de_mejora: Optional[str] = None
    oportunidad_de_mejora_seleccionada: Optional[bool] = None
    responsable_de_seguimiento: Optional[str] = None
    fecha_de_seguimiento_de_eficacia_de_acciones: Optional[datetime] = None
    efecto_deseado: Optional[str] = None
    seguimiento: Optional[str] = None
    eficaz: Optional[bool] = None
    fecha_seguimiento: Optional[datetime] = None
    observaciones: Optional[str] = None
    cerrado: Optional[bool] = None
    # trial827: Optional[str] = None

class PE_SE_MECreate(PE_SE_MEBase): pass
class PE_SE_MEUpdate(PE_SE_MEBase): pass
class PE_SE_ME(PE_SE_MEBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PE_SE_REBase(BaseModel):
    participante_1: Optional[str] = None
    participante_2: Optional[str] = None
    participante_3: Optional[str] = None
    participante_4: Optional[str] = None
    participante_5: Optional[str] = None
    participante_6: Optional[str] = None
    participante_7: Optional[str] = None
    participante_8: Optional[str] = None
    fecha: Optional[datetime] = None
    medio_de_reuni_n: Optional[str] = None
    tipo_de_revisi_n: Optional[str] = None
    comentarios_y_observaciones: Optional[str] = None
    # trial827: Optional[str] = None

class PE_SE_RECreate(PE_SE_REBase): pass
class PE_SE_REUpdate(PE_SE_REBase): pass
class PE_SE_RE(PE_SE_REBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PE_SE_SABase(BaseModel):
    id: Optional[int] = None
    id_re: Optional[int] = None
    salida: Optional[str] = None
    decisi_n: Optional[str] = None
    acciones: Optional[str] = None
    # trial827: Optional[str] = None

class PE_SE_SACreate(PE_SE_SABase): pass
class PE_SE_SAUpdate(PE_SE_SABase): pass
class PE_SE_SA(PE_SE_SABase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PE_SE_SSBase(BaseModel):
    salidas: Optional[str] = None
    # trial827: Optional[str] = None

class PE_SE_SSCreate(PE_SE_SSBase): pass
class PE_SE_SSUpdate(PE_SE_SSBase): pass
class PE_SE_SS(PE_SE_SSBase):
    model_config = ConfigDict(from_attributes=True)

class SYS_FACTORESKBase(BaseModel):
    descripcion: Optional[str] = None
    factor: Optional[float] = None
    # trial830: Optional[str] = None

class SYS_FACTORESKCreate(SYS_FACTORESKBase): pass
class SYS_FACTORESKUpdate(SYS_FACTORESKBase): pass
class SYS_FACTORESK(SYS_FACTORESKBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class TBL_LUGARESBase(BaseModel):
    ciudad: Optional[str] = None
    departamento: Optional[str] = None
    altitud: Optional[int] = None
    presionref_hpa: Optional[int] = None
    humedadref_pct: Optional[int] = None
    prioridad: Optional[int] = None
    # trial830: Optional[str] = None

class TBL_LUGARESCreate(TBL_LUGARESBase): pass
class TBL_LUGARESUpdate(TBL_LUGARESBase): pass
class TBL_LUGARES(TBL_LUGARESBase):
    lugarid: int
    model_config = ConfigDict(from_attributes=True)

class TBL_POSICIONES_HORNOBase(BaseModel):
    clasedeequipo: Optional[str] = None
    nombreposicion: Optional[str] = None
    # trial830: Optional[str] = None

class TBL_POSICIONES_HORNOCreate(TBL_POSICIONES_HORNOBase): pass
class TBL_POSICIONES_HORNOUpdate(TBL_POSICIONES_HORNOBase): pass
class TBL_POSICIONES_HORNO(TBL_POSICIONES_HORNOBase):
    posicionid: int
    model_config = ConfigDict(from_attributes=True)



# Export all schemas
__all__ = [
    "PA_DI_FABase",
    "PA_DI_FACreate",
    "PA_DI_FAUpdate",
    "PA_DI_FA",
    "PA_DI_PRBase",
    "PA_DI_PRCreate",
    "PA_DI_PRUpdate",
    "PA_DI_PR",
    "PA_DI_RABase",
    "PA_DI_RACreate",
    "PA_DI_RAUpdate",
    "PA_DI_RA",
    "PA_EQ_ACBase",
    "PA_EQ_ACCreate",
    "PA_EQ_ACUpdate",
    "PA_EQ_AC",
    "PA_EQ_CABase",
    "PA_EQ_CACreate",
    "PA_EQ_CAUpdate",
    "PA_EQ_CA",
    "PA_EQ_CBBase",
    "PA_EQ_CBCreate",
    "PA_EQ_CBUpdate",
    "PA_EQ_CB",
    "PA_EQ_CHBase",
    "PA_EQ_CHCreate",
    "PA_EQ_CHUpdate",
    "PA_EQ_CH",
    "PA_EQ_CIBase",
    "PA_EQ_CICreate",
    "PA_EQ_CIUpdate",
    "PA_EQ_CI",
    "PA_EQ_CVBase",
    "PA_EQ_CVCreate",
    "PA_EQ_CVUpdate",
    "PA_EQ_CV",
    "PA_EQ_DCBase",
    "PA_EQ_DCCreate",
    "PA_EQ_DCUpdate",
    "PA_EQ_DC",
    "PA_EQ_EQBase",
    "PA_EQ_EQCreate",
    "PA_EQ_EQUpdate",
    "PA_EQ_EQ",
    "PA_EQ_EXBase",
    "PA_EQ_EXCreate",
    "PA_EQ_EXUpdate",
    "PA_EQ_EX",
    "PA_EQ_HMBase",
    "PA_EQ_HMCreate",
    "PA_EQ_HMUpdate",
    "PA_EQ_HM",
    "PA_EQ_LEBase",
    "PA_EQ_LECreate",
    "PA_EQ_LEUpdate",
    "PA_EQ_LE",
    "PA_EQ_MABase",
    "PA_EQ_MACreate",
    "PA_EQ_MAUpdate",
    "PA_EQ_MA",
    "PA_EQ_MOBase",
    "PA_EQ_MOCreate",
    "PA_EQ_MOUpdate",
    "PA_EQ_MO",
    "PA_EQ_MRBase",
    "PA_EQ_MRCreate",
    "PA_EQ_MRUpdate",
    "PA_EQ_MR",
    "PA_EQ_MVBase",
    "PA_EQ_MVCreate",
    "PA_EQ_MVUpdate",
    "PA_EQ_MV",
    "PA_EQ_PABase",
    "PA_EQ_PACreate",
    "PA_EQ_PAUpdate",
    "PA_EQ_PA",
    "PA_EQ_PRBase",
    "PA_EQ_PRCreate",
    "PA_EQ_PRUpdate",
    "PA_EQ_PR",
    "PA_EQ_REBase",
    "PA_EQ_RECreate",
    "PA_EQ_REUpdate",
    "PA_EQ_RE",
    "PA_EQ_RPBase",
    "PA_EQ_RPCreate",
    "PA_EQ_RPUpdate",
    "PA_EQ_RP",
    "PA_EQ_VEBase",
    "PA_EQ_VECreate",
    "PA_EQ_VEUpdate",
    "PA_EQ_VE",
    "PA_IA_AHBase",
    "PA_IA_AHCreate",
    "PA_IA_AHUpdate",
    "PA_IA_AH",
    "PA_IA_AMBase",
    "PA_IA_AMCreate",
    "PA_IA_AMUpdate",
    "PA_IA_AM",
    "PA_IA_ARBase",
    "PA_IA_ARCreate",
    "PA_IA_ARUpdate",
    "PA_IA_AR",
    "PA_IA_CABase",
    "PA_IA_CACreate",
    "PA_IA_CAUpdate",
    "PA_IA_CA",
    "PA_IA_LEBase",
    "PA_IA_LECreate",
    "PA_IA_LEUpdate",
    "PA_IA_LE",
    "PA_IA_LIBase",
    "PA_IA_LICreate",
    "PA_IA_LIUpdate",
    "PA_IA_LI",
    "PA_IA_RABase",
    "PA_IA_RACreate",
    "PA_IA_RAUpdate",
    "PA_IA_RA",
    "PA_IA_RIBase",
    "PA_IA_RICreate",
    "PA_IA_RIUpdate",
    "PA_IA_RI",
    "PA_IA_SABase",
    "PA_IA_SACreate",
    "PA_IA_SAUpdate",
    "PA_IA_SA",
    "PA_IA_SIBase",
    "PA_IA_SICreate",
    "PA_IA_SIUpdate",
    "PA_IA_SI",
    "PA_PE_AUBase",
    "PA_PE_AUCreate",
    "PA_PE_AUUpdate",
    "PA_PE_AU",
    "PA_PE_CVBase",
    "PA_PE_CVCreate",
    "PA_PE_CVUpdate",
    "PA_PE_CV",
    "PA_PE_DEBase",
    "PA_PE_DECreate",
    "PA_PE_DEUpdate",
    "PA_PE_DE",
    "PA_PE_ECBase",
    "PA_PE_ECCreate",
    "PA_PE_ECUpdate",
    "PA_PE_EC",
    "PA_PE_EFBase",
    "PA_PE_EFCreate",
    "PA_PE_EFUpdate",
    "PA_PE_EF",
    "PA_PE_FGBase",
    "PA_PE_FGCreate",
    "PA_PE_FGUpdate",
    "PA_PE_FG",
    "PA_PE_IEBase",
    "PA_PE_IECreate",
    "PA_PE_IEUpdate",
    "PA_PE_IE",
    "PA_PE_ISBase",
    "PA_PE_ISCreate",
    "PA_PE_ISUpdate",
    "PA_PE_IS",
    "PA_PE_PEBase",
    "PA_PE_PECreate",
    "PA_PE_PEUpdate",
    "PA_PE_PE",
    "PA_PE_PLBase",
    "PA_PE_PLCreate",
    "PA_PE_PLUpdate",
    "PA_PE_PL",
    "PA_PE_POBase",
    "PA_PE_POCreate",
    "PA_PE_POUpdate",
    "PA_PE_PO",
    "PA_PE_PRBase",
    "PA_PE_PRCreate",
    "PA_PE_PRUpdate",
    "PA_PE_PR",
    "PA_PE_RQBase",
    "PA_PE_RQCreate",
    "PA_PE_RQUpdate",
    "PA_PE_RQ",
    "PA_PE_SEBase",
    "PA_PE_SECreate",
    "PA_PE_SEUpdate",
    "PA_PE_SE",
    "PA_PE_SPBase",
    "PA_PE_SPCreate",
    "PA_PE_SPUpdate",
    "PA_PE_SP",
    "PA_PE_SUBase",
    "PA_PE_SUCreate",
    "PA_PE_SUUpdate",
    "PA_PE_SU",
    "PA_PE_TPBase",
    "PA_PE_TPCreate",
    "PA_PE_TPUpdate",
    "PA_PE_TP",
    "PA_PS_ADBase",
    "PA_PS_ADCreate",
    "PA_PS_ADUpdate",
    "PA_PS_AD",
    "PA_PS_CRBase",
    "PA_PS_CRCreate",
    "PA_PS_CRUpdate",
    "PA_PS_CR",
    "PA_PS_DEBase",
    "PA_PS_DECreate",
    "PA_PS_DEUpdate",
    "PA_PS_DE",
    "PA_PS_EVBase",
    "PA_PS_EVCreate",
    "PA_PS_EVUpdate",
    "PA_PS_EV",
    "PA_PS_OSBase",
    "PA_PS_OSCreate",
    "PA_PS_OSUpdate",
    "PA_PS_OS",
    "PA_PS_PRBase",
    "PA_PS_PRCreate",
    "PA_PS_PRUpdate",
    "PA_PS_PR",
    "PA_PS_PSBase",
    "PA_PS_PSCreate",
    "PA_PS_PSUpdate",
    "PA_PS_PS",
    "PC_ES_ESBase",
    "PC_ES_ESCreate",
    "PC_ES_ESUpdate",
    "PC_ES_ES",
    "PC_LAB_PATRONESBase",
    "PC_LAB_PATRONESCreate",
    "PC_LAB_PATRONESUpdate",
    "PC_LAB_PATRONES",
    "PC_LAB_SOLUCIONESBase",
    "PC_LAB_SOLUCIONESCreate",
    "PC_LAB_SOLUCIONESUpdate",
    "PC_LAB_SOLUCIONES",
    "PC_LAB_SOLUCIONES_DETBase",
    "PC_LAB_SOLUCIONES_DETCreate",
    "PC_LAB_SOLUCIONES_DETUpdate",
    "PC_LAB_SOLUCIONES_DET",
    "PC_LAB_VALIDACIONMETODOSBase",
    "PC_LAB_VALIDACIONMETODOSCreate",
    "PC_LAB_VALIDACIONMETODOSUpdate",
    "PC_LAB_VALIDACIONMETODOS",
    "PC_QR_QUBase",
    "PC_QR_QUCreate",
    "PC_QR_QUUpdate",
    "PC_QR_QU",
    "PC_RE_ACBase",
    "PC_RE_ACCreate",
    "PC_RE_ACUpdate",
    "PC_RE_AC",
    "PC_RE_ANALISISBase",
    "PC_RE_ANALISISCreate",
    "PC_RE_ANALISISUpdate",
    "PC_RE_ANALISIS",
    "PC_RE_CCBase",
    "PC_RE_CCCreate",
    "PC_RE_CCUpdate",
    "PC_RE_CC",
    "PC_RE_CLBase",
    "PC_RE_CLCreate",
    "PC_RE_CLUpdate",
    "PC_RE_CL",
    "PC_RE_COBase",
    "PC_RE_COCreate",
    "PC_RE_COUpdate",
    "PC_RE_CO",
    "PC_RE_MUBase",
    "PC_RE_MUCreate",
    "PC_RE_MUUpdate",
    "PC_RE_MU",
    "PC_RE_OFBase",
    "PC_RE_OFCreate",
    "PC_RE_OFUpdate",
    "PC_RE_OF",
    "PC_RE_PIBase",
    "PC_RE_PICreate",
    "PC_RE_PIUpdate",
    "PC_RE_PI",
    "PC_RE_PRBase",
    "PC_RE_PRCreate",
    "PC_RE_PRUpdate",
    "PC_RE_PR",
    "PC_RE_SEBase",
    "PC_RE_SECreate",
    "PC_RE_SEUpdate",
    "PC_RE_SE",
    "PC_RE_SGBase",
    "PC_RE_SGCreate",
    "PC_RE_SGUpdate",
    "PC_RE_SG",
    "PC_RE_SHBase",
    "PC_RE_SHCreate",
    "PC_RE_SHUpdate",
    "PC_RE_SH",
    "PC_RE_SOBase",
    "PC_RE_SOCreate",
    "PC_RE_SOUpdate",
    "PC_RE_SO",
    "PC_TC_TCBase",
    "PC_TC_TCCreate",
    "PC_TC_TCUpdate",
    "PC_TC_TC",
    "PE_PL_ACBase",
    "PE_PL_ACCreate",
    "PE_PL_ACUpdate",
    "PE_PL_AC",
    "PE_PL_COBase",
    "PE_PL_COCreate",
    "PE_PL_COUpdate",
    "PE_PL_CO",
    "PE_PL_ESBase",
    "PE_PL_ESCreate",
    "PE_PL_ESUpdate",
    "PE_PL_ES",
    "PE_PL_OBBase",
    "PE_PL_OBCreate",
    "PE_PL_OBUpdate",
    "PE_PL_OB",
    "PE_PL_PCBase",
    "PE_PL_PCCreate",
    "PE_PL_PCUpdate",
    "PE_PL_PC",
    "PE_PL_PIBase",
    "PE_PL_PICreate",
    "PE_PL_PIUpdate",
    "PE_PL_PI",
    "PE_PL_PLBase",
    "PE_PL_PLCreate",
    "PE_PL_PLUpdate",
    "PE_PL_PL",
    "PE_PL_ROBase",
    "PE_PL_ROCreate",
    "PE_PL_ROUpdate",
    "PE_PL_RO",
    "PE_SE_ACBase",
    "PE_SE_ACCreate",
    "PE_SE_ACUpdate",
    "PE_SE_AC",
    "PE_SE_CABase",
    "PE_SE_CACreate",
    "PE_SE_CAUpdate",
    "PE_SE_CA",
    "PE_SE_COBase",
    "PE_SE_COCreate",
    "PE_SE_COUpdate",
    "PE_SE_CO",
    "PE_SE_EEBase",
    "PE_SE_EECreate",
    "PE_SE_EEUpdate",
    "PE_SE_EE",
    "PE_SE_ENBase",
    "PE_SE_ENCreate",
    "PE_SE_ENUpdate",
    "PE_SE_EN",
    "PE_SE_MABase",
    "PE_SE_MACreate",
    "PE_SE_MAUpdate",
    "PE_SE_MA",
    "PE_SE_MEBase",
    "PE_SE_MECreate",
    "PE_SE_MEUpdate",
    "PE_SE_ME",
    "PE_SE_REBase",
    "PE_SE_RECreate",
    "PE_SE_REUpdate",
    "PE_SE_RE",
    "PE_SE_SABase",
    "PE_SE_SACreate",
    "PE_SE_SAUpdate",
    "PE_SE_SA",
    "PE_SE_SSBase",
    "PE_SE_SSCreate",
    "PE_SE_SSUpdate",
    "PE_SE_SS",
    "SYS_FACTORESKBase",
    "SYS_FACTORESKCreate",
    "SYS_FACTORESKUpdate",
    "SYS_FACTORESK",
    "TBL_LUGARESBase",
    "TBL_LUGARESCreate",
    "TBL_LUGARESUpdate",
    "TBL_LUGARES",
    "TBL_POSICIONES_HORNOBase",
    "TBL_POSICIONES_HORNOCreate",
    "TBL_POSICIONES_HORNOUpdate",
    "TBL_POSICIONES_HORNO"
]
