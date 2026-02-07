from typing import Optional, List, Any
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

# =============================================================================
# CONFIGURACIÓN BASE
# =============================================================================
class PersonalBase(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        arbitrary_types_allowed=True
    )

# =============================================================================
# 1. CARGOS (PA_PE_DE)
# =============================================================================
class PA_PE_DEBase(PersonalBase):
    abreviacion: Optional[str] = None
    cargo: Optional[str] = None

class PA_PE_DECreate(PersonalBase):
    # PK Manual: Obligatoria
    abreviacion: str = Field(..., max_length=5, description="Código único (Ej: VGR)")
    cargo: str = Field(..., min_length=3)

class PA_PE_DEUpdate(PersonalBase):
    cargo: Optional[str] = None

class PA_PE_DERead(PersonalBase):
    id: int
    abreviacion: str
    cargo: Optional[str] = None

# =============================================================================
# 2. PERSONAL (PA_PE_PE) - FICHA COMPLETA
# =============================================================================
class PA_PE_PEBase(PersonalBase):
    nombre: Optional[str] = None
    cargo: Optional[str] = None
    vigente: Optional[bool] = True

class PA_PE_PECreate(PersonalBase):
    # PK Manual
    abreviatura: str = Field(..., max_length=5)
    nombre: str
    cargo: Optional[str] = None
    vigente: bool = True
    
    # Campos adicionales completos
    fotografia: Optional[str] = None # Ruta del archivo
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
    descripcion: Optional[str] = None # Observaciones

class PA_PE_PEUpdate(PersonalBase):
    nombre: Optional[str] = None
    cargo: Optional[str] = None
    vigente: Optional[bool] = None
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
    descripcion: Optional[str] = None

class PA_PE_PERead(PA_PE_PECreate):
    id: int

# =============================================================================
# 3. CURRICULUM VITAE (PA_PE_CV)
# =============================================================================
class PA_PE_CVCreate(PersonalBase):
    personal: str # FK
    requisito_de_competencia: Optional[str] = None
    carrera_curso_logro: Optional[str] = None
    institucion: Optional[str] = None
    fecha_inicio: Optional[datetime] = None
    fecha_final: Optional[datetime] = None
    carga_horaria: Optional[float] = None
    descripcion: Optional[str] = Field(None, alias="descripción") # Alias por tilde
    respaldo: Optional[str] = None

class PA_PE_CVUpdate(PersonalBase):
    requisito_de_competencia: Optional[str] = None
    carrera_curso_logro: Optional[str] = None
    institucion: Optional[str] = None
    fecha_inicio: Optional[datetime] = None
    fecha_final: Optional[datetime] = None
    carga_horaria: Optional[float] = None
    descripcion: Optional[str] = Field(None, alias="descripción")
    respaldo: Optional[str] = None

class PA_PE_CVRead(PA_PE_CVCreate):
    id: int

# =============================================================================
# 4. AUTORIZACIONES (PA_PE_AU)
# =============================================================================
class PA_PE_AUCreate(PersonalBase):
    autorizado_por: Optional[str] = None
    autorizado_a: Optional[str] = None
    cargo: Optional[str] = None
    fecha: Optional[datetime] = None
    autorizacion_a: Optional[str] = None
    comentario: Optional[str] = None

class PA_PE_AUUpdate(PersonalBase):
    autorizado_por: Optional[str] = None  # <--- Agregado
    autorizacion_a: Optional[str] = None
    comentario: Optional[str] = None
    cargo: Optional[str] = None
    fecha: Optional[datetime] = None      # <--- Agregado

class PA_PE_AURead(PA_PE_AUCreate):
    id: int

# =============================================================================
# 5. ELEMENTOS DE COMPETENCIA (PA_PE_EC)
# =============================================================================
class PA_PE_ECCreate(PersonalBase):
    elemento_de_competencia: str

class PA_PE_ECUpdate(PersonalBase):
    elemento_de_competencia: Optional[str] = None

class PA_PE_ECRead(PersonalBase):
    id: int
    elemento_de_competencia: str

