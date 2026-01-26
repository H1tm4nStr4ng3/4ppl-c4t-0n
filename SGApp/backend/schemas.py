from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class PA_DI_FABase(BaseModel):
    registrado_por: Optional[str] = None
    fecha: Optional[datetime] = None
    evento: Optional[str] = None
    resuelto: Optional[bool] = None
    trial814: Optional[str] = None

class PA_DI_FACreate(PA_DI_FABase): pass
class PA_DI_FAUpdate(PA_DI_FABase): pass
class PA_DI_FA(PA_DI_FABase):
    id: int
    class Config: from_attributes = True

class PA_DI_PRBase(BaseModel):
    codigo_del_proceso: Optional[str] = None
    proceso: Optional[str] = None
    vigente: Optional[bool] = None
    trial814: Optional[str] = None

class PA_DI_PRCreate(PA_DI_PRBase): pass
class PA_DI_PRUpdate(PA_DI_PRBase): pass
class PA_DI_PR(PA_DI_PRBase):
    id: int
    class Config: from_attributes = True

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
    trial814: Optional[str] = None

class PA_DI_RACreate(PA_DI_RABase): pass
class PA_DI_RAUpdate(PA_DI_RABase): pass
class PA_DI_RA(PA_DI_RABase):
    id: int
    class Config: from_attributes = True

class PA_EQ_ACBase(BaseModel):
    actividad: Optional[str] = None
    descripcion: Optional[str] = None
    trial814: Optional[str] = None

class PA_EQ_ACCreate(PA_EQ_ACBase): pass
class PA_EQ_ACUpdate(PA_EQ_ACBase): pass
class PA_EQ_AC(PA_EQ_ACBase):
    id: int
    class Config: from_attributes = True

class PA_EQ_CABase(BaseModel):
    registrado_por: Optional[str] = None
    fecha: Optional[datetime] = None
    equipamiento: Optional[str] = None
    certificado: Optional[str] = None
    ente_calibrador: Optional[str] = None
    fecha_de_calibracion: Optional[datetime] = None
    unidades: Optional[str] = None
    observaciones: Optional[str] = None
    apto: Optional[bool] = None
    regla: Optional[str] = None
    trial814: Optional[str] = None

class PA_EQ_CACreate(PA_EQ_CABase): pass
class PA_EQ_CAUpdate(PA_EQ_CABase): pass
class PA_EQ_CA(PA_EQ_CABase):
    id_equi: int
    class Config: from_attributes = True

class PA_EQ_CBBase(BaseModel):
    id_ci: Optional[int] = None
    tipoprueba: Optional[str] = None
    pesapatron_id: Optional[str] = None
    posicion: Optional[str] = None
    lectura_balanza: Optional[float] = None
    lectura_corregida: Optional[float] = None
    trial814: Optional[str] = None

class PA_EQ_CBCreate(PA_EQ_CBBase): pass
class PA_EQ_CBUpdate(PA_EQ_CBBase): pass
class PA_EQ_CB(PA_EQ_CBBase):
    id: int
    class Config: from_attributes = True

class PA_EQ_CHBase(BaseModel):
    id_ci: Optional[int] = None
    posicion: Optional[str] = None
    temppatron_leida: Optional[float] = None
    tempequipo_leida: Optional[float] = None
    diferencia: Optional[float] = None
    resultadopunto: Optional[str] = None
    trial814: Optional[str] = None

class PA_EQ_CHCreate(PA_EQ_CHBase): pass
class PA_EQ_CHUpdate(PA_EQ_CHBase): pass
class PA_EQ_CH(PA_EQ_CHBase):
    id: int
    class Config: from_attributes = True

class PA_EQ_CIBase(BaseModel):
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
    trial814: Optional[str] = None

class PA_EQ_CICreate(PA_EQ_CIBase): pass
class PA_EQ_CIUpdate(PA_EQ_CIBase): pass
class PA_EQ_CI(PA_EQ_CIBase):
    id_equi: int
    class Config: from_attributes = True

class PA_EQ_CVBase(BaseModel):
    id_ci: Optional[int] = None
    matraz_vacio: Optional[float] = None
    corr1: Optional[float] = None
    matraz_lleno: Optional[float] = None
    corr2: Optional[float] = None
    masa_h2o: Optional[float] = None
    densidad: Optional[float] = None
    volumen: Optional[float] = None
    trial814: Optional[str] = None

class PA_EQ_CVCreate(PA_EQ_CVBase): pass
class PA_EQ_CVUpdate(PA_EQ_CVBase): pass
class PA_EQ_CV(PA_EQ_CVBase):
    id: int
    class Config: from_attributes = True

class PA_EQ_DCBase(BaseModel):
    id_ca: Optional[str] = None
    valor_nominal: Optional[float] = None
    referencia: Optional[str] = None
    correccion_reportada: Optional[float] = None
    incertidumbre: Optional[float] = None
    tolerancia_de_medicion: Optional[float] = None
    conformidad: Optional[str] = None
    trial814: Optional[str] = None

class PA_EQ_DCCreate(PA_EQ_DCBase): pass
class PA_EQ_DCUpdate(PA_EQ_DCBase): pass
class PA_EQ_DC(PA_EQ_DCBase):
    id: int
    class Config: from_attributes = True

class PA_EQ_EQBase(BaseModel):
    equipamiento: Optional[str] = None
    codigo_interno: Optional[str] = None
    marca: Optional[str] = None
    serie: Optional[str] = None
    material: Optional[str] = None
    numero_de_piezas: Optional[str] = None
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
    trial814: Optional[str] = None

class PA_EQ_EQCreate(PA_EQ_EQBase): pass
class PA_EQ_EQUpdate(PA_EQ_EQBase): pass
class PA_EQ_EQ(PA_EQ_EQBase):
    id: int
    class Config: from_attributes = True

class PA_EQ_EXBase(BaseModel):
    id_ca: Optional[str] = None
    posicion: Optional[str] = None
    resultado: Optional[float] = None
    resultado_c: Optional[float] = None
    trial814: Optional[str] = None

class PA_EQ_EXCreate(PA_EQ_EXBase): pass
class PA_EQ_EXUpdate(PA_EQ_EXBase): pass
class PA_EQ_EX(PA_EQ_EXBase):
    id: int
    class Config: from_attributes = True

class PA_EQ_HMBase(BaseModel):
    id_ca: Optional[str] = None
    posicion: Optional[str] = None
    lectura1: Optional[float] = None
    lectura2: Optional[float] = None
    lectura3: Optional[float] = None
    promedio: Optional[float] = None
    desviacion_del_promedio: Optional[float] = None
    trial814: Optional[str] = None

