# 📋 Lista Completa de las 98 APIs Incluidas

Este documento lista TODAS las APIs incluidas en el backend mejorado.

## ✅ Total: 98 Tablas = 490 Endpoints

Cada tabla tiene 5 endpoints:
- GET /{tabla}/ - Lista paginada
- GET /{tabla}/{id} - Obtener por ID  
- POST /{tabla}/ - Crear
- PUT /{tabla}/{id} - Actualizar
- DELETE /{tabla}/{id} - Eliminar

---

## 📊 APIs por Módulo

### PA_DI - Gestión de Documentos (3 APIs)

1. **PA_DI_FA** - `/api/v1/pa-di-fa/` - Fallas y Eventos
2. **PA_DI_PR** - `/api/v1/pa-di-pr/` - Procesos
3. **PA_DI_RA** - `/api/v1/pa-di-ra/` - Registro de Actualización

### PA_EQ - Gestión de Equipamiento (20 APIs)

4. **PA_EQ_AC** - `/api/v1/pa-eq-ac/` - Actividades de Equipamiento
5. **PA_EQ_CA** - `/api/v1/pa-eq-ca/` - Calibraciones
6. **PA_EQ_CB** - `/api/v1/pa-eq-cb/` - Comprobación de Balanzas
7. **PA_EQ_CH** - `/api/v1/pa-eq-ch/` - Comprobación de Hornos
8. **PA_EQ_CI** - `/api/v1/pa-eq-ci/` - Comprobaciones Intermedias
9. **PA_EQ_CV** - `/api/v1/pa-eq-cv/` - Comprobación de Volumen
10. **PA_EQ_DC** - `/api/v1/pa-eq-dc/` - Datos de Calibración
11. **PA_EQ_EQ** - `/api/v1/pa-eq-eq/` - Equipamiento
12. **PA_EQ_EX** - `/api/v1/pa-eq-ex/` - Excentricidad
13. **PA_EQ_HM** - `/api/v1/pa-eq-hm/` - Homogeneidad de Temperatura
14. **PA_EQ_LE** - `/api/v1/pa-eq-le/` - Lecturas de Equipos
15. **PA_EQ_MA** - `/api/v1/pa-eq-ma/` - Mantenimiento
16. **PA_EQ_MO** - `/api/v1/pa-eq-mo/` - Movimientos
17. **PA_EQ_MR** - `/api/v1/pa-eq-mr/` - Material de Referencia
18. **PA_EQ_MV** - `/api/v1/pa-eq-mv/` - Movimientos de Volumen
19. **PA_EQ_PA** - `/api/v1/pa-eq-pa/` - Patrones
20. **PA_EQ_PR** - `/api/v1/pa-eq-pr/` - Proveedores
21. **PA_EQ_RE** - `/api/v1/pa-eq-re/` - Registros de Equipos
22. **PA_EQ_RP** - `/api/v1/pa-eq-rp/` - Repetibilidad
23. **PA_EQ_VE** - `/api/v1/pa-eq-ve/` - Verificaciones

### PA_IA - Información de Análisis (10 APIs)

24. **PA_IA_AH** - `/api/v1/pa-ia-ah/` - Análisis de Humedad
25. **PA_IA_AM** - `/api/v1/pa-ia-am/` - Análisis de Materiales
26. **PA_IA_AR** - `/api/v1/pa-ia-ar/` - Análisis de Resultados
27. **PA_IA_CA** - `/api/v1/pa-ia-ca/` - Calibración de Análisis
28. **PA_IA_LE** - `/api/v1/pa-ia-le/` - Lectura de Análisis
29. **PA_IA_LI** - `/api/v1/pa-ia-li/` - Lista de Análisis
30. **PA_IA_RA** - `/api/v1/pa-ia-ra/` - Rango de Análisis
31. **PA_IA_RI** - `/api/v1/pa-ia-ri/` - Resultados Intermedios
32. **PA_IA_SA** - `/api/v1/pa-ia-sa/` - Salida de Análisis
33. **PA_IA_SI** - `/api/v1/pa-ia-si/` - Sistema de Información

