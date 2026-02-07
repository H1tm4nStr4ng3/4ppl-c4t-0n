from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

# =============================================================================
# 1. CATEGORÍAS / LISTA DE EQUIPOS (PA_EQ_LE)
# =============================================================================
class PA_EQ_LEBase(BaseModel):
    # La clave es que el nombre del equipo es obligatorio
    lista_de_equipos: str 

class PA_EQ_LECreate(PA_EQ_LEBase):
    # SOLUCIÓN DEL ERROR: Definimos id como opcional y None por defecto.
    # Así Pydantic no reclama si no lo envías.
    id: Optional[int] = None 

class PA_EQ_LEUpdate(PA_EQ_LEBase):
    pass

class PA_EQ_LERead(PA_EQ_LEBase):
    # Al leer, sí queremos ver el ID que generó la base de datos
    id: Optional[int] = None 
    class Config:
        from_attributes = True

# =============================================================================
# 2. INVENTARIO DE EQUIPOS (PA_EQ_EQ)
# =============================================================================
class PA_EQ_EQBase(BaseModel):
    # IMPORTANTE: No incluimos 'id' aquí
    equipamiento: Optional[str] = None # FK a lista_de_equipos
    codigo_interno: str # Unique
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
    
    # CAMPOS NUEVOS
    version_software: Optional[str] = None
    version_firmware: Optional[str] = None

class PA_EQ_EQCreate(PA_EQ_EQBase):
    pass

class PA_EQ_EQUpdate(PA_EQ_EQBase):
    codigo_interno: Optional[str] = None # En update puede ser opcional

class PA_EQ_EQRead(PA_EQ_EQBase):
    id: int # Aquí sí va el ID
    class Config:
        from_attributes = True

# =============================================================================
# 3. ACTIVIDADES (PA_EQ_AC)
# =============================================================================
class PA_EQ_ACBase(BaseModel):
    actividad: str # PK
    descripcion: Optional[str] = None

class PA_EQ_ACCreate(PA_EQ_ACBase):
    pass

class PA_EQ_ACUpdate(PA_EQ_ACBase):
    pass

class PA_EQ_ACRead(PA_EQ_ACBase):
    id: int
    class Config:
        from_attributes = True

# =============================================================================
# 4. PLANIFICACIÓN Y PROGRAMACIÓN (PA_EQ_PA, PA_EQ_PR)
# =============================================================================
class PA_EQ_PABase(BaseModel):
    gestion: Optional[str] = None
    registrado_por: Optional[str] = None
    fecha: Optional[datetime] = None
    comentarios: Optional[str] = None

class PA_EQ_PACreate(PA_EQ_PABase):
    pass

class PA_EQ_PAUpdate(PA_EQ_PABase):
    pass

class PA_EQ_PARead(PA_EQ_PABase):
    id: int
    class Config:
        from_attributes = True

class PA_EQ_PRBase(BaseModel):
    id_pa: Optional[int] = None
    mes: Optional[str] = None
    actividad: Optional[str] = None # FK
    equipamiento: Optional[str] = None # FK Codigo Interno
    realizado: bool = False
    anulado: bool = False
    comentarios: Optional[str] = None

class PA_EQ_PRCreate(PA_EQ_PRBase):
    pass

class PA_EQ_PRUpdate(PA_EQ_PRBase):
    pass

class PA_EQ_PRRead(PA_EQ_PRBase):
    id_prog: int
    class Config:
        from_attributes = True

# =============================================================================
# 5. MANTENIMIENTO (PA_EQ_MA)
# =============================================================================
class PA_EQ_MABase(BaseModel):
    registrado_por: Optional[str] = None
    fecha: Optional[datetime] = None
    equipamiento: Optional[str] = None # FK
    tipo_de_mantenimiento: Optional[str] = None
    comentarios_de_mantenimiento: Optional[str] = None
    apto: bool = False

class PA_EQ_MACreate(PA_EQ_MABase):
    pass

class PA_EQ_MAUpdate(PA_EQ_MABase):
    pass

class PA_EQ_MARead(PA_EQ_MABase):
    id: int
    class Config:
        from_attributes = True

# =============================================================================
# 6. CALIBRACIONES (PA_EQ_CA) Y SUS DETALLES
# =============================================================================
class PA_EQ_DCBase(BaseModel):
    valor_nominal: Optional[float] = None
    referencia: Optional[str] = None
    correccion_reportada: Optional[float] = None
    incertidumbre: Optional[float] = None
    tolerancia_de_medicion: Optional[float] = None
    conformidad: Optional[str] = None

class PA_EQ_DCCreate(PA_EQ_DCBase):
    pass
class PA_EQ_DCUpdate(PA_EQ_DCBase):
    pass
class PA_EQ_DCRead(PA_EQ_DCBase):
    id: int
    class Config:
        from_attributes = True