class PA_EQ_HMCreate(PA_EQ_HMBase): pass
class PA_EQ_HMUpdate(PA_EQ_HMBase): pass
class PA_EQ_HM(PA_EQ_HMBase):
    id: int
    class Config: from_attributes = True

class PA_EQ_LEBase(BaseModel):
    lista_de_equipos: Optional[str] = None
    equipamiento: Optional[str] = None
    trial814: Optional[str] = None

class PA_EQ_LECreate(PA_EQ_LEBase): pass
class PA_EQ_LEUpdate(PA_EQ_LEBase): pass
class PA_EQ_LE(PA_EQ_LEBase):
    id: int
    class Config: from_attributes = True

class PA_EQ_MABase(BaseModel):
    registrado_por: Optional[str] = None
    fecha: Optional[datetime] = None
    equipamiento: Optional[str] = None
    descripcion_de_mantenimiento: Optional[str] = None
    realizado_por: Optional[str] = None
    autorizado_por: Optional[str] = None
    trial814: Optional[str] = None

class PA_EQ_MACreate(PA_EQ_MABase): pass
class PA_EQ_MAUpdate(PA_EQ_MABase): pass
class PA_EQ_MA(PA_EQ_MABase):
    id: int
    class Config: from_attributes = True

class PA_EQ_MOBase(BaseModel):
    registrado_por: Optional[str] = None
    fecha: Optional[datetime] = None
    id_reactivo: Optional[str] = None
    id_adquisicion: Optional[int] = None
    tipo: Optional[str] = None
    cantidad: Optional[float] = None
    unidad: Optional[str] = None
    comentarios: Optional[str] = None
    trial814: Optional[str] = None

class PA_EQ_MOCreate(PA_EQ_MOBase): pass
class PA_EQ_MOUpdate(PA_EQ_MOBase): pass
class PA_EQ_MO(PA_EQ_MOBase):
    id: int
    class Config: from_attributes = True

class PA_EQ_MRBase(BaseModel):
    material_de_referencia: Optional[str] = None
    fabricante_proveedor: Optional[str] = None
    numero_de_certificado: Optional[str] = None
    lote: Optional[str] = None
    fecha_de_apertura: Optional[datetime] = None
    fecha_de_vencimiento: Optional[datetime] = None
    ubicacion: Optional[str] = None
    cantidad_aprox: Optional[float] = None
    unidad: Optional[str] = None
    comentarios: Optional[str] = None
    estado: Optional[str] = None
    cantidad_disponible: Optional[float] = None
    tipo: Optional[str] = None
    trial814: Optional[str] = None

class PA_EQ_MRCreate(PA_EQ_MRBase): pass
class PA_EQ_MRUpdate(PA_EQ_MRBase): pass
class PA_EQ_MR(PA_EQ_MRBase):
    codigo_interno: str
    class Config: from_attributes = True

class PA_EQ_MVBase(BaseModel):
    fecha: Optional[datetime] = None
    id_mr: Optional[str] = None
    tipo: Optional[str] = None
    cantidad: Optional[float] = None
    unidad: Optional[str] = None
    trial814: Optional[str] = None

class PA_EQ_MVCreate(PA_EQ_MVBase): pass
class PA_EQ_MVUpdate(PA_EQ_MVBase): pass
class PA_EQ_MV(PA_EQ_MVBase):
    id: int
    class Config: from_attributes = True

class PA_EQ_PABase(BaseModel):
    registrado_por: Optional[str] = None
    fecha: Optional[datetime] = None
    programa: Optional[str] = None
    trial814: Optional[str] = None

class PA_EQ_PACreate(PA_EQ_PABase): pass
class PA_EQ_PAUpdate(PA_EQ_PABase): pass
class PA_EQ_PA(PA_EQ_PABase):
    id: int
    class Config: from_attributes = True

class PA_EQ_PRBase(BaseModel):
    equipamiento: Optional[str] = None
    actividad: Optional[str] = None
    fecha_de_actuacion: Optional[datetime] = None
    realizado: Optional[bool] = None
    fecha_realizado: Optional[datetime] = None
    id_pa: Optional[int] = None
    trial814: Optional[str] = None

class PA_EQ_PRCreate(PA_EQ_PRBase): pass
class PA_EQ_PRUpdate(PA_EQ_PRBase): pass
class PA_EQ_PR(PA_EQ_PRBase):
    id: int
    class Config: from_attributes = True

class PA_EQ_REBase(BaseModel):
    descripcion: Optional[str] = None
    marca: Optional[str] = None
    fecha_apert: Optional[datetime] = None
    fecha_venc: Optional[datetime] = None
    cantidad_aprox: Optional[float] = None
    unidad: Optional[str] = None
    ubicacion: Optional[str] = None
    lote: Optional[str] = None
    concentracion: Optional[str] = None
    factor: Optional[float] = None
    densidad_g_cm3: Optional[float] = None
    pureza: Optional[float] = None
    tipo: Optional[str] = None
    proveedor: Optional[str] = None
    comentarios: Optional[str] = None
    ensayo_estabilidad: Optional[str] = None
    trial814: Optional[str] = None

class PA_EQ_RECreate(PA_EQ_REBase): pass
class PA_EQ_REUpdate(PA_EQ_REBase): pass
class PA_EQ_RE(PA_EQ_REBase):
    id_reactivo: str
    class Config: from_attributes = True

class PA_EQ_RPBase(BaseModel):
    id_ca: Optional[str] = None
    lectura1: Optional[float] = None
    lectura2: Optional[float] = None
    lectura3: Optional[float] = None
    promedio: Optional[float] = None
    trial814: Optional[str] = None

class PA_EQ_RPCreate(PA_EQ_RPBase): pass
class PA_EQ_RPUpdate(PA_EQ_RPBase): pass
class PA_EQ_RP(PA_EQ_RPBase):
    id: int
    class Config: from_attributes = True

class PA_EQ_VEBase(BaseModel):
    registrado_por: Optional[str] = None
    fecha: Optional[datetime] = None
    set_patron: Optional[str] = None
    set_comparado: Optional[str] = None
    temperatura_oc: Optional[float] = None
    humedad_relativa: Optional[float] = None
    observaciones: Optional[str] = None
    conclusion: Optional[str] = None
    trial814: Optional[str] = None

