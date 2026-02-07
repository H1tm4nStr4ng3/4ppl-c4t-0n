"""
FastAPI Application - SGApp Backend
Versión 2.0 - COMPLETA con TODAS las 98 tablas
"""
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import SQLAlchemyError
import time
import logging

from app.core.config import settings
from app.api.router_factory import create_crud_router

# Importar TODOS los modelos
# from app.models import *

# Importar TODOS los schemas
# from app.schemas import *
from app import models
from app import schemas

# Configurar logging
logging.basicConfig(
    level=getattr(logging, settings.LOG_LEVEL),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Crear aplicación
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="API RESTful para Sistema de Gestión de Calidad - 98 Entidades",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# ============== MIDDLEWARE ==============

# CORS
app.add_middleware(
    CORSMiddleware,
#    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Compresión GZIP
app.add_middleware(GZipMiddleware, minimum_size=1000)


# Middleware de logging de requests
@app.middleware("http")
async def log_requests(request: Request, call_next):
    """Middleware para logging de requests"""
    start_time = time.time()
    
    # Log request
    logger.info(f"Request: {request.method} {request.url.path}")
    
    # Procesar request
    response = await call_next(request)
    
    # Log response
    process_time = time.time() - start_time
    logger.info(f"Response: {response.status_code} - Time: {process_time:.3f}s")
    
    # Agregar header de tiempo de procesamiento
    response.headers["X-Process-Time"] = str(process_time)
    
    return response


# ============== EXCEPTION HANDLERS ==============

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Manejador de errores de validación"""
    logger.error(f"Validation error: {exc.errors()}")
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "error": "Validation Error",
            "message": "Los datos proporcionados no son válidos",
            "detail": exc.errors()
        }
    )


@app.exception_handler(SQLAlchemyError)
async def sqlalchemy_exception_handler(request: Request, exc: SQLAlchemyError):
    """Manejador de errores de base de datos"""
    logger.error(f"Database error: {str(exc)}")
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "error": "Database Error",
            "message": "Error al procesar la operación en la base de datos",
            "detail": str(exc) if settings.LOG_LEVEL == "DEBUG" else None
        }
    )


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    """Manejador general de errores"""
    logger.error(f"Unexpected error: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "error": "Internal Server Error",
            "message": "Ha ocurrido un error inesperado",
            "detail": str(exc) if settings.LOG_LEVEL == "DEBUG" else None
        }
    )


# ============== ENDPOINTS PRINCIPALES ==============

@app.get("/", tags=["Root"])
async def root():
    """Endpoint raíz de la API"""
    return {
        "message": "SGApp API - Sistema de Gestión de Calidad",
        "version": settings.VERSION,
        "status": "active",
        "total_endpoints": 98 * 5,  # 98 tablas x 5 endpoints cada una
        "docs": "/docs",
        "redoc": "/redoc"
    }


@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "version": settings.VERSION
    }


# ============== REGISTRO DE TODOS LOS ROUTERS ==============
# Fallas y Eventos
app.include_router(
    create_crud_router(
        model=models.PA_DI_FA,
        schema=schemas.PA_DI_FA,
        create_schema=schemas.PA_DI_FACreate,
        update_schema=schemas.PA_DI_FAUpdate,
        prefix=f"{settings.API_V1_STR}/pa-di-fa",
        tags=["PA_DI_FA: Fallas y Eventos"]
    )
)
# Procesos
app.include_router(
    create_crud_router(
        model=models.PA_DI_PR,
        schema=schemas.PA_DI_PR,
        create_schema=schemas.PA_DI_PRCreate,
        update_schema=schemas.PA_DI_PRUpdate,
        prefix=f"{settings.API_V1_STR}/pa-di-pr",
        tags=["PA_DI_PR: Procesos"]
    )
)
# Registro de Actualización
app.include_router(
    create_crud_router(
        model=models.PA_DI_RA,
        schema=schemas.PA_DI_RA,
        create_schema=schemas.PA_DI_RACreate,
        update_schema=schemas.PA_DI_RAUpdate,
        prefix=f"{settings.API_V1_STR}/pa-di-ra",
        tags=["PA_DI_RA: Registro de Actualización"]
    )
)
# Actividades de Equipamiento
app.include_router(
    create_crud_router(
        model=models.PA_EQ_AC,
        schema=schemas.PA_EQ_AC,
        create_schema=schemas.PA_EQ_ACCreate,
        update_schema=schemas.PA_EQ_ACUpdate,
        prefix=f"{settings.API_V1_STR}/pa-eq-ac",
        tags=["PA_EQ_AC: Actividades de Equipamiento"]
    )
)
# Calibraciones
app.include_router(
    create_crud_router(
        model=models.PA_EQ_CA,
        schema=schemas.PA_EQ_CA,
        create_schema=schemas.PA_EQ_CACreate,
        update_schema=schemas.PA_EQ_CAUpdate,
        prefix=f"{settings.API_V1_STR}/pa-eq-ca",
        tags=["PA_EQ_CA: Calibraciones"]
    )
)
# Comprobación de Balanzas
app.include_router(
    create_crud_router(
        model=models.PA_EQ_CB,
        schema=schemas.PA_EQ_CB,
        create_schema=schemas.PA_EQ_CBCreate,
        update_schema=schemas.PA_EQ_CBUpdate,
        prefix=f"{settings.API_V1_STR}/pa-eq-cb",
        tags=["PA_EQ_CB: Comprobación de Balanzas"]
    )
)
# Comprobación de Hornos
app.include_router(
    create_crud_router(
        model=models.PA_EQ_CH,
        schema=schemas.PA_EQ_CH,
        create_schema=schemas.PA_EQ_CHCreate,
        update_schema=schemas.PA_EQ_CHUpdate,
        prefix=f"{settings.API_V1_STR}/pa-eq-ch",
        tags=["PA_EQ_CH: Comprobación de Hornos"]
    )
)
# Comprobaciones Intermedias
app.include_router(
    create_crud_router(
        model=models.PA_EQ_CI,
        schema=schemas.PA_EQ_CI,
        create_schema=schemas.PA_EQ_CICreate,
        update_schema=schemas.PA_EQ_CIUpdate,
        prefix=f"{settings.API_V1_STR}/pa-eq-ci",
        tags=["PA_EQ_CI: Comprobaciones Intermedias"]
    )
)
# Comprobación de Volumen
app.include_router(
    create_crud_router(
        model=models.PA_EQ_CV,
        schema=schemas.PA_EQ_CV,
        create_schema=schemas.PA_EQ_CVCreate,
        update_schema=schemas.PA_EQ_CVUpdate,
        prefix=f"{settings.API_V1_STR}/pa-eq-cv",
        tags=["PA_EQ_CV: Comprobación de Volumen"]
    )
)
# Datos de Calibración
app.include_router(
    create_crud_router(
        model=models.PA_EQ_DC,
        schema=schemas.PA_EQ_DC,
        create_schema=schemas.PA_EQ_DCCreate,
        update_schema=schemas.PA_EQ_DCUpdate,
        prefix=f"{settings.API_V1_STR}/pa-eq-dc",
        tags=["PA_EQ_DC: Datos de Calibración"]
    )
)
# Equipamiento
app.include_router(
    create_crud_router(
        model=models.PA_EQ_EQ,
        schema=schemas.PA_EQ_EQ,
        create_schema=schemas.PA_EQ_EQCreate,
        update_schema=schemas.PA_EQ_EQUpdate,
        prefix=f"{settings.API_V1_STR}/pa-eq-eq",
        tags=["PA_EQ_EQ: Equipamiento"]
    )
)
# Excentricidad
app.include_router(
    create_crud_router(
        model=models.PA_EQ_EX,
        schema=schemas.PA_EQ_EX,
        create_schema=schemas.PA_EQ_EXCreate,
        update_schema=schemas.PA_EQ_EXUpdate,
        prefix=f"{settings.API_V1_STR}/pa-eq-ex",
        tags=["PA_EQ_EX: Excentricidad"]
    )
)
# Homogeneidad de Temperatura
app.include_router(
    create_crud_router(
        model=models.PA_EQ_HM,
        schema=schemas.PA_EQ_HM,
        create_schema=schemas.PA_EQ_HMCreate,
        update_schema=schemas.PA_EQ_HMUpdate,
        prefix=f"{settings.API_V1_STR}/pa-eq-hm",
        tags=["PA_EQ_HM: Homogeneidad de Temperatura"]
    )
)
# Lecturas de Equipos
app.include_router(
    create_crud_router(
        model=models.PA_EQ_LE,
        schema=schemas.PA_EQ_LE,
        create_schema=schemas.PA_EQ_LECreate,
        update_schema=schemas.PA_EQ_LEUpdate,
        prefix=f"{settings.API_V1_STR}/pa-eq-le",
        tags=["PA_EQ_LE: Lecturas de Equipos"]
    )
)
# Mantenimiento
app.include_router(
    create_crud_router(
        model=models.PA_EQ_MA,
        schema=schemas.PA_EQ_MA,
        create_schema=schemas.PA_EQ_MACreate,
        update_schema=schemas.PA_EQ_MAUpdate,
        prefix=f"{settings.API_V1_STR}/pa-eq-ma",
        tags=["PA_EQ_MA: Mantenimiento"]
    )
)
# Movimientos
app.include_router(
    create_crud_router(
        model=models.PA_EQ_MO,
        schema=schemas.PA_EQ_MO,
        create_schema=schemas.PA_EQ_MOCreate,
        update_schema=schemas.PA_EQ_MOUpdate,
        prefix=f"{settings.API_V1_STR}/pa-eq-mo",
        tags=["PA_EQ_MO: Movimientos"]
    )
)
# Material de Referencia
app.include_router(
    create_crud_router(
        model=models.PA_EQ_MR,
        schema=schemas.PA_EQ_MRRead,
        create_schema=schemas.PA_EQ_MRCreate,
        update_schema=schemas.PA_EQ_MRUpdate,
        prefix=f"{settings.API_V1_STR}/pa-eq-mr",
        tags=["PA_EQ_MR: Material de Referencia"]
    )
)
# Movimientos de Volumen
app.include_router(
    create_crud_router(
        model=models.PA_EQ_MV,
        schema=schemas.PA_EQ_MV,
        create_schema=schemas.PA_EQ_MVCreate,
        update_schema=schemas.PA_EQ_MVUpdate,
        prefix=f"{settings.API_V1_STR}/pa-eq-mv",
        tags=["PA_EQ_MV: Movimientos de Volumen"]
    )
)
# Patrones
app.include_router(
    create_crud_router(
        model=models.PA_EQ_PA,
        schema=schemas.PA_EQ_PA,
        create_schema=schemas.PA_EQ_PACreate,
        update_schema=schemas.PA_EQ_PAUpdate,
        prefix=f"{settings.API_V1_STR}/pa-eq-pa",
        tags=["PA_EQ_PA: Patrones"]
    )
)
# Proveedores
app.include_router(
    create_crud_router(
        model=models.PA_EQ_PR,
        schema=schemas.PA_EQ_PR,
        create_schema=schemas.PA_EQ_PRCreate,
        update_schema=schemas.PA_EQ_PRUpdate,
        prefix=f"{settings.API_V1_STR}/pa-eq-pr",
        tags=["PA_EQ_PR: Proveedores"]
    )
)
# Registros de Equipos
app.include_router(
    create_crud_router(
        model=models.PA_EQ_RE,
        schema=schemas.PA_EQ_RECreate,
        create_schema=schemas.PA_EQ_RECreate,
        update_schema=schemas.PA_EQ_REUpdate,
        prefix=f"{settings.API_V1_STR}/pa-eq-re",
        tags=["PA_EQ_RE: Registros de Equipos"]
    )
)
# Repetibilidad
app.include_router(
    create_crud_router(
        model=models.PA_EQ_RP,
        schema=schemas.PA_EQ_RP,
        create_schema=schemas.PA_EQ_RPCreate,
        update_schema=schemas.PA_EQ_RPUpdate,
        prefix=f"{settings.API_V1_STR}/pa-eq-rp",
        tags=["PA_EQ_RP: Repetibilidad"]
    )
)
# Verificaciones
app.include_router(
    create_crud_router(
        model=models.PA_EQ_VE,
        schema=schemas.PA_EQ_VE,
        create_schema=schemas.PA_EQ_VECreate,
        update_schema=schemas.PA_EQ_VEUpdate,
        prefix=f"{settings.API_V1_STR}/pa-eq-ve",
        tags=["PA_EQ_VE: Verificaciones"]
    )
)
# Análisis de Humedad
app.include_router(
    create_crud_router(
        model=models.PA_IA_AH,
        schema=schemas.PA_IA_AH,
        create_schema=schemas.PA_IA_AHCreate,
        update_schema=schemas.PA_IA_AHUpdate,
        prefix=f"{settings.API_V1_STR}/pa-ia-ah",
        tags=["PA_IA_AH: Análisis de Humedad"]
    )
)
# Análisis de Materiales
app.include_router(
    create_crud_router(
        model=models.PA_IA_AM,
        schema=schemas.PA_IA_AM,
        create_schema=schemas.PA_IA_AMCreate,
        update_schema=schemas.PA_IA_AMUpdate,
        prefix=f"{settings.API_V1_STR}/pa-ia-am",
        tags=["PA_IA_AM: Análisis de Materiales"]
    )
)
# Análisis de Resultados
app.include_router(
    create_crud_router(
        model=models.PA_IA_AR,
        schema=schemas.PA_IA_AR,
        create_schema=schemas.PA_IA_ARCreate,
        update_schema=schemas.PA_IA_ARUpdate,
        prefix=f"{settings.API_V1_STR}/pa-ia-ar",
        tags=["PA_IA_AR: Análisis de Resultados"]
    )
)
# Calibración de Análisis
app.include_router(
    create_crud_router(
        model=models.PA_IA_CA,
        schema=schemas.PA_IA_CA,
        create_schema=schemas.PA_IA_CACreate,
        update_schema=schemas.PA_IA_CAUpdate,
        prefix=f"{settings.API_V1_STR}/pa-ia-ca",
        tags=["PA_IA_CA: Calibración de Análisis"]
    )
)
# Lectura de Análisis
app.include_router(
    create_crud_router(
        model=models.PA_IA_LE,
        schema=schemas.PA_IA_LE,
        create_schema=schemas.PA_IA_LECreate,
        update_schema=schemas.PA_IA_LEUpdate,
        prefix=f"{settings.API_V1_STR}/pa-ia-le",
        tags=["PA_IA_LE: Lectura de Análisis"]
    )
)
# Lista de Análisis
app.include_router(
    create_crud_router(
        model=models.PA_IA_LI,
        schema=schemas.PA_IA_LI,
        create_schema=schemas.PA_IA_LICreate,
        update_schema=schemas.PA_IA_LIUpdate,
        prefix=f"{settings.API_V1_STR}/pa-ia-li",
        tags=["PA_IA_LI: Lista de Análisis"]
    )
)
# Rango de Análisis
app.include_router(
    create_crud_router(
        model=models.PA_IA_RA,
        schema=schemas.PA_IA_RA,
        create_schema=schemas.PA_IA_RACreate,
        update_schema=schemas.PA_IA_RAUpdate,
        prefix=f"{settings.API_V1_STR}/pa-ia-ra",
        tags=["PA_IA_RA: Rango de Análisis"]
    )
)
# Resultados Intermedios
app.include_router(
    create_crud_router(
        model=models.PA_IA_RI,
        schema=schemas.PA_IA_RI,
        create_schema=schemas.PA_IA_RICreate,
        update_schema=schemas.PA_IA_RIUpdate,
        prefix=f"{settings.API_V1_STR}/pa-ia-ri",
        tags=["PA_IA_RI: Resultados Intermedios"]
    )
)
# Salida de Análisis
app.include_router(
    create_crud_router(
        model=models.PA_IA_SA,
        schema=schemas.PA_IA_SA,
        create_schema=schemas.PA_IA_SACreate,
        update_schema=schemas.PA_IA_SAUpdate,
        prefix=f"{settings.API_V1_STR}/pa-ia-sa",
        tags=["PA_IA_SA: Salida de Análisis"]
    )
)
# Sistema de Información de Análisis
app.include_router(
    create_crud_router(
        model=models.PA_IA_SI,
        schema=schemas.PA_IA_SI,
        create_schema=schemas.PA_IA_SICreate,
        update_schema=schemas.PA_IA_SIUpdate,
        prefix=f"{settings.API_V1_STR}/pa-ia-si",
        tags=["PA_IA_SI: Sistema de Información de Análisis"]
    )
)
# Auditorías
app.include_router(
    create_crud_router(
        model=models.PA_PE_AU,
        schema=schemas.PA_PE_AU,
        create_schema=schemas.PA_PE_AUCreate,
        update_schema=schemas.PA_PE_AUUpdate,
        prefix=f"{settings.API_V1_STR}/pa-pe-au",
        tags=["PA_PE_AU: Auditorías"]
    )
)
# Comunicaciones y Versiones
app.include_router(
    create_crud_router(
        model=models.PA_PE_CV,
        schema=schemas.PA_PE_CV,
        create_schema=schemas.PA_PE_CVCreate,
        update_schema=schemas.PA_PE_CVUpdate,
        prefix=f"{settings.API_V1_STR}/pa-pe-cv",
        tags=["PA_PE_CV: Comunicaciones y Versiones"]
    )
)
# Desarrollo de Ensayos
app.include_router(
    create_crud_router(
        model=models.PA_PE_DE,
        schema=schemas.PA_PE_DE,
        create_schema=schemas.PA_PE_DECreate,
        update_schema=schemas.PA_PE_DEUpdate,
        prefix=f"{settings.API_V1_STR}/pa-pe-de",
        tags=["PA_PE_DE: Definición de cargos"]
    )
)
# Evaluación de Calidad
app.include_router(
    create_crud_router(
        model=models.PA_PE_EC,
        schema=schemas.PA_PE_EC,
        create_schema=schemas.PA_PE_ECCreate,
        update_schema=schemas.PA_PE_ECUpdate,
        prefix=f"{settings.API_V1_STR}/pa-pe-ec",
        tags=["PA_PE_EC: Evaluación de Calidad"]
    )
)
# Efectividad
app.include_router(
    create_crud_router(
        model=models.PA_PE_EF,
        schema=schemas.PA_PE_EF,
        create_schema=schemas.PA_PE_EFCreate,
        update_schema=schemas.PA_PE_EFUpdate,
        prefix=f"{settings.API_V1_STR}/pa-pe-ef",
        tags=["PA_PE_EF: Efectividad"]
    )
)
# Formatos y Gráficos
app.include_router(
    create_crud_router(
        model=models.PA_PE_FG,
        schema=schemas.PA_PE_FG,
        create_schema=schemas.PA_PE_FGCreate,
        update_schema=schemas.PA_PE_FGUpdate,
        prefix=f"{settings.API_V1_STR}/pa-pe-fg",
        tags=["PA_PE_FG: Formatos y Gráficos"]
    )
)
# Inspecciones Externas
app.include_router(
    create_crud_router(
        model=models.PA_PE_IE,
        schema=schemas.PA_PE_IE,
        create_schema=schemas.PA_PE_IECreate,
        update_schema=schemas.PA_PE_IEUpdate,
        prefix=f"{settings.API_V1_STR}/pa-pe-ie",
        tags=["PA_PE_IE: Inspecciones Externas"]
    )
)
# Inspecciones
app.include_router(
    create_crud_router(
        model=models.PA_PE_IS,
        schema=schemas.PA_PE_IS,
        create_schema=schemas.PA_PE_ISCreate,
        update_schema=schemas.PA_PE_ISUpdate,
        prefix=f"{settings.API_V1_STR}/pa-pe-is",
        tags=["PA_PE_IS: Inspecciones"]
    )
)
# Personal
app.include_router(
    create_crud_router(
        model=models.PA_PE_PE,
        schema=schemas.PA_PE_PE,
        create_schema=schemas.PA_PE_PECreate,
        update_schema=schemas.PA_PE_PEUpdate,
        prefix=f"{settings.API_V1_STR}/pa-pe-pe",
        tags=["PA_PE_PE: Personal"]
    )
)
# Planificación
app.include_router(
    create_crud_router(
        model=models.PA_PE_PL,
        schema=schemas.PA_PE_PL,
        create_schema=schemas.PA_PE_PLCreate,
        update_schema=schemas.PA_PE_PLUpdate,
        prefix=f"{settings.API_V1_STR}/pa-pe-pl",
        tags=["PA_PE_PL: Planificación"]
    )
)
# Políticas
app.include_router(
    create_crud_router(
        model=models.PA_PE_PO,
        schema=schemas.PA_PE_PO,
        create_schema=schemas.PA_PE_POCreate,
        update_schema=schemas.PA_PE_POUpdate,
        prefix=f"{settings.API_V1_STR}/pa-pe-po",
        tags=["PA_PE_PO: Políticas"]
    )
)
# Procesos de Ensayo
app.include_router(
    create_crud_router(
        model=models.PA_PE_PR,
        schema=schemas.PA_PE_PR,
        create_schema=schemas.PA_PE_PRCreate,
        update_schema=schemas.PA_PE_PRUpdate,
        prefix=f"{settings.API_V1_STR}/pa-pe-pr",
        tags=["PA_PE_PR: Procesos de Ensayo"]
    )
)
# Requisitos
app.include_router(
    create_crud_router(
        model=models.PA_PE_RQ,
        schema=schemas.PA_PE_RQ,
        create_schema=schemas.PA_PE_RQCreate,
        update_schema=schemas.PA_PE_RQUpdate,
        prefix=f"{settings.API_V1_STR}/pa-pe-rq",
        tags=["PA_PE_RQ: Requisitos"]
    )
)
# Servicios
app.include_router(
    create_crud_router(
        model=models.PA_PE_SE,
        schema=schemas.PA_PE_SE,
        create_schema=schemas.PA_PE_SECreate,
        update_schema=schemas.PA_PE_SEUpdate,
        prefix=f"{settings.API_V1_STR}/pa-pe-se",
        tags=["PA_PE_SE: Servicios"]
    )
)
# Suministros y Productos
app.include_router(
    create_crud_router(
        model=models.PA_PE_SP,
        schema=schemas.PA_PE_SP,
        create_schema=schemas.PA_PE_SPCreate,
        update_schema=schemas.PA_PE_SPUpdate,
        prefix=f"{settings.API_V1_STR}/pa-pe-sp",
        tags=["PA_PE_SP: Suministros y Productos"]
    )
)
# Subcontratación
app.include_router(
    create_crud_router(
        model=models.PA_PE_SU,
        schema=schemas.PA_PE_SU,
        create_schema=schemas.PA_PE_SUCreate,
        update_schema=schemas.PA_PE_SUUpdate,
        prefix=f"{settings.API_V1_STR}/pa-pe-su",
        tags=["PA_PE_SU: Subcontratación"]
    )
)
# Tipos de Ensayo
app.include_router(
    create_crud_router(
        model=models.PA_PE_TP,
        schema=schemas.PA_PE_TP,
        create_schema=schemas.PA_PE_TPCreate,
        update_schema=schemas.PA_PE_TPUpdate,
        prefix=f"{settings.API_V1_STR}/pa-pe-tp",
        tags=["PA_PE_TP: Tipos de Ensayo"]
    )
)
# Administración
app.include_router(
    create_crud_router(
        model=models.PA_PS_AD,
        schema=schemas.PA_PS_AD,
        create_schema=schemas.PA_PS_ADCreate,
        update_schema=schemas.PA_PS_ADUpdate,
        prefix=f"{settings.API_V1_STR}/pa-ps-ad",
        tags=["PA_PS_AD: Administración"]
    )
)
# Control de Registros
app.include_router(
    create_crud_router(
        model=models.PA_PS_CR,
        schema=schemas.PA_PS_CR,
        create_schema=schemas.PA_PS_CRCreate,
        update_schema=schemas.PA_PS_CRUpdate,
        prefix=f"{settings.API_V1_STR}/pa-ps-cr",
        tags=["PA_PS_CR: Control de Registros"]
    )
)
# Desarrollo de Personal
app.include_router(
    create_crud_router(
        model=models.PA_PS_DE,
        schema=schemas.PA_PS_DE,
        create_schema=schemas.PA_PS_DECreate,
        update_schema=schemas.PA_PS_DEUpdate,
        prefix=f"{settings.API_V1_STR}/pa-ps-de",
        tags=["PA_PS_DE: Desarrollo de Personal"]
    )
)
# Evaluación de Personal
app.include_router(
    create_crud_router(
        model=models.PA_PS_EV,
        schema=schemas.PA_PS_EV,
        create_schema=schemas.PA_PS_EVCreate,
        update_schema=schemas.PA_PS_EVUpdate,
        prefix=f"{settings.API_V1_STR}/pa-ps-ev",
        tags=["PA_PS_EV: Evaluación de Personal"]
    )
)
# Observaciones
app.include_router(
    create_crud_router(
        model=models.PA_PS_OS,
        schema=schemas.PA_PS_OS,
        create_schema=schemas.PA_PS_OSCreate,
        update_schema=schemas.PA_PS_OSUpdate,
        prefix=f"{settings.API_V1_STR}/pa-ps-os",
        tags=["PA_PS_OS: Observaciones"]
    )
)
# Personal de Recursos
app.include_router(
    create_crud_router(
        model=models.PA_PS_PR,
        schema=schemas.PA_PS_PR,
        create_schema=schemas.PA_PS_PRCreate,
        update_schema=schemas.PA_PS_PRUpdate,
        prefix=f"{settings.API_V1_STR}/pa-ps-pr",
        tags=["PA_PS_PR: Personal de Recursos"]
    )
)
# Personal del Sistema
app.include_router(
    create_crud_router(
        model=models.PA_PS_PS,
        schema=schemas.PA_PS_PS,
        create_schema=schemas.PA_PS_PSCreate,
        update_schema=schemas.PA_PS_PSUpdate,
        prefix=f"{settings.API_V1_STR}/pa-ps-ps",
        tags=["PA_PS_PS: Personal del Sistema"]
    )
)
# Estado de Ensayos
app.include_router(
    create_crud_router(
        model=models.PC_ES_ES,
        schema=schemas.PC_ES_ES,
        create_schema=schemas.PC_ES_ESCreate,
        update_schema=schemas.PC_ES_ESUpdate,
        prefix=f"{settings.API_V1_STR}/pc-es-es",
        tags=["PC_ES_ES: Estado de Ensayos"]
    )
)
# Patrones de Laboratorio
app.include_router(
    create_crud_router(
        model=models.PC_LAB_PATRONES,
        schema=schemas.PC_LAB_PATRONES,
        create_schema=schemas.PC_LAB_PATRONESCreate,
        update_schema=schemas.PC_LAB_PATRONESUpdate,
        prefix=f"{settings.API_V1_STR}/pc-lab-patrones",
        tags=["PC_LAB_PATRONES: Patrones de Laboratorio"]
    )
)
# Soluciones de Laboratorio
app.include_router(
    create_crud_router(
        model=models.PC_LAB_SOLUCIONES,
        schema=schemas.PC_LAB_SOLUCIONES,
        create_schema=schemas.PC_LAB_SOLUCIONESCreate,
        update_schema=schemas.PC_LAB_SOLUCIONESUpdate,
        prefix=f"{settings.API_V1_STR}/pc-lab-soluciones",
        tags=["PC_LAB_SOLUCIONES: Soluciones de Laboratorio"]
    )
)
# Detalle de Soluciones
app.include_router(
    create_crud_router(
        model=models.PC_LAB_SOLUCIONES_DET,
        schema=schemas.PC_LAB_SOLUCIONES_DET,
        create_schema=schemas.PC_LAB_SOLUCIONES_DETCreate,
        update_schema=schemas.PC_LAB_SOLUCIONES_DETUpdate,
        prefix=f"{settings.API_V1_STR}/pc-lab-soluciones-det",
        tags=["PC_LAB_SOLUCIONES_DET: Detalle de Soluciones"]
    )
)
# Validación de Métodos
app.include_router(
    create_crud_router(
        model=models.PC_LAB_VALIDACIONMETODOS,
        schema=schemas.PC_LAB_VALIDACIONMETODOS,
        create_schema=schemas.PC_LAB_VALIDACIONMETODOSCreate,
        update_schema=schemas.PC_LAB_VALIDACIONMETODOSUpdate,
        prefix=f"{settings.API_V1_STR}/pc-lab-validacionmetodos",
        tags=["PC_LAB_VALIDACIONMETODOS: Validación de Métodos"]
    )
)
# Químicos de QR
app.include_router(
    create_crud_router(
        model=models.PC_QR_QU,
        schema=schemas.PC_QR_QU,
        create_schema=schemas.PC_QR_QUCreate,
        update_schema=schemas.PC_QR_QUUpdate,
        prefix=f"{settings.API_V1_STR}/pc-qr-qu",
        tags=["PC_QR_QU: Químicos de QR"]
    )
)
# Acciones de Resultados
app.include_router(
    create_crud_router(
        model=models.PC_RE_AC,
        schema=schemas.PC_RE_AC,
        create_schema=schemas.PC_RE_ACCreate,
        update_schema=schemas.PC_RE_ACUpdate,
        prefix=f"{settings.API_V1_STR}/pc-re-ac",
        tags=["PC_RE_AC: Acciones de Resultados"]
    )
)
# Análisis de Resultados
app.include_router(
    create_crud_router(
        model=models.PC_RE_ANALISIS,
        schema=schemas.PC_RE_ANALISIS,
        create_schema=schemas.PC_RE_ANALISISCreate,
        update_schema=schemas.PC_RE_ANALISISUpdate,
        prefix=f"{settings.API_V1_STR}/pc-re-analisis",
        tags=["PC_RE_ANALISIS: Análisis de Resultados"]
    )
)
# Control de Cambios
app.include_router(
    create_crud_router(
        model=models.PC_RE_CC,
        schema=schemas.PC_RE_CC,
        create_schema=schemas.PC_RE_CCCreate,
        update_schema=schemas.PC_RE_CCUpdate,
        prefix=f"{settings.API_V1_STR}/pc-re-cc",
        tags=["PC_RE_CC: Control de Cambios"]
    )
)
# Control de Lotes
app.include_router(
    create_crud_router(
        model=models.PC_RE_CL,
        schema=schemas.PC_RE_CL,
        create_schema=schemas.PC_RE_CLCreate,
        update_schema=schemas.PC_RE_CLUpdate,
        prefix=f"{settings.API_V1_STR}/pc-re-cl",
        tags=["PC_RE_CL: Control de Lotes"]
    )
)
# Control de Operaciones
app.include_router(
    create_crud_router(
        model=models.PC_RE_CO,
        schema=schemas.PC_RE_CO,
        create_schema=schemas.PC_RE_COCreate,
        update_schema=schemas.PC_RE_COUpdate,
        prefix=f"{settings.API_V1_STR}/pc-re-co",
        tags=["PC_RE_CO: Control de Operaciones"]
    )
)
# Muestreo
app.include_router(
    create_crud_router(
        model=models.PC_RE_MU,
        schema=schemas.PC_RE_MU,
        create_schema=schemas.PC_RE_MUCreate,
        update_schema=schemas.PC_RE_MUUpdate,
        prefix=f"{settings.API_V1_STR}/pc-re-mu",
        tags=["PC_RE_MU: Muestreo"]
    )
)
# Ofertas
app.include_router(
    create_crud_router(
        model=models.PC_RE_OF,
        schema=schemas.PC_RE_OF,
        create_schema=schemas.PC_RE_OFCreate,
        update_schema=schemas.PC_RE_OFUpdate,
        prefix=f"{settings.API_V1_STR}/pc-re-of",
        tags=["PC_RE_OF: Ofertas"]
    )
)
# Pedidos Internos
app.include_router(
    create_crud_router(
        model=models.PC_RE_PI,
        schema=schemas.PC_RE_PI,
        create_schema=schemas.PC_RE_PICreate,
        update_schema=schemas.PC_RE_PIUpdate,
        prefix=f"{settings.API_V1_STR}/pc-re-pi",
        tags=["PC_RE_PI: Pedidos Internos"]
    )
)
# Presupuestos
app.include_router(
    create_crud_router(
        model=models.PC_RE_PR,
        schema=schemas.PC_RE_PR,
        create_schema=schemas.PC_RE_PRCreate,
        update_schema=schemas.PC_RE_PRUpdate,
        prefix=f"{settings.API_V1_STR}/pc-re-pr",
        tags=["PC_RE_PR: Presupuestos"]
    )
)
# Seguimiento
app.include_router(
    create_crud_router(
        model=models.PC_RE_SE,
        schema=schemas.PC_RE_SE,
        create_schema=schemas.PC_RE_SECreate,
        update_schema=schemas.PC_RE_SEUpdate,
        prefix=f"{settings.API_V1_STR}/pc-re-se",
        tags=["PC_RE_SE: Seguimiento"]
    )
)
# Seguridad
app.include_router(
    create_crud_router(
        model=models.PC_RE_SG,
        schema=schemas.PC_RE_SG,
        create_schema=schemas.PC_RE_SGCreate,
        update_schema=schemas.PC_RE_SGUpdate,
        prefix=f"{settings.API_V1_STR}/pc-re-sg",
        tags=["PC_RE_SG: Seguridad"]
    )
)
# Historial de Seguimiento
app.include_router(
    create_crud_router(
        model=models.PC_RE_SH,
        schema=schemas.PC_RE_SH,
        create_schema=schemas.PC_RE_SHCreate,
        update_schema=schemas.PC_RE_SHUpdate,
        prefix=f"{settings.API_V1_STR}/pc-re-sh",
        tags=["PC_RE_SH: Historial de Seguimiento"]
    )
)
# Solicitudes
app.include_router(
    create_crud_router(
        model=models.PC_RE_SO,
        schema=schemas.PC_RE_SO,
        create_schema=schemas.PC_RE_SOCreate,
        update_schema=schemas.PC_RE_SOUpdate,
        prefix=f"{settings.API_V1_STR}/pc-re-so",
        tags=["PC_RE_SO: Solicitudes"]
    )
)
# Tarjetas de Control
app.include_router(
    create_crud_router(
        model=models.PC_TC_TC,
        schema=schemas.PC_TC_TC,
        create_schema=schemas.PC_TC_TCCreate,
        update_schema=schemas.PC_TC_TCUpdate,
        prefix=f"{settings.API_V1_STR}/pc-tc-tc",
        tags=["PC_TC_TC: Tarjetas de Control"]
    )
)
# Acciones de Planificación
app.include_router(
    create_crud_router(
        model=models.PE_PL_AC,
        schema=schemas.PE_PL_AC,
        create_schema=schemas.PE_PL_ACCreate,
        update_schema=schemas.PE_PL_ACUpdate,
        prefix=f"{settings.API_V1_STR}/pe-pl-ac",
        tags=["PE_PL_AC: Acciones de Planificación"]
    )
)
# Contexto de Planificación
app.include_router(
    create_crud_router(
        model=models.PE_PL_CO,
        schema=schemas.PE_PL_CO,
        create_schema=schemas.PE_PL_COCreate,
        update_schema=schemas.PE_PL_COUpdate,
        prefix=f"{settings.API_V1_STR}/pe-pl-co",
        tags=["PE_PL_CO: Contexto de Planificación"]
    )
)
# Estrategia
app.include_router(
    create_crud_router(
        model=models.PE_PL_ES,
        schema=schemas.PE_PL_ES,
        create_schema=schemas.PE_PL_ESCreate,
        update_schema=schemas.PE_PL_ESUpdate,
        prefix=f"{settings.API_V1_STR}/pe-pl-es",
        tags=["PE_PL_ES: Estrategia"]
    )
)
# Objetivos
app.include_router(
    create_crud_router(
        model=models.PE_PL_OB,
        schema=schemas.PE_PL_OB,
        create_schema=schemas.PE_PL_OBCreate,
        update_schema=schemas.PE_PL_OBUpdate,
        prefix=f"{settings.API_V1_STR}/pe-pl-ob",
        tags=["PE_PL_OB: Objetivos"]
    )
)
# Partes de Contexto
app.include_router(
    create_crud_router(
        model=models.PE_PL_PC,
        schema=schemas.PE_PL_PC,
        create_schema=schemas.PE_PL_PCCreate,
        update_schema=schemas.PE_PL_PCUpdate,
        prefix=f"{settings.API_V1_STR}/pe-pl-pc",
        tags=["PE_PL_PC: Partes de Contexto"]
    )
)
# Partes Interesadas
app.include_router(
    create_crud_router(
        model=models.PE_PL_PI,
        schema=schemas.PE_PL_PI,
        create_schema=schemas.PE_PL_PICreate,
        update_schema=schemas.PE_PL_PIUpdate,
        prefix=f"{settings.API_V1_STR}/pe-pl-pi",
        tags=["PE_PL_PI: Partes Interesadas"]
    )
)
# Planes
app.include_router(
    create_crud_router(
        model=models.PE_PL_PL,
        schema=schemas.PE_PL_PL,
        create_schema=schemas.PE_PL_PLCreate,
        update_schema=schemas.PE_PL_PLUpdate,
        prefix=f"{settings.API_V1_STR}/pe-pl-pl",
        tags=["PE_PL_PL: Planes"]
    )
)
# Riesgos y Oportunidades
app.include_router(
    create_crud_router(
        model=models.PE_PL_RO,
        schema=schemas.PE_PL_RO,
        create_schema=schemas.PE_PL_ROCreate,
        update_schema=schemas.PE_PL_ROUpdate,
        prefix=f"{settings.API_V1_STR}/pe-pl-ro",
        tags=["PE_PL_RO: Riesgos y Oportunidades"]
    )
)
# Acciones Correctivas
app.include_router(
    create_crud_router(
        model=models.PE_SE_AC,
        schema=schemas.PE_SE_AC,
        create_schema=schemas.PE_SE_ACCreate,
        update_schema=schemas.PE_SE_ACUpdate,
        prefix=f"{settings.API_V1_STR}/pe-se-ac",
        tags=["PE_SE_AC: Acciones Correctivas"]
    )
)
# Correcciones de Acciones
app.include_router(
    create_crud_router(
        model=models.PE_SE_CA,
        schema=schemas.PE_SE_CA,
        create_schema=schemas.PE_SE_CACreate,
        update_schema=schemas.PE_SE_CAUpdate,
        prefix=f"{settings.API_V1_STR}/pe-se-ca",
        tags=["PE_SE_CA: Correcciones de Acciones"]
    )
)
# Correcciones
app.include_router(
    create_crud_router(
        model=models.PE_SE_CO,
        schema=schemas.PE_SE_CO,
        create_schema=schemas.PE_SE_COCreate,
        update_schema=schemas.PE_SE_COUpdate,
        prefix=f"{settings.API_V1_STR}/pe-se-co",
        tags=["PE_SE_CO: Correcciones"]
    )
)
# Entradas de Evaluación
app.include_router(
    create_crud_router(
        model=models.PE_SE_EE,
        schema=schemas.PE_SE_EE,
        create_schema=schemas.PE_SE_EECreate,
        update_schema=schemas.PE_SE_EEUpdate,
        prefix=f"{settings.API_V1_STR}/pe-se-ee",
        tags=["PE_SE_EE: Entradas de Evaluación"]
    )
)
# Entradas
app.include_router(
    create_crud_router(
        model=models.PE_SE_EN,
        schema=schemas.PE_SE_EN,
        create_schema=schemas.PE_SE_ENCreate,
        update_schema=schemas.PE_SE_ENUpdate,
        prefix=f"{settings.API_V1_STR}/pe-se-en",
        tags=["PE_SE_EN: Entradas"]
    )
)
# Mejoras de Acciones
app.include_router(
    create_crud_router(
        model=models.PE_SE_MA,
        schema=schemas.PE_SE_MA,
        create_schema=schemas.PE_SE_MACreate,
        update_schema=schemas.PE_SE_MAUpdate,
        prefix=f"{settings.API_V1_STR}/pe-se-ma",
        tags=["PE_SE_MA: Mejoras de Acciones"]
    )
)
# Oportunidades de Mejora
app.include_router(
    create_crud_router(
        model=models.PE_SE_ME,
        schema=schemas.PE_SE_ME,
        create_schema=schemas.PE_SE_MECreate,
        update_schema=schemas.PE_SE_MEUpdate,
        prefix=f"{settings.API_V1_STR}/pe-se-me",
        tags=["PE_SE_ME: Oportunidades de Mejora"]
    )
)
# Reuniones
app.include_router(
    create_crud_router(
        model=models.PE_SE_RE,
        schema=schemas.PE_SE_RE,
        create_schema=schemas.PE_SE_RECreate,
        update_schema=schemas.PE_SE_REUpdate,
        prefix=f"{settings.API_V1_STR}/pe-se-re",
        tags=["PE_SE_RE: Reuniones"]
    )
)
# Salidas de Acciones
app.include_router(
    create_crud_router(
        model=models.PE_SE_SA,
        schema=schemas.PE_SE_SA,
        create_schema=schemas.PE_SE_SACreate,
        update_schema=schemas.PE_SE_SAUpdate,
        prefix=f"{settings.API_V1_STR}/pe-se-sa",
        tags=["PE_SE_SA: Salidas de Acciones"]
    )
)
# Salidas de Seguimiento
app.include_router(
    create_crud_router(
        model=models.PE_SE_SS,
        schema=schemas.PE_SE_SS,
        create_schema=schemas.PE_SE_SSCreate,
        update_schema=schemas.PE_SE_SSUpdate,
        prefix=f"{settings.API_V1_STR}/pe-se-ss",
        tags=["PE_SE_SS: Salidas de Seguimiento"]
    )
)
# Factores K
app.include_router(
    create_crud_router(
        model=models.SYS_FACTORESK,
        schema=schemas.SYS_FACTORESK,
        create_schema=schemas.SYS_FACTORESKCreate,
        update_schema=schemas.SYS_FACTORESKUpdate,
        prefix=f"{settings.API_V1_STR}/sys-factoresk",
        tags=["SYS_FACTORESK: Factores K"]
    )
)
# Lugares
app.include_router(
    create_crud_router(
        model=models.TBL_LUGARES,
        schema=schemas.TBL_LUGARES,
        create_schema=schemas.TBL_LUGARESCreate,
        update_schema=schemas.TBL_LUGARESUpdate,
        prefix=f"{settings.API_V1_STR}/tbl-lugares",
        tags=["TBL_LUGARES: Lugares"]
    )
)
# Posiciones de Horno
app.include_router(
    create_crud_router(
        model=models.TBL_POSICIONES_HORNO,
        schema=schemas.TBL_POSICIONES_HORNO,
        create_schema=schemas.TBL_POSICIONES_HORNOCreate,
        update_schema=schemas.TBL_POSICIONES_HORNOUpdate,
        prefix=f"{settings.API_V1_STR}/tbl-posiciones-horno",
        tags=["TBL_POSICIONES_HORNO: Posiciones de Horno"]
    )
)

logger.info(f"Application started - {settings.PROJECT_NAME} v{settings.VERSION}")
logger.info(f"Total APIs registered: 98 tables x 5 endpoints = 490 endpoints")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level=settings.LOG_LEVEL.lower()
    )