class PA_EQ_EXBase(BaseModel):
    carga: Optional[float] = None
    posicion: Optional[float] = None
    diferencia_reportada: Optional[float] = None
    tolerancia: Optional[float] = None
    conformidad: Optional[str] = None

class PA_EQ_EXCreate(PA_EQ_EXBase):
    pass
class PA_EQ_EXUpdate(PA_EQ_EXBase):
    pass
class PA_EQ_EXRead(PA_EQ_EXBase):
    id: int
    class Config:
        from_attributes = True

class PA_EQ_HMBase(BaseModel):
    temperatura_nominal: Optional[float] = None
    en_el_tiempo: Optional[float] = None
    incertidumbre_expandida: Optional[float] = None
    tolerancia_en_el_tiempo: Optional[float] = None
    conformidad_tiempo: Optional[str] = None
    en_el_espacio: Optional[float] = None
    tolerancia_en_el_espacio: Optional[float] = None
    conformidad_espacio: Optional[str] = None

class PA_EQ_HMCreate(PA_EQ_HMBase):
    pass
class PA_EQ_HMUpdate(PA_EQ_HMBase):
    pass
class PA_EQ_HMRead(PA_EQ_HMBase):
    id: int
    class Config:
        from_attributes = True

class PA_EQ_RPBase(BaseModel):
    carga: Optional[float] = None
    desv_est: Optional[float] = None
    tolerancia: Optional[float] = None
    conformidad: Optional[str] = None

class PA_EQ_RPCreate(PA_EQ_RPBase):
    pass
class PA_EQ_RPUpdate(PA_EQ_RPBase):
    pass
class PA_EQ_RPRead(PA_EQ_RPBase):
    id: int
    class Config:
        from_attributes = True

# Tabla Padre (CA)
class PA_EQ_CABase(BaseModel):
    id_equi: Optional[int] = None
    registrado_por: Optional[str] = None
    fecha: Optional[datetime] = None
    equipamiento: Optional[str] = None # FK Codigo Interno
    certificado: str # PK
    ente_calibrador: Optional[str] = None
    fecha_de_calibracion: Optional[datetime] = None
    unidades: Optional[str] = None
    observaciones: Optional[str] = None
    apto: bool = False
    regla: Optional[str] = None

class PA_EQ_CACreate(PA_EQ_CABase):
    pass
class PA_EQ_CAUpdate(PA_EQ_CABase):
    pass
class PA_EQ_CARead(PA_EQ_CABase):
    class Config:
        from_attributes = True

# =============================================================================
# 7. COMPROBACIONES INTERMEDIAS (PA_EQ_CI) Y DETALLES
# =============================================================================
class PA_EQ_CBBase(BaseModel):
    tipoprueba: Optional[str] = None
    pesapatron_id: Optional[str] = None
    posicion: Optional[str] = None
    lectura_balanza: Optional[float] = None
    lectura_corregida: Optional[float] = None

class PA_EQ_CBCreate(PA_EQ_CBBase):
    pass
class PA_EQ_CBUpdate(PA_EQ_CBBase):
    pass
class PA_EQ_CBRead(PA_EQ_CBBase):
    id: int
    class Config:
        from_attributes = True

class PA_EQ_CHBase(BaseModel):
    posicion: Optional[str] = None
    temppatron_leida: Optional[float] = None
    tempequipo_leida: Optional[float] = None
    diferencia: Optional[float] = None
    resultadopunto: Optional[str] = None

class PA_EQ_CHCreate(PA_EQ_CHBase):
    pass
class PA_EQ_CHUpdate(PA_EQ_CHBase):
    pass
class PA_EQ_CHRead(PA_EQ_CHBase):
    id: int
    class Config:
        from_attributes = True

class PA_EQ_CVBase(BaseModel):
    matraz_vacio: Optional[float] = None
    corr1: Optional[float] = None
    matraz_lleno: Optional[float] = None
    corr2: Optional[float] = None
    masa_h2o: Optional[float] = None
    densidad: Optional[float] = None
    volumen: Optional[float] = None

class PA_EQ_CVCreate(PA_EQ_CVBase):
    pass
class PA_EQ_CVUpdate(PA_EQ_CVBase):
    pass
class PA_EQ_CVRead(PA_EQ_CVBase):
    id: int
    class Config:
        from_attributes = True

# Padre (CI)
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

class PA_EQ_CICreate(PA_EQ_CIBase):
    pass
class PA_EQ_CIUpdate(PA_EQ_CIBase):
    pass
class PA_EQ_CIRead(PA_EQ_CIBase):
    id_equi: int
    class Config:
        from_attributes = True