class PA_EQ_VECreate(PA_EQ_VEBase): pass
class PA_EQ_VEUpdate(PA_EQ_VEBase): pass
class PA_EQ_VE(PA_EQ_VEBase):
    id: int
    class Config: from_attributes = True

class PA_IA_AHBase(BaseModel):
    registrado_por: Optional[str] = None
    id_am: Optional[int] = None
    fecha: Optional[datetime] = None
    valor: Optional[float] = None
    conforme: Optional[bool] = None
    observaciones: Optional[str] = None
    trial814: Optional[str] = None

class PA_IA_AHCreate(PA_IA_AHBase): pass
class PA_IA_AHUpdate(PA_IA_AHBase): pass
class PA_IA_AH(PA_IA_AHBase):
    id: int
    class Config: from_attributes = True

class PA_IA_AMBase(BaseModel):
    instrumento: Optional[str] = None
    area: Optional[int] = None
    parametro: Optional[str] = None
    especificacion: Optional[str] = None
    frecuencia: Optional[str] = None
    trial814: Optional[str] = None

class PA_IA_AMCreate(PA_IA_AMBase): pass
class PA_IA_AMUpdate(PA_IA_AMBase): pass
class PA_IA_AM(PA_IA_AMBase):
    id: int
    class Config: from_attributes = True

class PA_IA_ARBase(BaseModel):
    area: Optional[str] = None
    trial814: Optional[str] = None

class PA_IA_ARCreate(PA_IA_ARBase): pass
class PA_IA_ARUpdate(PA_IA_ARBase): pass
class PA_IA_AR(PA_IA_ARBase):
    id: int
    class Config: from_attributes = True

class PA_IA_CABase(BaseModel):
    registrado_por: Optional[str] = None
    condiciones_ambientales: Optional[str] = None
    descripcion: Optional[str] = None
    fecha: Optional[datetime] = None
    trial814: Optional[str] = None

class PA_IA_CACreate(PA_IA_CABase): pass
class PA_IA_CAUpdate(PA_IA_CABase): pass
class PA_IA_CA(PA_IA_CABase):
    id: int
    class Config: from_attributes = True

class PA_IA_LEBase(BaseModel):
    id_li: Optional[int] = None
    elemento: Optional[str] = None
    descripcion: Optional[str] = None
    trial814: Optional[str] = None

class PA_IA_LECreate(PA_IA_LEBase): pass
class PA_IA_LEUpdate(PA_IA_LEBase): pass
class PA_IA_LE(PA_IA_LEBase):
    id: int
    class Config: from_attributes = True

class PA_IA_LIBase(BaseModel):
    registrado_por: Optional[str] = None
    lista_de_infraestructura: Optional[str] = None
    descripcion: Optional[str] = None
    fecha: Optional[datetime] = None
    trial814: Optional[str] = None

class PA_IA_LICreate(PA_IA_LIBase): pass
class PA_IA_LIUpdate(PA_IA_LIBase): pass
class PA_IA_LI(PA_IA_LIBase):
    id: int
    class Config: from_attributes = True

class PA_IA_RABase(BaseModel):
    registrado_por: Optional[str] = None
    id_requisitos_condiciones_ambientales: Optional[str] = None
    fecha: Optional[datetime] = None
    trial814: Optional[str] = None

class PA_IA_RACreate(PA_IA_RABase): pass
class PA_IA_RAUpdate(PA_IA_RABase): pass
class PA_IA_RA(PA_IA_RABase):
    id: int
    class Config: from_attributes = True

class PA_IA_RIBase(BaseModel):
    registrado_por: Optional[str] = None
    id_requisitos_de_instalacion: Optional[str] = None
    fecha: Optional[datetime] = None
    trial814: Optional[str] = None

class PA_IA_RICreate(PA_IA_RIBase): pass
class PA_IA_RIUpdate(PA_IA_RIBase): pass
class PA_IA_RI(PA_IA_RIBase):
    id: int
    class Config: from_attributes = True

class PA_IA_SABase(BaseModel):
    id_requisitos_condiciones_ambientales: Optional[int] = None
    seguimiento: Optional[str] = None
    trial814: Optional[str] = None

class PA_IA_SACreate(PA_IA_SABase): pass
class PA_IA_SAUpdate(PA_IA_SABase): pass
class PA_IA_SA(PA_IA_SABase):
    id: int
    class Config: from_attributes = True

class PA_IA_SIBase(BaseModel):
    id_requisitos_de_instalacion: Optional[int] = None
    registrado_por: Optional[str] = None
    seguimiento: Optional[str] = None
    trial814: Optional[str] = None

class PA_IA_SICreate(PA_IA_SIBase): pass
class PA_IA_SIUpdate(PA_IA_SIBase): pass
class PA_IA_SI(PA_IA_SIBase):
    id: int
    class Config: from_attributes = True

class PA_PE_AUBase(BaseModel):
    autorizado_a: Optional[str] = None
    cargo: Optional[str] = None
    autorizacion: Optional[str] = None
    fecha_autorizacion: Optional[datetime] = None
    vigente: Optional[bool] = None
    trial814: Optional[str] = None

class PA_PE_AUCreate(PA_PE_AUBase): pass
class PA_PE_AUUpdate(PA_PE_AUBase): pass
class PA_PE_AU(PA_PE_AUBase):
    id: int
    class Config: from_attributes = True

class PA_PE_CVBase(BaseModel):
    personal: Optional[str] = None
    requisito_de_competencia: Optional[str] = None
    responsable: Optional[str] = None
    fecha_de_evaluacion: Optional[datetime] = None
    metodo: Optional[str] = None
    resultado: Optional[str] = None
    eficaz: Optional[bool] = None
    comentarios: Optional[str] = None
    trial814: Optional[str] = None

class PA_PE_CVCreate(PA_PE_CVBase): pass
class PA_PE_CVUpdate(PA_PE_CVBase): pass
class PA_PE_CV(PA_PE_CVBase):
    id: int
    class Config: from_attributes = True

class PA_PE_DEBase(BaseModel):
    cargo: Optional[str] = None
    trial814: Optional[str] = None

class PA_PE_DECreate(PA_PE_DEBase): pass
class PA_PE_DEUpdate(PA_PE_DEBase): pass
class PA_PE_DE(PA_PE_DEBase):
    abreviacion: str
    class Config: from_attributes = True

class PA_PE_ECBase(BaseModel):
    descripcion: Optional[str] = None
    trial814: Optional[str] = None