# =============================================================================
# 6. EFICACIA DE FORMACIÓN (PA_PE_EF)
# =============================================================================
class PA_PE_EFCreate(PersonalBase):
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
    eficaz: bool = False
    cerrado: bool = False

class PA_PE_EFUpdate(PA_PE_EFCreate):
    pass

class PA_PE_EFRead(PA_PE_EFCreate):
    id: int

# =============================================================================
# 7. REQUISITOS DEL CARGO (PA_PE_RQ)
# =============================================================================
class PA_PE_RQCreate(PersonalBase):
    fecha: Optional[datetime] = None
    cargo_req: str  # FK
    responsable: Optional[str] = None # FK
    aprobado_vigente: bool = True
    comentarios: Optional[str] = None

    # --- EDUCACION (1-3) ---
    educacion1: Optional[str] = None
    educacion1c: bool = False
    educacion2: Optional[str] = None
    educacion2c: bool = False
    educacion3: Optional[str] = None
    educacion3c: bool = False

    # --- FORMACION (1-10) ---
    formacion1: Optional[str] = None
    formacion1c: bool = False
    formacion2: Optional[str] = None
    formacion2c: bool = False
    formacion3: Optional[str] = None
    formacion3c: bool = False
    formacion4: Optional[str] = None
    formacion4c: bool = False
    formacion5: Optional[str] = None
    formacion5c: bool = False
    formacion6: Optional[str] = None
    formacion6c: bool = False
    formacion7: Optional[str] = None
    formacion7c: bool = False
    formacion8: Optional[str] = None
    formacion8c: bool = False
    formacion9: Optional[str] = None
    formacion9c: bool = False
    formacion10: Optional[str] = None
    formacion10c: bool = False

    # --- EXPERIENCIA (1-5) ---
    experiencia1: Optional[str] = None
    experiencia1c: bool = False
    experiencia2: Optional[str] = None
    experiencia2c: bool = False
    experiencia3: Optional[str] = None
    experiencia3c: bool = False
    experiencia4: Optional[str] = None
    experiencia4c: bool = False
    experiencia5: Optional[str] = None
    experiencia5c: bool = False

    # --- HABILIDADES (1-10) ---
    habilidades1: Optional[str] = None
    habilidades1c: bool = False
    habilidades2: Optional[str] = None
    habilidades2c: bool = False
    habilidades3: Optional[str] = None
    habilidades3c: bool = False
    habilidades4: Optional[str] = None
    habilidades4c: bool = False
    habilidades5: Optional[str] = None
    habilidades5c: bool = False
    habilidades6: Optional[str] = None
    habilidades6c: bool = False
    habilidades7: Optional[str] = None
    habilidades7c: bool = False
    habilidades8: Optional[str] = None
    habilidades8c: bool = False
    habilidades9: Optional[str] = None
    habilidades9c: bool = False
    habilidades10: Optional[str] = None
    habilidades10c: bool = False

    # --- CONOCIMIENTO (1-10) ---
    conocimiento1: Optional[str] = None
    conocimiento1c: bool = False
    conocimiento2: Optional[str] = None
    conocimiento2c: bool = False
    conocimiento3: Optional[str] = None
    conocimiento3c: bool = False
    conocimiento4: Optional[str] = None
    conocimiento4c: bool = False
    conocimiento5: Optional[str] = None
    conocimiento5c: bool = False
    conocimiento6: Optional[str] = None
    conocimiento6c: bool = False
    conocimiento7: Optional[str] = None
    conocimiento7c: bool = False
    conocimiento8: Optional[str] = None
    conocimiento8c: bool = False
    conocimiento9: Optional[str] = None
    conocimiento9c: bool = False
    conocimiento10: Optional[str] = None
    conocimiento10c: bool = False

    # --- CALIFICACION (1-5) ---
    calificacion1: Optional[str] = None
    calificacion1c: bool = False
    calificacion2: Optional[str] = None
    calificacion2c: bool = False
    calificacion3: Optional[str] = None
    calificacion3c: bool = False
    calificacion4: Optional[str] = None
    calificacion4c: bool = False
    calificacion5: Optional[str] = None
    calificacion5c: bool = False