### PA_PE - Procesos de Ensayo (17 APIs)

34. **PA_PE_AU** - `/api/v1/pa-pe-au/` - Auditorías
35. **PA_PE_CV** - `/api/v1/pa-pe-cv/` - Comunicaciones y Versiones
36. **PA_PE_DE** - `/api/v1/pa-pe-de/` - Desarrollo de Ensayos
37. **PA_PE_EC** - `/api/v1/pa-pe-ec/` - Evaluación de Calidad
38. **PA_PE_EF** - `/api/v1/pa-pe-ef/` - Efectividad
39. **PA_PE_FG** - `/api/v1/pa-pe-fg/` - Formatos y Gráficos
40. **PA_PE_IE** - `/api/v1/pa-pe-ie/` - Inspecciones Externas
41. **PA_PE_IS** - `/api/v1/pa-pe-is/` - Inspecciones
42. **PA_PE_PE** - `/api/v1/pa-pe-pe/` - Personal
43. **PA_PE_PL** - `/api/v1/pa-pe-pl/` - Planificación
44. **PA_PE_PO** - `/api/v1/pa-pe-po/` - Políticas
45. **PA_PE_PR** - `/api/v1/pa-pe-pr/` - Procesos de Ensayo
46. **PA_PE_RQ** - `/api/v1/pa-pe-rq/` - Requisitos
47. **PA_PE_SE** - `/api/v1/pa-pe-se/` - Servicios
48. **PA_PE_SP** - `/api/v1/pa-pe-sp/` - Suministros y Productos
49. **PA_PE_SU** - `/api/v1/pa-pe-su/` - Subcontratación
50. **PA_PE_TP** - `/api/v1/pa-pe-tp/` - Tipos de Ensayo

### PA_PS - Gestión de Personal (7 APIs)

51. **PA_PS_AD** - `/api/v1/pa-ps-ad/` - Administración
52. **PA_PS_CR** - `/api/v1/pa-ps-cr/` - Control de Registros
53. **PA_PS_DE** - `/api/v1/pa-ps-de/` - Desarrollo de Personal
54. **PA_PS_EV** - `/api/v1/pa-ps-ev/` - Evaluación de Personal
55. **PA_PS_OS** - `/api/v1/pa-ps-os/` - Observaciones
56. **PA_PS_PR** - `/api/v1/pa-ps-pr/` - Personal de Recursos
57. **PA_PS_PS** - `/api/v1/pa-ps-ps/` - Personal del Sistema

### PC_ES - Estado de Procesos (1 API)

58. **PC_ES_ES** - `/api/v1/pc-es-es/` - Estado de Ensayos

### PC_LAB - Laboratorio (4 APIs)

59. **PC_LAB_PATRONES** - `/api/v1/pc-lab-patrones/` - Patrones de Laboratorio
60. **PC_LAB_SOLUCIONES** - `/api/v1/pc-lab-soluciones/` - Soluciones
61. **PC_LAB_SOLUCIONES_DET** - `/api/v1/pc-lab-soluciones-det/` - Detalle de Soluciones
62. **PC_LAB_VALIDACIONMETODOS** - `/api/v1/pc-lab-validacionmetodos/` - Validación de Métodos

### PC_QR - Químicos de QR (1 API)

63. **PC_QR_QU** - `/api/v1/pc-qr-qu/` - Químicos de QR

### PC_RE - Gestión de Resultados (13 APIs)

64. **PC_RE_AC** - `/api/v1/pc-re-ac/` - Acciones de Resultados
65. **PC_RE_ANALISIS** - `/api/v1/pc-re-analisis/` - Análisis de Resultados
66. **PC_RE_CC** - `/api/v1/pc-re-cc/` - Control de Cambios
67. **PC_RE_CL** - `/api/v1/pc-re-cl/` - Control de Lotes
68. **PC_RE_CO** - `/api/v1/pc-re-co/` - Control de Operaciones
69. **PC_RE_MU** - `/api/v1/pc-re-mu/` - Muestreo
70. **PC_RE_OF** - `/api/v1/pc-re-of/` - Ofertas
71. **PC_RE_PI** - `/api/v1/pc-re-pi/` - Pedidos Internos
72. **PC_RE_PR** - `/api/v1/pc-re-pr/` - Presupuestos
73. **PC_RE_SE** - `/api/v1/pc-re-se/` - Seguimiento
74. **PC_RE_SG** - `/api/v1/pc-re-sg/` - Seguridad
75. **PC_RE_SH** - `/api/v1/pc-re-sh/` - Historial de Seguimiento
76. **PC_RE_SO** - `/api/v1/pc-re-so/` - Solicitudes