class PA_PE_ECCreate(PA_PE_ECBase): pass
class PA_PE_ECUpdate(PA_PE_ECBase): pass
class PA_PE_EC(PA_PE_ECBase):
    elemento_de_competencia: str
    class Config: from_attributes = True

class PA_PE_EFBase(BaseModel):
    tipo: Optional[str] = None
    item_evaluado: Optional[str] = None
    fecha_evaluacion: Optional[datetime] = None
    resultado: Optional[str] = None
    eficaz: Optional[bool] = None
    observaciones: Optional[str] = None
    trial814: Optional[str] = None

class PA_PE_EFCreate(PA_PE_EFBase): pass
class PA_PE_EFUpdate(PA_PE_EFBase): pass
class PA_PE_EF(PA_PE_EFBase):
    id: int
    class Config: from_attributes = True

class PA_PE_FGBase(BaseModel):
    forma_de_generacion: Optional[str] = None
    trial814: Optional[str] = None

class PA_PE_FGCreate(PA_PE_FGBase): pass
class PA_PE_FGUpdate(PA_PE_FGBase): pass
class PA_PE_FG(PA_PE_FGBase):
    id: int
    class Config: from_attributes = True

class PA_PE_IEBase(BaseModel):
    id_is: Optional[int] = None
    item: Optional[str] = None
    descripcion: Optional[str] = None
    trial814: Optional[str] = None

class PA_PE_IECreate(PA_PE_IEBase): pass
class PA_PE_IEUpdate(PA_PE_IEBase): pass
class PA_PE_IE(PA_PE_IEBase):
    id: int
    class Config: from_attributes = True

class PA_PE_ISBase(BaseModel):
    cargo: Optional[str] = None
    descripcion: Optional[str] = None
    trial814: Optional[str] = None

class PA_PE_ISCreate(PA_PE_ISBase): pass
class PA_PE_ISUpdate(PA_PE_ISBase): pass
class PA_PE_IS(PA_PE_ISBase):
    id: int
    class Config: from_attributes = True

class PA_PE_PEBase(BaseModel):
    abreviatura: Optional[str] = None
    personal: Optional[str] = None
    cargo: Optional[str] = None
    fecha_de_contratacion: Optional[datetime] = None
    fecha_de_terminacion: Optional[datetime] = None
    ci: Optional[str] = None
    activo: Optional[bool] = None
    tipo_usuario: Optional[str] = None
    usuario: Optional[str] = None
    contrase_a: Optional[str] = None
    correo: Optional[str] = None
    telefono: Optional[str] = None
    firma: Optional[str] = None
    firma_simple: Optional[str] = None
    genero: Optional[str] = None
    fecha_nacimiento: Optional[datetime] = None
    direccion: Optional[str] = None
    trial814: Optional[str] = None

class PA_PE_PECreate(PA_PE_PEBase): pass
class PA_PE_PEUpdate(PA_PE_PEBase): pass
class PA_PE_PE(PA_PE_PEBase):
    id: int
    class Config: from_attributes = True

class PA_PE_PLBase(BaseModel):
    item_del_programa: Optional[str] = None
    fecha_de_registro: Optional[datetime] = None
    tipo_de_plan: Optional[str] = None
    elaborado_por: Optional[str] = None
    autorizado_por: Optional[str] = None
    asistentes: Optional[str] = None
    evaluadores: Optional[str] = None
    forma_generacion: Optional[int] = None
    objetivo: Optional[str] = None
    contenido: Optional[str] = None
    fecha_programada: Optional[datetime] = None
    fecha_realizada: Optional[datetime] = None
    horas: Optional[float] = None
    responsable: Optional[str] = None
    trial814: Optional[str] = None

class PA_PE_PLCreate(PA_PE_PLBase): pass
class PA_PE_PLUpdate(PA_PE_PLBase): pass
class PA_PE_PL(PA_PE_PLBase):
    id: int
    class Config: from_attributes = True

class PA_PE_POBase(BaseModel):
    proceso_de_seleccion: Optional[int] = None
    nombre_completo: Optional[str] = None
    ci: Optional[str] = None
    fecha_nacimiento: Optional[datetime] = None
    telefono: Optional[str] = None
    correo: Optional[str] = None
    direccion: Optional[str] = None
    cv: Optional[str] = None
    puntaje: Optional[float] = None
    observaciones: Optional[str] = None
    seleccionado: Optional[bool] = None
    trial814: Optional[str] = None

class PA_PE_POCreate(PA_PE_POBase): pass
class PA_PE_POUpdate(PA_PE_POBase): pass
class PA_PE_PO(PA_PE_POBase):
    id: int
    class Config: from_attributes = True

class PA_PE_PRBase(BaseModel):
    registrado_por: Optional[str] = None
    fecha: Optional[datetime] = None
    dirigido_a: Optional[str] = None
    actividad: Optional[str] = None
    lugar: Optional[str] = None
    observaciones: Optional[str] = None
    trial814: Optional[str] = None

class PA_PE_PRCreate(PA_PE_PRBase): pass
class PA_PE_PRUpdate(PA_PE_PRBase): pass
class PA_PE_PR(PA_PE_PRBase):
    id: int
    class Config: from_attributes = True

class PA_PE_RQBase(BaseModel):
    cargo_req: Optional[str] = None
    responsable: Optional[str] = None
    edad_minima: Optional[int] = None
    edad_maxima: Optional[int] = None
    genero: Optional[str] = None
    educacion_requerida: Optional[str] = None
    experiencia_requerida: Optional[str] = None
    conocimientos_especificos: Optional[str] = None
    habilidades: Optional[str] = None
    trial814: Optional[str] = None

class PA_PE_RQCreate(PA_PE_RQBase): pass
class PA_PE_RQUpdate(PA_PE_RQBase): pass
class PA_PE_RQ(PA_PE_RQBase):
    id: int
    class Config: from_attributes = True

class PA_PE_SEBase(BaseModel):
    personal: Optional[str] = None
    requisitos: Optional[int] = None
    responsable: Optional[str] = None
    fecha: Optional[datetime] = None
    puntaje_total: Optional[float] = None
    calificacion: Optional[str] = None
    observaciones: Optional[str] = None
    trial814: Optional[str] = None

class PA_PE_SECreate(PA_PE_SEBase): pass
class PA_PE_SEUpdate(PA_PE_SEBase): pass
class PA_PE_SE(PA_PE_SEBase):
    id: int
    class Config: from_attributes = True