class PA_PE_RQUpdate(PA_PE_RQCreate):
    # En update, todo es opcional, incluso lo que era obligatorio en create
    cargo_req: Optional[str] = None
    aprobado_vigente: Optional[bool] = None

class PA_PE_RQRead(PA_PE_RQCreate):
    id: int

# =============================================================================
# 8. SEGUIMIENTO Y EVALUACIÓN (PA_PE_SE)
# =============================================================================
class PA_PE_SECreate(PersonalBase):
    responsable: Optional[str] = None # FK
    fecha: Optional[datetime] = None
    personal: Optional[str] = None # FK
    cargo: Optional[str] = None # FK
    requisitos: Optional[int] = None # FK a PA_PE_RQ
    
    # IMPORTANTE: Hemos omitido doc1...doc5 (LargeBinary) intencionalmente

    # --- EDUCACION (String Eval + Bool Cumple + Int Nota) ---
    ev_educacion1: Optional[str] = None
    cumple_educacion1: bool = False
    educacion1n: int = 0
    ev_educacion2: Optional[str] = None
    cumple_educacion2: bool = False
    educacion2n: int = 0
    ev_educacion3: Optional[str] = None
    cumple_educacion3: bool = False
    educacion3n: int = 0

    # --- FORMACION (String Eval + Bool Cumple + Int Nota) ---
    ev_formacion1: Optional[str] = None
    cumple_formacion1: bool = False
    formacion1n: int = 0
    ev_formacion2: Optional[str] = None
    cumple_formacion2: bool = False
    formacion2n: int = 0
    ev_formacion3: Optional[str] = None
    cumple_formacion3: bool = False
    formacion3n: int = 0
    ev_formacion4: Optional[str] = None
    cumple_formacion4: bool = False
    formacion4n: int = 0
    ev_formacion5: Optional[str] = None
    cumple_formacion5: bool = False
    formacion5n: int = 0
    ev_formacion6: Optional[str] = None
    cumple_formacion6: bool = False
    formacion6n: int = 0
    ev_formacion7: Optional[str] = None
    cumple_formacion7: bool = False
    formacion7n: int = 0
    ev_formacion8: Optional[str] = None
    cumple_formacion8: bool = False
    formacion8n: int = 0
    ev_formacion9: Optional[str] = None
    cumple_formacion9: bool = False
    formacion9n: int = 0
    ev_formacion10: Optional[str] = None
    cumple_formacion10: bool = False
    formacion10n: int = 0

    # --- EXPERIENCIA ---
    ev_experiencia1: Optional[str] = None
    cumple_experiencia1: bool = False
    experiencia1n: int = 0
    ev_experiencia2: Optional[str] = None
    cumple_experiencia2: bool = False
    experiencia2n: int = 0
    ev_experiencia3: Optional[str] = None
    cumple_experiencia3: bool = False
    experiencia3n: int = 0
    ev_experiencia4: Optional[str] = None
    cumple_experiencia4: bool = False
    experiencia4n: int = 0
    ev_experiencia5: Optional[str] = None
    cumple_experiencia5: bool = False
    experiencia5n: int = 0

    # --- HABILIDADES ---
    ev_habilidades1: Optional[str] = None
    cumple_habilidades1: bool = False
    habilidades1n: int = 0
    ev_habilidades2: Optional[str] = None
    cumple_habilidades2: bool = False
    habilidades2n: int = 0
    ev_habilidades3: Optional[str] = None
    cumple_habilidades3: bool = False
    habilidades3n: int = 0
    ev_habilidades4: Optional[str] = None
    cumple_habilidades4: bool = False
    habilidades4n: int = 0
    ev_habilidades5: Optional[str] = None
    cumple_habilidades5: bool = False
    habilidades5n: int = 0
    ev_habilidades6: Optional[str] = None
    cumple_habilidades6: bool = False
    habilidades6n: int = 0
    ev_habilidades7: Optional[str] = None
    cumple_habilidades7: bool = False
    habilidades7n: int = 0
    ev_habilidades8: Optional[str] = None
    cumple_habilidades8: bool = False
    habilidades8n: int = 0
    ev_habilidades9: Optional[str] = None
    cumple_habilidades9: bool = False
    habilidades9n: int = 0
    ev_habilidades10: Optional[str] = None
    cumple_habilidades10: bool = False
    habilidades10n: int = 0

    # --- CONOCIMIENTO ---
    ev_conocimiento1: Optional[str] = None
    cumple_conocimiento1: bool = False
    conocimiento1n: int = 0
    ev_conocimiento2: Optional[str] = None
    cumple_conocimiento2: bool = False
    conocimiento2n: int = 0
    ev_conocimiento3: Optional[str] = None
    cumple_conocimiento3: bool = False
    conocimiento3n: int = 0
    ev_conocimiento4: Optional[str] = None
    cumple_conocimiento4: bool = False
    conocimiento4n: int = 0
    ev_conocimiento5: Optional[str] = None
    cumple_conocimiento5: bool = False
    conocimiento5n: int = 0
    ev_conocimiento6: Optional[str] = None
    cumple_conocimiento6: bool = False
    conocimiento6n: int = 0
    ev_conocimiento7: Optional[str] = None
    cumple_conocimiento7: bool = False
    conocimiento7n: int = 0
    ev_conocimiento8: Optional[str] = None
    cumple_conocimiento8: bool = False
    conocimiento8n: int = 0
    ev_conocimiento9: Optional[str] = None
    cumple_conocimiento9: bool = False
    conocimiento9n: int = 0
    ev_conocimiento10: Optional[str] = None
    cumple_conocimiento10: bool = False
    conocimiento10n: int = 0

    # --- CALIFICACION ---
    ev_calificacion1: Optional[str] = None
    cumple_calificacion1: bool = False
    calificacion1n: int = 0
    ev_calificacion2: Optional[str] = None
    cumple_calificacion2: bool = False
    calificacion2n: int = 0
    ev_calificacion3: Optional[str] = None
    cumple_calificacion3: bool = False
    calificacion3n: int = 0
    ev_calificacion4: Optional[str] = None
    cumple_calificacion4: bool = False
    calificacion4n: int = 0
    ev_calificacion5: Optional[str] = None
    cumple_calificacion5: bool = False
    calificacion5n: int = 0

    # RESULTADOS
    promedio: float = 0
    escala: int = 0
    conclusion: Optional[str] = None
    competencia_asegurada: bool = False