# =============================================================================
# 8. VERIFICACIÓN MASIVA (PA_EQ_VE)
# =============================================================================
class PA_EQ_VEBase(BaseModel):
    fecha: Optional[datetime] = None
    set_patron: Optional[str] = None # FK
    set_comparado: Optional[str] = None # FK
    registrado_por: Optional[str] = None
    objeto_item_medio: Optional[str] = None

    item_1: Optional[str] = None; res_patron_1: float = 0; u_patron_1: float = 0; res_comparado_1: float = 0; u_comparado_1: float = 0; en_1: Optional[float] = None
    # ... (Items adicionales se omiten por brevedad pero se asumen existentes si se necesitan)
    conclusion: Optional[str] = None
    observaciones: Optional[str] = None

class PA_EQ_VECreate(PA_EQ_VEBase):
    pass
class PA_EQ_VEUpdate(PA_EQ_VEBase):
    pass
class PA_EQ_VERead(PA_EQ_VEBase):
    id: int
    class Config:
        from_attributes = True

# =============================================================================
# 9. REACTIVOS Y MOVIMIENTOS (PA_EQ_RE, PA_EQ_MO)
# =============================================================================

# --- HIJO: MOVIMIENTOS / BITÁCORA (MO) ---
class PA_EQ_MOBase(BaseModel):
    # Relación: Usaremos el ID del reactivo como FK
    id_reactivo: Optional[int] = None 
    registrado_por: Optional[str] = None
    fecha_movimiento: Optional[datetime] = None
    tipo_movimiento: Optional[str] = None # Entrada, Salida, Ajuste
    cantidad: Optional[float] = 0.0
    saldo: Optional[float] = 0.0 # Stock resultante
    id_adquisicion: Optional[int] = None
    observaciones: Optional[str] = None

class PA_EQ_MOCreate(PA_EQ_MOBase):
    pass # Sin ID

class PA_EQ_MOUpdate(PA_EQ_MOBase):
    pass

class PA_EQ_MORead(PA_EQ_MOBase):
    id: int # El ID de la tabla movimientos
    class Config:
        from_attributes = True

# --- PADRE: REACTIVOS (RE) ---
class PA_EQ_REBase(BaseModel):
    nombre_reactivo: str # Obligatorio
    codigo_interno: Optional[str] = None
    no_articulo: Optional[str] = None # CAS o Referencia
    proveedor: Optional[str] = None
    marca: Optional[str] = None
    serie: Optional[str] = None # Lote
    
    unidad_almacen: Optional[str] = None # gr, ml, L
    unidad: Optional[str] = None # Presentación
    valor: Optional[float] = 0.0 # Cantidad inicial / actual
    stock_minimo: Optional[int] = 0
    
    ubicacion: Optional[str] = None
    grado_calidad: Optional[str] = None # PA, HPLC, etc.
    estado: Optional[str] = None # Vigente, Agotado
    sustancia_controlada: bool = False
    
    fecha_de_apertura: Optional[datetime] = None
    fecha_de_vencimiento: Optional[datetime] = None
    
    comentarios: Optional[str] = None

class PA_EQ_RECreate(PA_EQ_REBase):
    pass # Sin ID

class PA_EQ_REUpdate(PA_EQ_REBase):
    pass

class PA_EQ_RERead(PA_EQ_REBase):
    id: int
    # LA MOCHILA: Traemos el historial de movimientos
    pa_eq_mo_items: List[PA_EQ_MORead] = []
    
    class Config:
        from_attributes = True

# =============================================================================
# 10. MATERIALES DE REFERENCIA (PA_EQ_MR, PA_EQ_MV)
# =============================================================================

# --- HIJO: ESPECIFICACIONES (MV) ---
class PA_EQ_MVBase(BaseModel):
    id_mr: Optional[str] = None # FK al codigo_interno del padre
    parametro: Optional[str] = None
    valor: Optional[float] = 0.0
    incertidumbre: Optional[float] = 0.0
    unidad: Optional[str] = None

class PA_EQ_MVCreate(PA_EQ_MVBase):
    pass

class PA_EQ_MVUpdate(PA_EQ_MVBase):
    pass

class PA_EQ_MVRead(PA_EQ_MVBase):
    id: int


# --- PADRE: MATERIAL DE REFERENCIA (MR) ---
class PA_EQ_MRBase(BaseModel):
    equipamiento: Optional[str] = None
    codigo_interno: str # Unique y FK del hijo
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

class PA_EQ_MRCreate(PA_EQ_MRBase):
    pass

class PA_EQ_MRUpdate(PA_EQ_MRBase):
    # Permitimos editar todo menos quizás el código si tiene hijos
    pass

class PA_EQ_MRRead(PA_EQ_MRBase):
    id: int
    # AQUÍ ESTÁ LA MAGIA: Incluimos los hijos en la lectura
    pa_eq_mv_items: List[PA_EQ_MVRead] = [] 
    