class PA_PE_SPBase(BaseModel):
    proceso_de_seleccion: Optional[str] = None
    puesto: Optional[str] = None
    evaluadores: Optional[str] = None
    fecha_apertura: Optional[datetime] = None
    fecha_cierre: Optional[datetime] = None
    trial814: Optional[str] = None

class PA_PE_SPCreate(PA_PE_SPBase): pass
class PA_PE_SPUpdate(PA_PE_SPBase): pass
class PA_PE_SP(PA_PE_SPBase):
    id: int
    class Config: from_attributes = True

class PA_PE_SUBase(BaseModel):
    supervisores: Optional[str] = None
    fecha: Optional[datetime] = None
    area: Optional[str] = None
    observaciones: Optional[str] = None
    trial814: Optional[str] = None

class PA_PE_SUCreate(PA_PE_SUBase): pass
class PA_PE_SUUpdate(PA_PE_SUBase): pass
class PA_PE_SU(PA_PE_SUBase):
    id: int
    class Config: from_attributes = True

class PA_PS_ADBase(BaseModel):
    registrado_por: Optional[str] = None
    fecha: Optional[datetime] = None
    producto_o_servicio: Optional[int] = None
    descripcion: Optional[str] = None
    cantidad: Optional[float] = None
    unidad: Optional[str] = None
    proveedor_seleccionado: Optional[str] = None
    monto: Optional[float] = None
    estado: Optional[str] = None
    observaciones: Optional[str] = None
    trial814: Optional[str] = None

class PA_PS_ADCreate(PA_PS_ADBase): pass
class PA_PS_ADUpdate(PA_PS_ADBase): pass
class PA_PS_AD(PA_PS_ADBase):
    id: int
    class Config: from_attributes = True

class PA_PS_CRBase(BaseModel):
    criterio: Optional[str] = None
    descripcion: Optional[str] = None
    trial814: Optional[str] = None

class PA_PS_CRCreate(PA_PS_CRBase): pass
class PA_PS_CRUpdate(PA_PS_CRBase): pass
class PA_PS_CR(PA_PS_CRBase):
    id_criterio: str
    class Config: from_attributes = True

class PA_PS_DEBase(BaseModel):
    id_evaluacion: Optional[int] = None
    id_criterio: Optional[str] = None
    puntaje: Optional[float] = None
    trial814: Optional[str] = None

class PA_PS_DECreate(PA_PS_DEBase): pass
class PA_PS_DEUpdate(PA_PS_DEBase): pass
class PA_PS_DE(PA_PS_DEBase):
    id: int
    class Config: from_attributes = True

class PA_PS_EVBase(BaseModel):
    id_adquisicion: Optional[int] = None
    id_proveedor: Optional[int] = None
    fecha_evaluacion: Optional[datetime] = None
    puntaje_total: Optional[float] = None
    calificacion: Optional[str] = None
    observaciones: Optional[str] = None
    trial814: Optional[str] = None

class PA_PS_EVCreate(PA_PS_EVBase): pass
class PA_PS_EVUpdate(PA_PS_EVBase): pass
class PA_PS_EV(PA_PS_EVBase):
    id: int
    class Config: from_attributes = True

class PA_PS_OSBase(BaseModel):
    id_ad: Optional[int] = None
    numero_orden: Optional[str] = None
    fecha_emision: Optional[datetime] = None
    fecha_entrega_esperada: Optional[datetime] = None
    fecha_entrega_real: Optional[datetime] = None
    estado: Optional[str] = None
    trial814: Optional[str] = None

class PA_PS_OSCreate(PA_PS_OSBase): pass
class PA_PS_OSUpdate(PA_PS_OSBase): pass
class PA_PS_OS(PA_PS_OSBase):
    id: int
    class Config: from_attributes = True

class PA_PS_PRBase(BaseModel):
    proveedor: Optional[str] = None
    razon_social: Optional[str] = None
    nit: Optional[str] = None
    direccion: Optional[str] = None
    telefono: Optional[str] = None
    correo: Optional[str] = None
    contacto: Optional[str] = None
    tipo_proveedor: Optional[str] = None
    activo: Optional[bool] = None
    trial814: Optional[str] = None

class PA_PS_PRCreate(PA_PS_PRBase): pass
class PA_PS_PRUpdate(PA_PS_PRBase): pass
class PA_PS_PR(PA_PS_PRBase):
    id: int
    class Config: from_attributes = True

class PA_PS_PSBase(BaseModel):
    producto_servicio: Optional[str] = None
    tipo: Optional[str] = None
    descripcion: Optional[str] = None
    codigo: Optional[str] = None
    vigente: Optional[bool] = None
    trial814: Optional[str] = None

class PA_PS_PSCreate(PA_PS_PSBase): pass
class PA_PS_PSUpdate(PA_PS_PSBase): pass
class PA_PS_PS(PA_PS_PSBase):
    id: int
    class Config: from_attributes = True

class PC_ES_ESBase(BaseModel):
    responsable: Optional[str] = None
    fecha: Optional[datetime] = None
    cliente: Optional[str] = None
    puntaje_total: Optional[float] = None
    observaciones: Optional[str] = None
    trial814: Optional[str] = None

class PC_ES_ESCreate(PC_ES_ESBase): pass
class PC_ES_ESUpdate(PC_ES_ESBase): pass
class PC_ES_ES(PC_ES_ESBase):
    id: int
    class Config: from_attributes = True

class PC_LAB_PATRONESBase(BaseModel):
    codigo_patron: Optional[str] = None
    descripcion: Optional[str] = None
    concentracion: Optional[str] = None
    trial814: Optional[str] = None

class PC_LAB_PATRONESCreate(PC_LAB_PATRONESBase): pass
class PC_LAB_PATRONESUpdate(PC_LAB_PATRONESBase): pass
class PC_LAB_PATRONES(PC_LAB_PATRONESBase):
    id: int
    class Config: from_attributes = True

class PC_LAB_SOLUCIONESBase(BaseModel):
    codigo_solucion: Optional[str] = None
    nombre: Optional[str] = None
    concentracion: Optional[str] = None
    fecha_preparacion: Optional[datetime] = None
    fecha_vencimiento: Optional[datetime] = None
    preparado_por: Optional[str] = None
    trial814: Optional[str] = None

class PC_LAB_SOLUCIONESCreate(PC_LAB_SOLUCIONESBase): pass
class PC_LAB_SOLUCIONESUpdate(PC_LAB_SOLUCIONESBase): pass
class PC_LAB_SOLUCIONES(PC_LAB_SOLUCIONESBase):
    id: int
    class Config: from_attributes = True