class PA_PE_SEUpdate(PA_PE_SECreate):
    pass

class PA_PE_SERead(PA_PE_SECreate):
    id: int
# =============================================================================
# 9. SELECCIÓN DE PUESTO (PA_PE_SP)
# =============================================================================
class PA_PE_SPCreate(PersonalBase):
    puesto: str # FK a PA_PE_DE.abreviacion (El cargo)
    fecha_inicial: Optional[datetime] = None
    fecha_final: Optional[datetime] = None
    evaluadores: Optional[str] = None # FK a PA_PE_PE.abreviatura
    
    # Ponderaciones CV
    ponderacion_educacion: float = 0
    ponderacion_formacion: float = 0
    ponderacion_habilidades: float = 0
    ponderacion_experiencia: float = 0
    ponderacion_conocimientotecnico: float = 0
    
    ponderacion_calificacion: float = 0 # Media total esperada
    ponderacion_minima_cv: float = 0    # Umbral pase
    
    conclusion_cv: Optional[str] = None # Comentarios generales del proceso

    # Configuración Entrevista (Definición de qué evaluar)
    item_entrevista_1: Optional[str] = None
    ponderacion_entrevista_1: float = 0
    
    item_entrevista_2: Optional[str] = None
    ponderacion_entrevista_2: float = 0
    
    item_entrevista_3: Optional[str] = None
    ponderacion_entrevista_3: float = 0
    
    item_entrevista_4: Optional[str] = None
    ponderacion_entrevista_4: float = 0
    
    item_entrevista_5: Optional[str] = None
    ponderacion_entrevista_5: float = 0

    ponderacion_minima_entrevista: float = 0 # Umbral selección
    conclusion_entrevista: Optional[str] = None

