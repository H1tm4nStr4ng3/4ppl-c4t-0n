# 🏗️ Arquitectura del Backend SGApp v2.0

## 📐 Diagrama de Arquitectura

```
┌─────────────────────────────────────────────────────────────────┐
│                         CLIENTE / FRONTEND                       │
│              (React, Angular, Vue, Mobile App, etc.)             │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            │ HTTP/HTTPS Requests
                            │
┌───────────────────────────▼─────────────────────────────────────┐
│                          NGINX / PROXY                           │
│                      (Proxy Reverso - Opcional)                  │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            │
┌───────────────────────────▼─────────────────────────────────────┐
│                      FASTAPI APPLICATION                         │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                    MIDDLEWARE LAYER                       │  │
│  │  • CORS Middleware                                        │  │
│  │  • GZIP Compression                                       │  │
│  │  • Request Logging                                        │  │
│  │  • Exception Handlers                                     │  │
│  └──────────────────────────────────────────────────────────┘  │
│                            │                                     │
│  ┌──────────────────────────▼──────────────────────────────┐  │
│  │                    API ROUTERS                            │  │
│  │  ┌────────────────────────────────────────────────────┐  │  │
│  │  │  Router Factory (create_crud_router)               │  │  │
│  │  │  • Genera endpoints CRUD automáticamente           │  │  │
│  │  │  • GET /       → Lista paginada                    │  │  │
│  │  │  • GET /{id}   → Obtener por ID                    │  │  │
│  │  │  • POST /      → Crear                             │  │  │
│  │  │  • PUT /{id}   → Actualizar                        │  │  │
│  │  │  • DELETE /{id}→ Eliminar                          │  │  │
│  │  └────────────────────────────────────────────────────┘  │  │
│  └──────────────────────────┬──────────────────────────────┘  │
│                              │                                  │
│  ┌──────────────────────────▼──────────────────────────────┐  │
│  │                    CRUD LAYER                             │  │
│  │  ┌────────────────────────────────────────────────────┐  │  │
│  │  │  CRUDBase (Generic CRUD Operations)                │  │  │
│  │  │  • get(id) → Obtener un registro                   │  │  │
│  │  │  • get_multi(skip, limit) → Lista paginada         │  │  │
│  │  │  • count() → Total de registros                    │  │  │
│  │  │  • create(obj_in) → Crear registro                 │  │  │
│  │  │  • update(db_obj, obj_in) → Actualizar             │  │  │
│  │  │  • delete(id) → Eliminar registro                  │  │  │
│  │  └────────────────────────────────────────────────────┘  │  │
│  └──────────────────────────┬──────────────────────────────┘  │
│                              │                                  │
│  ┌──────────────────────────▼──────────────────────────────┐  │
│  │                 VALIDATION LAYER                          │  │
│  │  ┌────────────────────────────────────────────────────┐  │  │
│  │  │  Pydantic Schemas                                  │  │  │
│  │  │  • Base Schema                                     │  │  │
│  │  │  • Create Schema                                   │  │  │
│  │  │  • Update Schema                                   │  │  │
│  │  │  • Response Schema                                 │  │  │
│  │  │  → Validación automática de tipos y datos         │  │  │
│  │  └────────────────────────────────────────────────────┘  │  │
│  └──────────────────────────┬──────────────────────────────┘  │
│                              │                                  │
│  ┌──────────────────────────▼──────────────────────────────┐  │
│  │                    ORM LAYER                              │  │
│  │  ┌────────────────────────────────────────────────────┐  │  │
│  │  │  SQLAlchemy Models                                 │  │  │
│  │  │  • PA_DI_* (Documentos)                            │  │  │
│  │  │  • PA_EQ_* (Equipamiento)                          │  │  │
│  │  │  • PE_SE_* (Procesos Estratégicos)                 │  │  │
│  │  │  • SYS_* (Sistema)                                 │  │  │
│  │  │  → Mapeo objeto-relacional                        │  │  │
│  │  └────────────────────────────────────────────────────┘  │  │
│  └──────────────────────────┬──────────────────────────────┘  │
│                              │                                  │
│  ┌──────────────────────────▼──────────────────────────────┐  │
│  │              DATABASE CONNECTION POOL                     │  │
│  │  • Pool Size: 10                                          │  │
│  │  • Max Overflow: 20                                       │  │
│  │  • Pre-ping: Enabled                                      │  │
│  └──────────────────────────┬──────────────────────────────┘  │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            │ SQL Queries
                            │
┌───────────────────────────▼─────────────────────────────────────┐
│                     POSTGRESQL DATABASE                          │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                     Schema: SGApp                         │  │
│  │  ┌────────────────────────────────────────────────────┐  │  │
│  │  │  Tablas Principales:                               │  │  │
│  │  │  • pa_di_fa (Fallas/Eventos)                       │  │  │
│  │  │  • pa_di_pr (Procesos)                             │  │  │
│  │  │  • pa_di_ra (Registro Actualización)               │  │  │
│  │  │  • pa_eq_* (Equipamiento - 10+ tablas)             │  │  │
│  │  │  • pe_se_* (Procesos Estratégicos - 10+ tablas)    │  │  │
│  │  │  • sys_* (Sistema - 3 tablas)                      │  │  │
│  │  └────────────────────────────────────────────────────┘  │  │
│  └──────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────────┘
```

