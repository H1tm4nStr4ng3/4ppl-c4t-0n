# 🚀 SGApp Backend - Sistema de Gestión de Calidad

API RESTful moderna y optimizada para Sistema de Gestión de Calidad, construida con FastAPI y PostgreSQL.

## ✨ Características Principales

- ✅ **Arquitectura Limpia**: Código DRY siguiendo las mejores prácticas
- ✅ **CRUD Completo**: Operaciones Create, Read, Update, Delete para todas las entidades
- ✅ **Paginación Automática**: Respuestas paginadas con metadatos
- ✅ **Validación Robusta**: Validación de datos con Pydantic
- ✅ **Manejo de Errores**: Sistema robusto de manejo de excepciones
- ✅ **CORS Configurado**: Listo para integración con frontend
- ✅ **Documentación Automática**: Swagger UI y ReDoc incluidos
- ✅ **Docker Ready**: Containerización completa con Docker Compose
- ✅ **Type Hints**: Código completamente tipado
- ✅ **Logging**: Sistema de logging estructurado

## 📋 Requisitos Previos

- Python 3.11 o superior
- PostgreSQL 14 o superior
- Docker y Docker Compose (opcional)

## 🛠️ Instalación

### Opción 1: Instalación Local

1. **Clonar el repositorio**
```bash
git clone <repository-url>
cd backend_mejorado
```

2. **Crear entorno virtual**
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Configurar variables de entorno**
```bash
cp .env.example .env
# Editar .env con tus credenciales de base de datos
```

5. **Ejecutar migraciones** (si es necesario)
```bash
# Tu base de datos ya debe existir con el schema SGApp
# Este backend se conecta a una base de datos existente
```

6. **Iniciar el servidor**
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Opción 2: Docker Compose (Recomendado)

1. **Iniciar todos los servicios**
```bash
docker-compose up -d
```

Esto iniciará:
- PostgreSQL en el puerto 5432
- API en el puerto 8000
- pgAdmin en el puerto 5050 (opcional)

2. **Ver logs**
```bash
docker-compose logs -f api
```

3. **Detener servicios**
```bash
docker-compose down
```

## 📚 Estructura del Proyecto

```
backend_mejorado/
│
├── app/
│   ├── api/
│   │   ├── endpoints/          # Endpoints personalizados (si se necesitan)
│   │   └── router_factory.py   # Factory para generar routers CRUD
│   │
│   ├── core/
│   │   ├── config.py           # Configuración de la aplicación
│   │   └── database.py         # Configuración de base de datos
│   │
│   ├── crud/
│   │   └── base.py             # Operaciones CRUD genéricas
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── pa_di.py            # Modelos de Documentos
│   │   ├── pa_eq.py            # Modelos de Equipamiento
│   │   ├── pe.py               # Modelos de Procesos Estratégicos
│   │   └── sys.py              # Modelos del Sistema
│   │
│   ├── schemas/
│   │   ├── base.py             # Schemas base y utilidades
│   │   ├── pa_di.py            # Schemas de Documentos
│   │   └── ...                 # Otros schemas
│   │
│   └── main.py                 # Aplicación principal
│
├── tests/                      # Tests unitarios y de integración
├── .env.example                # Ejemplo de variables de entorno
├── docker-compose.yml          # Configuración de Docker Compose
├── Dockerfile                  # Dockerfile para la API
├── requirements.txt            # Dependencias de Python
├── generate_routers.py         # Script para generar routers
└── README.md                   # Este archivo
```

## 🔧 Configuración

### Variables de Entorno

Crea un archivo `.env` basado en `.env.example`:

```env
# Base de Datos
DATABASE_URL=postgresql://user:password@localhost:5432/SGApp

# API
PROJECT_NAME=SGApp API
VERSION=2.0.0
API_V1_STR=/api/v1

# CORS
BACKEND_CORS_ORIGINS=["http://localhost:3000"]

# Paginación
DEFAULT_PAGE_SIZE=50
MAX_PAGE_SIZE=1000

# Logging
LOG_LEVEL=INFO
```

## 📖 Uso de la API

### Documentación Interactiva

Una vez que el servidor esté ejecutándose, accede a:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Endpoints Principales

#### Health Check
```bash
GET /health
```

#### Listar Registros (con paginación)
```bash
GET /api/v1/pa-di-fa/?skip=0&limit=50
```