class PA_PE_SPUpdate(PersonalBase):
    # Datos Generales
    puesto: Optional[str] = None
    evaluadores: Optional[str] = None
    fecha_inicial: Optional[datetime] = None
    fecha_final: Optional[datetime] = None
    
    # Ponderaciones CV
    ponderacion_educacion: Optional[float] = None
    ponderacion_formacion: Optional[float] = None
    ponderacion_habilidades: Optional[float] = None
    ponderacion_experiencia: Optional[float] = None
    ponderacion_conocimientotecnico: Optional[float] = None
    
    ponderacion_minima_cv: Optional[float] = None
    conclusion_cv: Optional[str] = None

    # Configuración Entrevista
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

class PA_PE_SPRead(PA_PE_SPCreate):
    id: int

# =============================================================================
# 10. POSTULANTES (PA_PE_PO)
# =============================================================================
class PA_PE_POCreate(PersonalBase):
    proceso_de_seleccion: int # FK a PA_PE_SP.id
    postulante: str # Nombre del candidato (Externo)
    
    # Notas CV (0 a 100 usualmente)
    educacion: float = 0
    formacion: float = 0
    experiencia: float = 0
    habilidades: float = 0
    conocimientotecnico: float = 0
    
    resultado_cv: float = 0       # Resultado calculado ponderado
    pasa_a_entrevista: bool = False
    
    # Notas Entrevista (Según los items definidos en SP)
    item_entrevista1: float = 0 # Nota para el item_entrevista_1 del padre
    item_entrevista2: float = 0
    item_entrevista3: float = 0
    item_entrevista4: float = 0
    item_entrevista5: float = 0
    
    resultado_entrevista: float = 0 # Resultado calculado ponderado
    calificacion: float = 0         # Nota final global (si aplica)
    
    seleccionado: bool = False      # Ganador

class PA_PE_POUpdate(PersonalBase):
    # Todo editable para calificar
    educacion: Optional[float] = None
    formacion: Optional[float] = None
    experiencia: Optional[float] = None
    habilidades: Optional[float] = None
    conocimientotecnico: Optional[float] = None
    
    resultado_cv: Optional[float] = None
    pasa_a_entrevista: Optional[bool] = None
    
    item_entrevista1: Optional[float] = None
    item_entrevista2: Optional[float] = None
    item_entrevista3: Optional[float] = None
    item_entrevista4: Optional[float] = None
    item_entrevista5: Optional[float] = None
    
    resultado_entrevista: Optional[float] = None
    calificacion: Optional[float] = None
    seleccionado: Optional[bool] = None

class PA_PE_PORead(PA_PE_POCreate):
    id: int

# =============================================================================
# 11. PROGRAMA (PA_PE_PR)
# =============================================================================
class PA_PE_PRCreate(PersonalBase):
    registrado_por: Optional[str] = None
    dirigido_a: Optional[str] = Field(None, alias="dirigido_a") # Alias para mapear con BD
    actividad: Optional[str] = None
    competencia_por_adquirir: Optional[str] = None
    fecha_programada: Optional[datetime] = None
    comentarios: Optional[str] = None

class PA_PE_PRUpdate(PA_PE_PRCreate):
    pass

class PA_PE_PRRead(PA_PE_PRCreate):
    id: int

# =============================================================================
# 12. PLANIFICACIÓN (PA_PE_PL)
# =============================================================================
class PA_PE_PLCreate(PersonalBase):
    item_del_programa: Optional[int] = None
    elaborado_por: Optional[str] = None
    fecha_inicio: Optional[datetime] = None
    forma_generacion: Optional[int] = None
    responsable_de_generacion_de_competencia: Optional[str] = None
    tematica: Optional[str] = None
    asistentes: Optional[str] = None
    comentarios_de_la_generacion_de_competencia: Optional[str] = None
    evaluacion_si_aplica: Optional[float] = None
    conclusion: Optional[str] = None
    respaldo1: Optional[str] = None
    respaldo2: Optional[str] = None
    respaldo3: Optional[str] = None
    competencia: bool = False
    fecha_final: Optional[datetime] = None

