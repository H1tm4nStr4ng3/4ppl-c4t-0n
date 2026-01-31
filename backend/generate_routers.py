"""
Script para generar automáticamente todos los schemas y routers faltantes
Este script crea los archivos necesarios para todas las tablas del sistema
"""
import os
from pathlib import Path

# Definición de todas las tablas y sus configuraciones
TABLES_CONFIG = {
    "PA_EQ": [
        ("PA_EQ_AC", "actividad", "str", "Actividades de Equipamiento"),
        ("PA_EQ_CA", "certificado", "str", "Calibraciones"),
        ("PA_EQ_CB", "id", "int", "Comprobación de Balanzas"),
        ("PA_EQ_CH", "id", "int", "Comprobación de Hornos"),
        ("PA_EQ_CI", "id_equi", "int", "Comprobaciones Intermedias"),
        ("PA_EQ_CV", "id", "int", "Comprobación de Volumen"),
        ("PA_EQ_DC", "id", "int", "Datos de Calibración"),
        ("PA_EQ_EQ", "id", "int", "Equipamiento"),
        ("PA_EQ_EX", "id", "int", "Excentricidad"),
        ("PA_EQ_HM", "id", "int", "Homogeneidad de Temperatura"),
    ],
    "PE_SE": [
        ("PE_SE_AC", "id", "int", "Acciones Correctivas"),
        ("PE_SE_CA", "id", "int", "Correcciones de Acciones"),
        ("PE_SE_CO", "id", "int", "Correcciones"),
        ("PE_SE_EE", "entradas", "str", "Entradas de Evaluación"),
        ("PE_SE_EN", "id", "int", "Entradas"),
        ("PE_SE_MA", "id", "int", "Mejoras de Acciones"),
        ("PE_SE_ME", "id", "int", "Oportunidades de Mejora"),
        ("PE_SE_RE", "id", "int", "Reuniones"),
        ("PE_SE_SA", "id", "int", "Salidas de Acciones"),
        ("PE_SE_SS", "salidas", "str", "Salidas de Seguimiento"),
    ],
    "SYS": [
        ("SYS_FACTORESK", "id", "int", "Factores K"),
        ("TBL_LUGARES", "lugarid", "int", "Lugares"),
        ("TBL_POSICIONES_HORNO", "posicionid", "int", "Posiciones de Horno"),
    ]
}


def generate_router_registration(table_name, description, pk_field, pk_type):
    """Genera el código para registrar un router"""
    prefix = table_name.lower().replace("_", "-")
    
    return f'''
# {description}
app.include_router(
    create_crud_router(
        model={table_name},
        schema={table_name}Schema,
        create_schema={table_name}Create,
        update_schema={table_name}Update,
        prefix=f"{{settings.API_V1_STR}}/{prefix}",
        tags=["{table_name}: {description}"]
    )
)
'''


def generate_all_routers():
    """Genera código para registrar todos los routers"""
    print("=" * 80)
    print("CÓDIGO PARA AGREGAR AL ARCHIVO main.py")
    print("=" * 80)
    print()
    print("# Agregar después de los imports existentes:")
    print()
    
    # Generar imports
    imports_by_module = {}
    for module, tables in TABLES_CONFIG.items():
        model_imports = []
        schema_imports = []
        for table_name, pk, pk_type, desc in tables:
            model_imports.append(table_name)
            schema_imports.extend([
                f"{table_name} as {table_name}Schema",
                f"{table_name}Create",
                f"{table_name}Update"
            ])
        
        module_lower = module.lower().replace("_", ".")
        if module == "SYS":
            module_lower = "sys"
        elif module == "PE_SE":
            module_lower = "pe"
        elif module == "PA_EQ":
            module_lower = "pa_eq"
            
        imports_by_module[module] = {
            "model": f"from app.models.{module_lower} import {', '.join(model_imports)}",
            "schema": f"from app.schemas.{module_lower} import ({', '.join(schema_imports)})"
        }
    
    # Imprimir imports
    print("# IMPORTS DE MODELOS:")
    for module in ["PA_EQ", "PE_SE", "SYS"]:
        if module in imports_by_module:
            print(imports_by_module[module]["model"])
    
    print()
    print("# IMPORTS DE SCHEMAS:")
    for module in ["PA_EQ", "PE_SE", "SYS"]:
        if module in imports_by_module:
            print(imports_by_module[module]["schema"])
    
    print()
    print("=" * 80)
    print("REGISTRO DE ROUTERS - Agregar después de los routers existentes:")
    print("=" * 80)
    print()
    
    # Generar registros de routers
    for module, tables in TABLES_CONFIG.items():
        print(f"\n# ============== {module} ==============")
        for table_name, pk, pk_type, desc in tables:
            print(generate_router_registration(table_name, desc, pk, pk_type))
    
    print()
    print("=" * 80)
    print("SCRIPT COMPLETADO")
    print("=" * 80)
    print()
    print("INSTRUCCIONES:")
    print("1. Copia los IMPORTS al inicio del archivo main.py")
    print("2. Copia el REGISTRO DE ROUTERS al final de main.py (antes del logger.info)")
    print("3. Asegúrate de que todos los schemas estén creados")
    print("4. Reinicia el servidor")
    print()


if __name__ == "__main__":
    generate_all_routers()