## 🔄 Flujo de una Petición

```
1. CLIENTE
   │
   │  GET /api/v1/pa-di-fa/?skip=0&limit=50
   │
   ▼
2. MIDDLEWARE
   │  • Validar CORS
   │  • Comprimir respuesta (GZIP)
   │  • Log request
   │
   ▼
3. ROUTER
   │  • Identificar endpoint
   │  • Parsear parámetros (skip, limit)
   │  • Validar con Pydantic
   │
   ▼
4. CRUD LAYER
   │  • crud.get_multi(db, skip=0, limit=50)
   │  • crud.count(db)
   │
   ▼
5. ORM (SQLAlchemy)
   │  • Construir query SQL
   │  • SELECT * FROM "SGApp".pa_di_fa 
   │    OFFSET 0 LIMIT 50
   │
   ▼
6. DATABASE
   │  • Ejecutar query
   │  • Retornar resultados
   │
   ▼
7. ORM
   │  • Mapear resultados a objetos Python
   │
   ▼
8. CRUD LAYER
   │  • Formatear respuesta paginada
   │
   ▼
9. ROUTER
   │  • Serializar con Pydantic
   │  • Validar respuesta
   │
   ▼
10. MIDDLEWARE
    │  • Comprimir
    │  • Log response
    │
    ▼
11. CLIENTE
    │  Recibe:
    │  {
    │    "items": [...],
    │    "total": 100,
    │    "skip": 0,
    │    "limit": 50,
    │    "has_next": true,
    │    "has_prev": false
    │  }
```

## 📁 Estructura de Archivos

```
backend_mejorado/
│
├── app/                                    # Aplicación principal
│   │
│   ├── api/                                # Capa de API
│   │   ├── __init__.py
│   │   ├── router_factory.py              # Factory para routers CRUD
│   │   └── endpoints/                     # Endpoints personalizados (futuro)
│   │       └── __init__.py
│   │
│   ├── core/                               # Configuración central
│   │   ├── __init__.py
│   │   ├── config.py                      # Settings (con Pydantic)
│   │   └── database.py                    # Configuración DB
│   │
│   ├── crud/                               # Operaciones de base de datos
│   │   ├── __init__.py
│   │   └── base.py                        # CRUD genérico reutilizable
│   │
│   ├── models/                             # Modelos SQLAlchemy
│   │   ├── __init__.py
│   │   ├── pa_di.py                       # Modelos de documentos
│   │   ├── pa_eq.py                       # Modelos de equipamiento
│   │   ├── pe.py                          # Modelos de procesos
│   │   └── sys.py                         # Modelos del sistema
│   │
│   ├── schemas/                            # Schemas Pydantic
│   │   ├── __init__.py
│   │   ├── base.py                        # Schemas base
│   │   ├── pa_di.py                       # Schemas de documentos
│   │   └── ...                            # Otros schemas
│   │
│   └── main.py                             # Punto de entrada de la app
│
├── tests/                                  # Tests (estructura preparada)
│   └── __init__.py
│
├── .env.example                            # Variables de entorno ejemplo
├── .gitignore                              # Archivos ignorados por Git
├── docker-compose.yml                      # Config Docker Compose
├── Dockerfile                              # Dockerfile de la app
├── requirements.txt                        # Dependencias Python
│
├── README.md                               # Documentación completa
├── API_EXAMPLES.md                         # Ejemplos de uso
├── MIGRATION_GUIDE.md                      # Guía de migración
├── SUMMARY.md                              # Resumen ejecutivo
├── LEEME_PRIMERO.md                        # Instrucciones rápidas
└── generate_routers.py                     # Script auxiliar
```