class PA_PE_PLUpdate(PA_PE_PLCreate):
    pass

class PA_PE_PLRead(PA_PE_PLCreate):
    id: int
# =============================================================================
# 13. OTROS (Tablas pequeñas FG, IE, IS, SU, TP)
# =============================================================================

# Forma de Generación
class PA_PE_FGCreate(PersonalBase):
    forma_de_generacion: Optional[str] = None
class PA_PE_FGUpdate(PersonalBase):
    forma_de_generacion: Optional[str] = None
class PA_PE_FGRead(PA_PE_FGCreate):
    id: int

# Inducción Específica
class PA_PE_IECreate(PersonalBase):
    id_is: Optional[int] = None
    cargo: Optional[str] = None
    item: Optional[str] = None
    actividad: Optional[str] = None
class PA_PE_IEUpdate(PersonalBase):
    actividad: Optional[str] = None
class PA_PE_IERead(PA_PE_IECreate):
    id: int

# Inducción Sistema
class PA_PE_ISCreate(PersonalBase):
    cargo: Optional[str] = None
    item: Optional[str] = None
    comentarios: Optional[str] = None
class PA_PE_ISUpdate(PersonalBase):
    comentarios: Optional[str] = None
class PA_PE_ISRead(PA_PE_ISCreate):
    id: int

# =============================================================================
# 13. SUPERVISIÓN DE PERSONAL (PA_PE_SU)
# =============================================================================

class PA_PE_SUBase(BaseModel):
    fecha: Optional[datetime] = None
    supervisores: Optional[str] = None  # FK
    supervisados: Optional[str] = None  # FK
    cargo: Optional[str] = None
    item: Optional[str] = None # Actividad
    comentarios: Optional[str] = None
    requiere_adquirir_o_aumentar_competencia: bool = False

    # Items 1-10
    item_de_supervision_1: Optional[str] = None
    supervision_exitosa_1: bool = False
    item_de_supervision_2: Optional[str] = None
    supervision_exitosa_2: bool = False
    item_de_supervision_3: Optional[str] = None
    supervision_exitosa_3: bool = False
    item_de_supervision_4: Optional[str] = None
    supervision_exitosa_4: bool = False
    item_de_supervision_5: Optional[str] = None
    supervision_exitosa_5: bool = False
    item_de_supervision_6: Optional[str] = None
    supervision_exitosa_6: bool = False
    item_de_supervision_7: Optional[str] = None
    supervision_exitosa_7: bool = False
    item_de_supervision_8: Optional[str] = None
    supervision_exitosa_8: bool = False
    item_de_supervision_9: Optional[str] = None
    supervision_exitosa_9: bool = False
    item_de_supervision_10: Optional[str] = None
    supervision_exitosa_10: bool = False

class PA_PE_SUCreate(PA_PE_SUBase):
    pass

class PA_PE_SUUpdate(PA_PE_SUBase):
    pass

class PA_PE_SURead(PA_PE_SUBase):
    id: int
    
    # Opcional: Si quieres devolver los nombres de las personas en el GET
    # supervisores_rel: Optional[PA_PE_PERead] = None
    # supervisados_rel: Optional[PA_PE_PERead] = None

    class Config:
        from_attributes = True

# Test/Prueba (TP)
class PA_PE_TPCreate(PersonalBase):
    nombre: Optional[str] = None
    cargo: Optional[str] = None
    parametro_a_evaluar: Optional[int] = None
    valor_medido: Optional[int] = None
class PA_PE_TPUpdate(PersonalBase):
    valor_medido: Optional[int] = None
class PA_PE_TPRead(PA_PE_TPCreate):
    id: int