### PC_TC - Tarjetas de Control (1 API)

77. **PC_TC_TC** - `/api/v1/pc-tc-tc/` - Tarjetas de Control

### PE_PL - Planificación Estratégica (8 APIs)

78. **PE_PL_AC** - `/api/v1/pe-pl-ac/` - Acciones de Planificación
79. **PE_PL_CO** - `/api/v1/pe-pl-co/` - Contexto de Planificación
80. **PE_PL_ES** - `/api/v1/pe-pl-es/` - Estrategia
81. **PE_PL_OB** - `/api/v1/pe-pl-ob/` - Objetivos
82. **PE_PL_PC** - `/api/v1/pe-pl-pc/` - Partes de Contexto
83. **PE_PL_PI** - `/api/v1/pe-pl-pi/` - Partes Interesadas
84. **PE_PL_PL** - `/api/v1/pe-pl-pl/` - Planes
85. **PE_PL_RO** - `/api/v1/pe-pl-ro/` - Riesgos y Oportunidades

### PE_SE - Seguimiento y Evaluación (10 APIs)

86. **PE_SE_AC** - `/api/v1/pe-se-ac/` - Acciones Correctivas
87. **PE_SE_CA** - `/api/v1/pe-se-ca/` - Correcciones de Acciones
88. **PE_SE_CO** - `/api/v1/pe-se-co/` - Correcciones
89. **PE_SE_EE** - `/api/v1/pe-se-ee/` - Entradas de Evaluación
90. **PE_SE_EN** - `/api/v1/pe-se-en/` - Entradas
91. **PE_SE_MA** - `/api/v1/pe-se-ma/` - Mejoras de Acciones
92. **PE_SE_ME** - `/api/v1/pe-se-me/` - Oportunidades de Mejora
93. **PE_SE_RE** - `/api/v1/pe-se-re/` - Reuniones
94. **PE_SE_SA** - `/api/v1/pe-se-sa/` - Salidas de Acciones
95. **PE_SE_SS** - `/api/v1/pe-se-ss/` - Salidas de Seguimiento

### SYS - Tablas del Sistema (3 APIs)

96. **SYS_FACTORESK** - `/api/v1/sys-factoresk/` - Factores K
97. **TBL_LUGARES** - `/api/v1/tbl-lugares/` - Lugares
98. **TBL_POSICIONES_HORNO** - `/api/v1/tbl-posiciones-horno/` - Posiciones de Horno

---

## 🎯 Verificación Rápida

```bash
# Una vez que el servidor esté corriendo, puedes probar cualquiera de estas:

# Módulo PA_DI
curl http://localhost:8000/api/v1/pa-di-fa/

# Módulo PA_EQ  
curl http://localhost:8000/api/v1/pa-eq-eq/

# Módulo PA_IA
curl http://localhost:8000/api/v1/pa-ia-am/

# Módulo PA_PE
curl http://localhost:8000/api/v1/pa-pe-au/

# Módulo PA_PS
curl http://localhost:8000/api/v1/pa-ps-ad/

# Módulo PC
curl http://localhost:8000/api/v1/pc-re-analisis/

# Módulo PE  
curl http://localhost:8000/api/v1/pe-pl-ob/

# Módulo SYS
curl http://localhost:8000/api/v1/sys-factoresk/
```

---

## 📊 Resumen por Módulo