class PC_LAB_SOLUCIONES_DETBase(BaseModel):
    id_solucion: Optional[int] = None
    reactivo: Optional[str] = None
    cantidad: Optional[float] = None
    unidad: Optional[str] = None
    trial814: Optional[str] = None

class PC_LAB_SOLUCIONES_DETCreate(PC_LAB_SOLUCIONES_DETBase): pass
class PC_LAB_SOLUCIONES_DETUpdate(PC_LAB_SOLUCIONES_DETBase): pass
class PC_LAB_SOLUCIONES_DET(PC_LAB_SOLUCIONES_DETBase):
    id: int
    class Config: from_attributes = True

class PC_LAB_VALIDACIONMETODOSBase(BaseModel):
    codigo_metodo: Optional[str] = None
    nombre_metodo: Optional[str] = None
    fecha_validacion: Optional[datetime] = None
    responsable: Optional[str] = None
    estado: Optional[str] = None
    observaciones: Optional[str] = None
    trial814: Optional[str] = None

class PC_LAB_VALIDACIONMETODOSCreate(PC_LAB_VALIDACIONMETODOSBase): pass
class PC_LAB_VALIDACIONMETODOSUpdate(PC_LAB_VALIDACIONMETODOSBase): pass
class PC_LAB_VALIDACIONMETODOS(PC_LAB_VALIDACIONMETODOSBase):
    id: int
    class Config: from_attributes = True

class PC_QR_QUBase(BaseModel):
    registrado_por: Optional[str] = None
    fecha: Optional[datetime] = None
    codigo_queja: Optional[str] = None
    cliente: Optional[str] = None
    tipo: Optional[str] = None
    descripcion: Optional[str] = None
    estado: Optional[str] = None
    resolucion: Optional[str] = None
    trial814: Optional[str] = None

class PC_QR_QUCreate(PC_QR_QUBase): pass
class PC_QR_QUUpdate(PC_QR_QUBase): pass
class PC_QR_QU(PC_QR_QUBase):
    id: int
    class Config: from_attributes = True

class PC_RE_ACBase(BaseModel):
    cliente: Optional[int] = None
    contacto: Optional[int] = None
    servicio_global: Optional[int] = None
    servicio: Optional[int] = None
    proforma: Optional[int] = None
    responsable_de_muestra: Optional[str] = None
    fecha_solicitud: Optional[datetime] = None
    fecha_inicio: Optional[datetime] = None
    fecha_finalizacion: Optional[datetime] = None
    estado: Optional[str] = None
    observaciones: Optional[str] = None
    trial814: Optional[str] = None

class PC_RE_ACCreate(PC_RE_ACBase): pass
class PC_RE_ACUpdate(PC_RE_ACBase): pass
class PC_RE_AC(PC_RE_ACBase):
    id: int
    class Config: from_attributes = True

class PC_RE_ANALISISBase(BaseModel):
    fecha: Optional[datetime] = None
    codigo_analisis: Optional[str] = None
    descripcion: Optional[str] = None
    trial814: Optional[str] = None

class PC_RE_ANALISISCreate(PC_RE_ANALISISBase): pass
class PC_RE_ANALISISUpdate(PC_RE_ANALISISBase): pass
class PC_RE_ANALISIS(PC_RE_ANALISISBase):
    id: int
    class Config: from_attributes = True

class PC_RE_CCBase(BaseModel):
    id_cl: Optional[int] = None
    nombre_contacto: Optional[str] = None
    cargo: Optional[str] = None
    telefono: Optional[str] = None
    correo: Optional[str] = None
    trial814: Optional[str] = None

class PC_RE_CCCreate(PC_RE_CCBase): pass
class PC_RE_CCUpdate(PC_RE_CCBase): pass
class PC_RE_CC(PC_RE_CCBase):
    id: int
    class Config: from_attributes = True

class PC_RE_CLBase(BaseModel):
    cliente: Optional[str] = None
    razon_social: Optional[str] = None
    nit: Optional[str] = None
    direccion: Optional[str] = None
    telefono: Optional[str] = None
    correo: Optional[str] = None
    activo: Optional[bool] = None
    trial814: Optional[str] = None

class PC_RE_CLCreate(PC_RE_CLBase): pass
class PC_RE_CLUpdate(PC_RE_CLBase): pass
class PC_RE_CL(PC_RE_CLBase):
    id: int
    class Config: from_attributes = True

class PC_RE_COBase(BaseModel):
    codigo_cotizacion: Optional[str] = None
    fecha: Optional[datetime] = None
    cliente: Optional[str] = None
    monto_total: Optional[float] = None
    estado: Optional[str] = None
    trial814: Optional[str] = None

class PC_RE_COCreate(PC_RE_COBase): pass
class PC_RE_COUpdate(PC_RE_COBase): pass
class PC_RE_CO(PC_RE_COBase):
    id: int
    class Config: from_attributes = True

class PC_RE_MUBase(BaseModel):
    id_ac: Optional[int] = None
    codigo_muestra: Optional[str] = None
    descripcion: Optional[str] = None
    fecha_recepcion: Optional[datetime] = None
    estado: Optional[str] = None
    trial814: Optional[str] = None

class PC_RE_MUCreate(PC_RE_MUBase): pass
class PC_RE_MUUpdate(PC_RE_MUBase): pass
class PC_RE_MU(PC_RE_MUBase):
    id: int
    class Config: from_attributes = True

class PC_RE_OFBase(BaseModel):
    revisado_por: Optional[str] = None
    fecha: Optional[datetime] = None
    codigo_oferta: Optional[str] = None
    descripcion: Optional[str] = None
    trial814: Optional[str] = None

class PC_RE_OFCreate(PC_RE_OFBase): pass
class PC_RE_OFUpdate(PC_RE_OFBase): pass
class PC_RE_OF(PC_RE_OFBase):
    id: int
    class Config: from_attributes = True

class PC_RE_PIBase(BaseModel):
    id_pr: Optional[int] = None
    servicio: Optional[int] = None
    cantidad: Optional[int] = None
    precio_unitario: Optional[float] = None
    subtotal: Optional[float] = None
    trial814: Optional[str] = None

class PC_RE_PICreate(PC_RE_PIBase): pass
class PC_RE_PIUpdate(PC_RE_PIBase): pass
class PC_RE_PI(PC_RE_PIBase):
    id: int
    class Config: from_attributes = True

