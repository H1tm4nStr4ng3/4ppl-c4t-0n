# 🚀 Inicio Rápido - SGApp Frontend

## Paso 1: Instalación

Abre una terminal en la carpeta del proyecto y ejecuta:

```bash
npm install
```

Este comando instalará todas las dependencias necesarias (React, React Router, Axios, Lucide React, Vite, etc.)

## Paso 2: Configurar el Backend

Asegúrate de que tu backend FastAPI esté ejecutándose en `http://localhost:8000`

Para iniciar el backend (en otra terminal):
```bash
cd /ruta/a/tu/backend
uvicorn main:app --reload
```

## Paso 3: Iniciar el Frontend

En la terminal del proyecto frontend, ejecuta:

```bash
npm run dev
```

## Paso 4: Acceder a la Aplicación

Abre tu navegador en:
```
http://localhost:3000
```

## 📱 Usar la Aplicación

### En Escritorio:
1. Verás el sidebar a la izquierda con todas las categorías
2. Haz clic en una categoría para expandir sus módulos
3. Selecciona un módulo para ver sus datos
4. Usa los botones "Nuevo", "Editar" y "Eliminar" para gestionar los datos

### En Móvil:
1. Haz clic en el icono de menú (☰) en la esquina superior izquierda
2. El sidebar se abrirá desde la izquierda
3. Selecciona el módulo que desees
4. El sidebar se cerrará automáticamente al seleccionar

## 🎨 Características Principales

### Dashboard
- Estadísticas generales del sistema
- Accesos rápidos a módulos frecuentes
- Información del sistema

### Módulos CRUD
- **Buscar**: Usa la barra de búsqueda para filtrar datos
- **Crear**: Haz clic en "Nuevo" para agregar un elemento
- **Editar**: Haz clic en el ícono de lápiz en cada fila
- **Eliminar**: Haz clic en el ícono de basura (confirmará antes de eliminar)

## 🔧 Problemas Comunes

### "Error al cargar los datos"
**Solución**: Verifica que el backend esté ejecutándose:
```bash
# En la terminal del backend debería aparecer:
# Uvicorn running on http://127.0.0.1:8000
```

### "No se conecta al backend"
**Solución**: Verifica la configuración de CORS en tu backend FastAPI.
Debe incluir:
```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### El sidebar no aparece en móvil
**Solución**: Haz clic en el botón de menú (tres líneas horizontales) en la parte superior izquierda.

## 📚 Recursos Adicionales

- **README.md**: Documentación completa del proyecto
- **src/services/api.js**: Todos los endpoints disponibles
- **src/App.css**: Personalización de estilos

## 💡 Consejos

1. **Búsqueda Rápida**: La búsqueda funciona en todos los campos de la tabla
2. **Formularios Dinámicos**: Los formularios se generan automáticamente según la estructura de datos
3. **Validación**: Los campos de fecha, número y texto se validan automáticamente
4. **Confirmación**: Las eliminaciones siempre pedirán confirmación

## 🎯 Próximos Pasos

Una vez familiarizado con la aplicación:
- Explora todos los módulos disponibles
- Personaliza los colores en `src/App.css`
- Agrega nuevos endpoints en `src/services/api.js`
- Modifica el Dashboard según tus necesidades

¡Disfruta usando SGApp! 🎉