#### Obtener un Registro
```bash
GET /api/v1/pa-di-fa/{id}
```

#### Crear Registro
```bash
POST /api/v1/pa-di-fa/
Content-Type: application/json

{
  "registrado_por": "usuario",
  "fecha": "2024-01-20T10:00:00",
  "evento": "Descripción del evento",
  "resuelto": false
}
```

#### Actualizar Registro
```bash
PUT /api/v1/pa-di-fa/{id}
Content-Type: application/json

{
  "resuelto": true
}
```

#### Eliminar Registro
```bash
DELETE /api/v1/pa-di-fa/{id}
```

### Ejemplo de Respuesta Paginada

```json
{
  "items": [
    {
      "id": 1,
      "registrado_por": "usuario",
      "fecha": "2024-01-20T10:00:00",
      "evento": "Descripción",
      "resuelto": false,
      "trial814": null
    }
  ],
  "total": 100,
  "skip": 0,
  "limit": 50,
  "has_next": true,
  "has_prev": false
}
```

## 🎯 Mejoras Implementadas

### vs. Versión Anterior

| Aspecto | Antes | Ahora |
|---------|-------|-------|
| Líneas de código | ~1,482 | ~500 (70% reducción) |
| Código repetitivo | Sí, altamente duplicado | No, totalmente DRY |
| Paginación | No | Sí, automática |
| Operación DELETE | No | Sí, implementada |
| Manejo de errores | Básico | Robusto y detallado |
| CORS | No configurado | Configurado |
| Validación | Limitada | Completa con Pydantic |
| Logging | No | Sí, estructurado |
| Docker | No | Sí, con Docker Compose |
| Documentación | Básica | Completa con ejemplos |

### Características Nuevas

1. **Router Factory**: Sistema genérico que genera automáticamente todos los endpoints CRUD
2. **CRUD Base**: Clase base reutilizable para operaciones de base de datos
3. **Paginación**: Respuestas paginadas con metadatos (total, has_next, has_prev)
4. **Middleware de Logging**: Registro automático de todas las requests
5. **Exception Handlers**: Manejo centralizado de errores
6. **Type Safety**: Código completamente tipado con hints
7. **Schemas Organizados**: Schemas separados por módulos
8. **Docker Ready**: Containerización completa con PostgreSQL y pgAdmin

## 🧪 Testing

```bash
# Ejecutar tests
pytest

# Con coverage
pytest --cov=app tests/

# Tests específicos
pytest tests/test_api.py -v
```

## 🚀 Despliegue en Producción

### Consideraciones

1. **Cambiar SECRET_KEY** en variables de entorno
2. **Configurar CORS** para dominios específicos
3. **Usar HTTPS** con certificados SSL
4. **Configurar LOG_LEVEL=WARNING** o ERROR
5. **Implementar rate limiting** si es necesario
6. **Usar un proxy reverse** (nginx, traefik)
7. **Configurar backups** automáticos de la base de datos

### Ejemplo con Docker

```bash
# Producción
docker-compose -f docker-compose.prod.yml up -d

# Escalar API
docker-compose up -d --scale api=3
```

## 📝 Agregar Nuevas Entidades

Para agregar una nueva entidad al sistema:

1. **Crear el modelo** en `app/models/`
2. **Crear los schemas** en `app/schemas/`
3. **Registrar el router** en `app/main.py`:

```python
from app.models.new_module import NewModel
from app.schemas.new_module import NewModelSchema, NewModelCreate, NewModelUpdate

app.include_router(
    create_crud_router(
        model=NewModel,
        schema=NewModelSchema,
        create_schema=NewModelCreate,
        update_schema=NewModelUpdate,
        prefix=f"{settings.API_V1_STR}/new-model",
        tags=["New Model"]
    )
)
```

## 🐛 Troubleshooting

### Error de conexión a la base de datos

```bash
# Verificar que PostgreSQL esté ejecutándose
docker-compose ps

# Ver logs de PostgreSQL
docker-compose logs postgres
```

### Error de permisos

```bash
# Asegurar que el schema SGApp exista
psql -U postgres -d SGApp -c "CREATE SCHEMA IF NOT EXISTS \"SGApp\";"
```

## 📄 Licencia

Este proyecto está bajo la licencia MIT.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📞 Soporte

Para soporte y preguntas, abre un issue en el repositorio.

---

**Desarrollado con ❤️ usando FastAPI**