class PC_RE_PRBase(BaseModel):
    registrado_por: Optional[str] = None
    fecha: Optional[datetime] = None
    codigo_proforma: Optional[str] = None
    cliente: Optional[str] = None
    contacto: Optional[str] = None
    monto_total: Optional[float] = None
    vigencia: Optional[datetime] = None
    estado: Optional[str] = None
    observaciones: Optional[str] = None
    trial814: Optional[str] = None

class PC_RE_PRCreate(PC_RE_PRBase): pass
class PC_RE_PRUpdate(PC_RE_PRBase): pass
class PC_RE_PR(PC_RE_PRBase):
    id: int
    class Config: from_attributes = True

class PC_RE_SEBase(BaseModel):
    servicio: Optional[str] = None
    descripcion: Optional[str] = None
    codigo: Optional[str] = None
    vigente: Optional[bool] = None
    trial814: Optional[str] = None

class PC_RE_SECreate(PC_RE_SEBase): pass
class PC_RE_SEUpdate(PC_RE_SEBase): pass
class PC_RE_SE(PC_RE_SEBase):
    id: int
    class Config: from_attributes = True

class PC_RE_SGBase(BaseModel):
    servicio_global: Optional[str] = None
    descripcion: Optional[str] = None
    trial814: Optional[str] = None

class PC_RE_SGCreate(PC_RE_SGBase): pass
class PC_RE_SGUpdate(PC_RE_SGBase): pass
class PC_RE_SG(PC_RE_SGBase):
    id: int
    class Config: from_attributes = True

class PC_RE_SHBase(BaseModel):
    id_sg: Optional[int] = None
    servicio: Optional[int] = None
    trial814: Optional[str] = None

class PC_RE_SHCreate(PC_RE_SHBase): pass
class PC_RE_SHUpdate(PC_RE_SHBase): pass
class PC_RE_SH(PC_RE_SHBase):
    id: int
    class Config: from_attributes = True

class PC_RE_SOBase(BaseModel):
    codigo_solicitud: Optional[str] = None
    fecha: Optional[datetime] = None
    solicitante: Optional[str] = None
    descripcion: Optional[str] = None
    estado: Optional[str] = None
    trial814: Optional[str] = None

class PC_RE_SOCreate(PC_RE_SOBase): pass
class PC_RE_SOUpdate(PC_RE_SOBase): pass
class PC_RE_SO(PC_RE_SOBase):
    id: int
    class Config: from_attributes = True

class PC_TC_TCBase(BaseModel):
    registrado_por: Optional[str] = None
    fecha: Optional[datetime] = None
    codigo: Optional[str] = None
    descripcion: Optional[str] = None
    trial814: Optional[str] = None

class PC_TC_TCCreate(PC_TC_TCBase): pass
class PC_TC_TCUpdate(PC_TC_TCBase): pass
class PC_TC_TC(PC_TC_TCBase):
    id: int
    class Config: from_attributes = True

class PE_PL_ACBase(BaseModel):
    riesgo_oportunidad: Optional[int] = None
    acciones_de_mejora: Optional[int] = None
    acciones_correctivas: Optional[int] = None
    correciones: Optional[int] = None
    accion: Optional[str] = None
    responsable: Optional[str] = None
    fecha_planificada: Optional[datetime] = None
    fecha_cumplida: Optional[datetime] = None
    estado: Optional[str] = None
    trial814: Optional[str] = None

class PE_PL_ACCreate(PE_PL_ACBase): pass
class PE_PL_ACUpdate(PE_PL_ACBase): pass
class PE_PL_AC(PE_PL_ACBase):
    id: int
    class Config: from_attributes = True

class PE_PL_COBase(BaseModel):
    registrado_por: Optional[str] = None
    fecha: Optional[datetime] = None
    tipo: Optional[str] = None
    descripcion: Optional[str] = None
    trial814: Optional[str] = None

class PE_PL_COCreate(PE_PL_COBase): pass
class PE_PL_COUpdate(PE_PL_COBase): pass
class PE_PL_CO(PE_PL_COBase):
    id: int
    class Config: from_attributes = True

class PE_PL_ESBase(BaseModel):
    registrado_por: Optional[str] = None
    fecha: Optional[datetime] = None
    estrategia: Optional[str] = None
    descripcion: Optional[str] = None
    vigente: Optional[bool] = None
    trial814: Optional[str] = None

class PE_PL_ESCreate(PE_PL_ESBase): pass
class PE_PL_ESUpdate(PE_PL_ESBase): pass
class PE_PL_ES(PE_PL_ESBase):
    id: int
    class Config: from_attributes = True

class PE_PL_OBBase(BaseModel):
    registrado_por: Optional[str] = None
    estrategia_1: Optional[int] = None
    fecha: Optional[datetime] = None
    objetivo: Optional[str] = None
    descripcion: Optional[str] = None
    vigente: Optional[bool] = None
    trial814: Optional[str] = None

class PE_PL_OBCreate(PE_PL_OBBase): pass
class PE_PL_OBUpdate(PE_PL_OBBase): pass
class PE_PL_OB(PE_PL_OBBase):
    id: int
    class Config: from_attributes = True

class PE_PL_PCBase(BaseModel):
    responsable: Optional[str] = None
    riesgo_oportunidad: Optional[int] = None
    fecha: Optional[datetime] = None
    descripcion: Optional[str] = None
    trial814: Optional[str] = None

class PE_PL_PCCreate(PE_PL_PCBase): pass
class PE_PL_PCUpdate(PE_PL_PCBase): pass
class PE_PL_PC(PE_PL_PCBase):
    id: int
    class Config: from_attributes = True

class PE_PL_PIBase(BaseModel):
    registrado_por: Optional[str] = None
    fecha: Optional[datetime] = None
    parte_interesada: Optional[str] = None
    necesidades_expectativas: Optional[str] = None
    relevancia: Optional[str] = None
    trial814: Optional[str] = None

class PE_PL_PICreate(PE_PL_PIBase): pass
class PE_PL_PIUpdate(PE_PL_PIBase): pass
class PE_PL_PI(PE_PL_PIBase):
    id: int
    class Config: from_attributes = True

class PE_PL_PLBase(BaseModel):
    objetivo: Optional[int] = None
    plan: Optional[str] = None
    descripcion: Optional[str] = None
    fecha_inicio: Optional[datetime] = None
    fecha_fin: Optional[datetime] = None
    estado: Optional[str] = None
    trial814: Optional[str] = None

class PE_PL_PLCreate(PE_PL_PLBase): pass
class PE_PL_PLUpdate(PE_PL_PLBase): pass
class PE_PL_PL(PE_PL_PLBase):
    id: int
    class Config: from_attributes = True