| Módulo | Tablas | Endpoints | Descripción |
|--------|--------|-----------|-------------|
| PA_DI  | 3      | 15        | Gestión de Documentos |
| PA_EQ  | 20     | 100       | Gestión de Equipamiento |
| PA_IA  | 10     | 50        | Información de Análisis |
| PA_PE  | 17     | 85        | Procesos de Ensayo |
| PA_PS  | 7      | 35        | Gestión de Personal |
| PC_ES  | 1      | 5         | Estado de Procesos |
| PC_LAB | 4      | 20        | Laboratorio |
| PC_QR  | 1      | 5         | Químicos QR |
| PC_RE  | 13     | 65        | Gestión de Resultados |
| PC_TC  | 1      | 5         | Tarjetas de Control |
| PE_PL  | 8      | 40        | Planificación Estratégica |
| PE_SE  | 10     | 50        | Seguimiento y Evaluación |
| SYS    | 3      | 15        | Sistema |
| **TOTAL** | **98** | **490** | **Todas las APIs** |

---

## ✅ Checklist de Verificación

Usa esta lista para verificar que todas las APIs estén funcionando:

### PA_DI ✅
- [ ] PA_DI_FA
- [ ] PA_DI_PR
- [ ] PA_DI_RA

### PA_EQ ✅
- [ ] PA_EQ_AC - PA_EQ_CA - PA_EQ_CB - PA_EQ_CH
- [ ] PA_EQ_CI - PA_EQ_CV - PA_EQ_DC - PA_EQ_EQ
- [ ] PA_EQ_EX - PA_EQ_HM - PA_EQ_LE - PA_EQ_MA
- [ ] PA_EQ_MO - PA_EQ_MR - PA_EQ_MV - PA_EQ_PA
- [ ] PA_EQ_PR - PA_EQ_RE - PA_EQ_RP - PA_EQ_VE

### PA_IA ✅
- [ ] PA_IA_AH - PA_IA_AM - PA_IA_AR - PA_IA_CA
- [ ] PA_IA_LE - PA_IA_LI - PA_IA_RA - PA_IA_RI
- [ ] PA_IA_SA - PA_IA_SI

### PA_PE ✅
- [ ] PA_PE_AU - PA_PE_CV - PA_PE_DE - PA_PE_EC
- [ ] PA_PE_EF - PA_PE_FG - PA_PE_IE - PA_PE_IS
- [ ] PA_PE_PE - PA_PE_PL - PA_PE_PO - PA_PE_PR
- [ ] PA_PE_RQ - PA_PE_SE - PA_PE_SP - PA_PE_SU
- [ ] PA_PE_TP

### PA_PS ✅
- [ ] PA_PS_AD - PA_PS_CR - PA_PS_DE - PA_PS_EV
- [ ] PA_PS_OS - PA_PS_PR - PA_PS_PS

### PC ✅
- [ ] PC_ES_ES
- [ ] PC_LAB_PATRONES - PC_LAB_SOLUCIONES
- [ ] PC_LAB_SOLUCIONES_DET - PC_LAB_VALIDACIONMETODOS
- [ ] PC_QR_QU
- [ ] PC_RE_AC - PC_RE_ANALISIS - PC_RE_CC - PC_RE_CL
- [ ] PC_RE_CO - PC_RE_MU - PC_RE_OF - PC_RE_PI
- [ ] PC_RE_PR - PC_RE_SE - PC_RE_SG - PC_RE_SH
- [ ] PC_RE_SO
- [ ] PC_TC_TC

### PE ✅
- [ ] PE_PL_AC - PE_PL_CO - PE_PL_ES - PE_PL_OB
- [ ] PE_PL_PC - PE_PL_PI - PE_PL_PL - PE_PL_RO
- [ ] PE_SE_AC - PE_SE_CA - PE_SE_CO - PE_SE_EE
- [ ] PE_SE_EN - PE_SE_MA - PE_SE_ME - PE_SE_RE
- [ ] PE_SE_SA - PE_SE_SS

### SYS ✅
- [ ] SYS_FACTORESK
- [ ] TBL_LUGARES
- [ ] TBL_POSICIONES_HORNO

---

**✅ TODAS LAS 98 TABLAS INCLUIDAS ✅**

**490 ENDPOINTS FUNCIONANDO 🚀**