## 🎯 Componentes Clave

### 1. Router Factory
**Ubicación**: `app/api/router_factory.py`
**Propósito**: Genera automáticamente todos los endpoints CRUD
**Ventaja**: Elimina código duplicado (de 1,482 líneas a ~500)

### 2. CRUD Base
**Ubicación**: `app/crud/base.py`
**Propósito**: Implementa operaciones de base de datos genéricas
**Ventaja**: Reutilización de código, comportamiento consistente

### 3. Models (SQLAlchemy)
**Ubicación**: `app/models/*.py`
**Propósito**: Define estructura de tablas de base de datos
**Organización**: Por módulos (pa_di, pa_eq, pe, sys)

### 4. Schemas (Pydantic)
**Ubicación**: `app/schemas/*.py`
**Propósito**: Validación y serialización de datos
**Tipos**: Base, Create, Update, Response

### 5. Main Application
**Ubicación**: `app/main.py`
**Propósito**: Punto de entrada, configuración de app
**Incluye**: Middleware, exception handlers, router registration

## 🔌 Integración con Otros Sistemas

### Frontend (React/Angular/Vue)
```javascript
// Configuración base
const API_URL = 'http://localhost:8000/api/v1';

// Fetch con paginación
fetch(`${API_URL}/pa-di-fa/?skip=0&limit=50`)
  .then(res => res.json())
  .then(data => {
    console.log(data.items);      // Array de registros
    console.log(data.total);      // Total en BD
    console.log(data.has_next);   // ¿Hay más páginas?
  });
```

### Mobile App (React Native/Flutter)
```dart
// Dart/Flutter
final response = await http.get(
  Uri.parse('$apiUrl/pa-di-fa/?skip=0&limit=50'),
);
final data = jsonDecode(response.body);
List items = data['items'];
```

### Otros Backends (Microservicios)
```python
import requests

# Python a Python
response = requests.get(
    'http://sgapp-api:8000/api/v1/pa-di-fa/',
    params={'skip': 0, 'limit': 50}
)
data = response.json()
```

## 🔒 Seguridad

### Implementado
- ✅ CORS configurado
- ✅ Validación de datos (Pydantic)
- ✅ SQL Injection protection (ORM)
- ✅ Error handling robusto
- ✅ Environment variables para secrets

### Recomendado Agregar
- [ ] Autenticación (JWT/OAuth2)
- [ ] Autorización (RBAC)
- [ ] Rate limiting
- [ ] HTTPS/TLS
- [ ] API Keys

## 📊 Performance

### Optimizaciones Implementadas
- Connection pooling (10 conexiones base, 20 max)
- GZIP compression para respuestas
- Paginación para evitar queries grandes
- Índices en primary keys
- Pre-ping para validar conexiones

### Métricas Objetivo
- Response time: < 200ms (queries simples)
- Throughput: 1000+ req/s
- Database connections: Reutilizadas eficientemente

## 🚀 Escalabilidad

### Horizontal Scaling
```bash
# Docker Compose
docker-compose up -d --scale api=3

# Balanceo con nginx
upstream api_servers {
    server api:8000;
    server api:8001;
    server api:8002;
}
```

### Vertical Scaling
- Incrementar DB_POOL_SIZE
- Incrementar MAX_OVERFLOW
- Más RAM/CPU para contenedores

---

**Este diagrama representa la arquitectura completa del sistema. Cada componente está diseñado para ser modular, mantenible y escalable.**