class PE_PL_ROBase(BaseModel):
    registrado_por: Optional[str] = None
    fecha: Optional[datetime] = None
    tipo: Optional[str] = None
    descripcion: Optional[str] = None
    probabilidad: Optional[str] = None
    impacto: Optional[str] = None
    nivel_riesgo: Optional[str] = None
    estado: Optional[str] = None
    trial814: Optional[str] = None

class PE_PL_ROCreate(PE_PL_ROBase): pass
class PE_PL_ROUpdate(PE_PL_ROBase): pass
class PE_PL_RO(PE_PL_ROBase):
    id: int
    class Config: from_attributes = True

class PE_SE_ACBase(BaseModel):
    registrado_por: Optional[str] = None
    fecha: Optional[datetime] = None
    descripcion_no_conformidad: Optional[str] = None
    causa_raiz: Optional[str] = None
    accion_correctiva: Optional[str] = None
    responsable: Optional[str] = None
    fecha_planificada: Optional[datetime] = None
    fecha_implementada: Optional[datetime] = None
    estado: Optional[str] = None
    trial814: Optional[str] = None

class PE_SE_ACCreate(PE_SE_ACBase): pass
class PE_SE_ACUpdate(PE_SE_ACBase): pass
class PE_SE_AC(PE_SE_ACBase):
    id: int
    class Config: from_attributes = True

class PE_SE_CABase(BaseModel):
    acciones_correctivas: Optional[int] = None
    causa: Optional[str] = None
    trial814: Optional[str] = None

class PE_SE_CACreate(PE_SE_CABase): pass
class PE_SE_CAUpdate(PE_SE_CABase): pass
class PE_SE_CA(PE_SE_CABase):
    id: int
    class Config: from_attributes = True

class PE_SE_COBase(BaseModel):
    correcciones: Optional[int] = None
    descripcion: Optional[str] = None
    fecha: Optional[datetime] = None
    responsable: Optional[str] = None
    trial814: Optional[str] = None

class PE_SE_COCreate(PE_SE_COBase): pass
class PE_SE_COUpdate(PE_SE_COBase): pass
class PE_SE_CO(PE_SE_COBase):
    id: int
    class Config: from_attributes = True

class PE_SE_EEBase(BaseModel):
    trial814: Optional[str] = None

class PE_SE_EECreate(PE_SE_EEBase): pass
class PE_SE_EEUpdate(PE_SE_EEBase): pass
class PE_SE_EE(PE_SE_EEBase):
    entradas: str
    class Config: from_attributes = True

class PE_SE_ENBase(BaseModel):
    id_re: Optional[int] = None
    entrada: Optional[str] = None
    descripcion: Optional[str] = None
    trial814: Optional[str] = None

class PE_SE_ENCreate(PE_SE_ENBase): pass
class PE_SE_ENUpdate(PE_SE_ENBase): pass
class PE_SE_EN(PE_SE_ENBase):
    id: int
    class Config: from_attributes = True

class PE_SE_MABase(BaseModel):
    acciones_de_mejora: Optional[int] = None
    descripcion: Optional[str] = None
    trial814: Optional[str] = None

class PE_SE_MACreate(PE_SE_MABase): pass
class PE_SE_MAUpdate(PE_SE_MABase): pass
class PE_SE_MA(PE_SE_MABase):
    id: int
    class Config: from_attributes = True

class PE_SE_MEBase(BaseModel):
    fecha: Optional[datetime] = None
    descripcion_oportunidad: Optional[str] = None
    accion_mejora: Optional[str] = None
    responsable: Optional[str] = None
    fecha_planificada: Optional[datetime] = None
    fecha_implementada: Optional[datetime] = None
    estado: Optional[str] = None
    trial814: Optional[str] = None

class PE_SE_MECreate(PE_SE_MEBase): pass
class PE_SE_MEUpdate(PE_SE_MEBase): pass
class PE_SE_ME(PE_SE_MEBase):
    id: int
    class Config: from_attributes = True

class PE_SE_REBase(BaseModel):
    recurso: Optional[str] = None
    descripcion: Optional[str] = None
    tipo: Optional[str] = None
    trial814: Optional[str] = None

class PE_SE_RECreate(PE_SE_REBase): pass
class PE_SE_REUpdate(PE_SE_REBase): pass
class PE_SE_RE(PE_SE_REBase):
    id: int
    class Config: from_attributes = True

class PE_SE_SABase(BaseModel):
    id_re: Optional[int] = None
    salida: Optional[str] = None
    descripcion: Optional[str] = None
    trial814: Optional[str] = None

class PE_SE_SACreate(PE_SE_SABase): pass
class PE_SE_SAUpdate(PE_SE_SABase): pass
class PE_SE_SA(PE_SE_SABase):
    id: int
    class Config: from_attributes = True

class PE_SE_SSBase(BaseModel):
    trial814: Optional[str] = None

class PE_SE_SSCreate(PE_SE_SSBase): pass
class PE_SE_SSUpdate(PE_SE_SSBase): pass
class PE_SE_SS(PE_SE_SSBase):
    salidas: str
    class Config: from_attributes = True

class SYS_FACTORESKBase(BaseModel):
    k: Optional[float] = None
    n: Optional[int] = None
    trial814: Optional[str] = None

class SYS_FACTORESKCreate(SYS_FACTORESKBase): pass
class SYS_FACTORESKUpdate(SYS_FACTORESKBase): pass
class SYS_FACTORESK(SYS_FACTORESKBase):
    id: int
    class Config: from_attributes = True

class TBL_LUGARESBase(BaseModel):
    lugar: Optional[str] = None
    descripcion: Optional[str] = None
    activo: Optional[bool] = None
    trial814: Optional[str] = None

class TBL_LUGARESCreate(TBL_LUGARESBase): pass
class TBL_LUGARESUpdate(TBL_LUGARESBase): pass
class TBL_LUGARES(TBL_LUGARESBase):
    id: int
    class Config: from_attributes = True

class TBL_POSICIONES_HORNOBase(BaseModel):
    posicion: Optional[str] = None
    descripcion: Optional[str] = None
    trial814: Optional[str] = None

class TBL_POSICIONES_HORNOCreate(TBL_POSICIONES_HORNOBase): pass
class TBL_POSICIONES_HORNOUpdate(TBL_POSICIONES_HORNOBase): pass
class TBL_POSICIONES_HORNO(TBL_POSICIONES_HORNOBase):
    id: int
    class Config: from_attributes = True
