# app/schemas/all_schemas.py
# ORQUESTADOR HÍBRIDO: Manual para Personal y Equipamiento, Automático para el resto.
from __future__ import annotations
from typing import Any, List, Type
import inspect

# 1. IMPORTAR LOS ESQUEMAS MANUALES (VIPs)
# Al importar * aquí, hacemos que estén disponibles para main.py
from app.schemas.personal_schemas import *
from app.schemas.equipamiento_schemas import * # <--- NUEVO: Importamos Equipamiento

# Importamos los modelos SQL
from app import models
from sqlalchemy.sql.type_api import TypeEngine

# Herramientas de generación automática (Solo para lo que NO sea Manual)
from pydantic import BaseModel, create_model, ConfigDict, Field
from typing import Optional, Dict, Tuple
from sqlalchemy import Integer, String, Float, Boolean, DateTime, Text, BigInteger, SmallInteger
import unicodedata
from datetime import datetime

# ---------------------------
# UTILS (Para el generador automático)
# ---------------------------
def _to_ascii_name(name: str) -> str:
    nfkd = unicodedata.normalize("NFKD", name)
    ascii_name = "".join(c for c in nfkd if not unicodedata.combining(c))
    ascii_name = ascii_name.replace("-", "_").replace(" ", "_")
    if ascii_name and ascii_name[0].isdigit():
        ascii_name = f"f_{ascii_name}"
    return ascii_name

def _py_type(col_type: TypeEngine) -> type:
    if isinstance(col_type, (Integer, BigInteger, SmallInteger)): return int
    if isinstance(col_type, Float): return float
    if isinstance(col_type, Boolean): return bool
    if isinstance(col_type, DateTime): return datetime
    if isinstance(col_type, (String, Text)): return str
    return Any

class _SchemaBase(BaseModel):
    model_config = ConfigDict(from_attributes=True, populate_by_name=True, arbitrary_types_allowed=True)

class _ReadBase(BaseModel):
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

# ---------------------------
# GENERADOR AUTOMÁTICO (SOLO FALLBACK)
# ---------------------------
ALL_EXPORTS = []

def _iter_sqla_models(module) -> List[Type[Any]]:
    result = []
    for _, obj in inspect.getmembers(module):
        if inspect.isclass(obj) and hasattr(obj, "__table__"):
            try: getattr(obj, "__tablename__")
            except: continue
            result.append(obj)
    return result

def _collect_columns(model_cls):
    cols = list(model_cls.__table__.columns)
    return [c for c in cols if c.primary_key], [c for c in cols if not c.primary_key]

def _field_name_and_aliases(col):
    py_name = _to_ascii_name(col.key) or _to_ascii_name(col.name)
    return py_name, {"alias": col.name}

def _define_pyd_models_for(sa_cls: Type[Any]) -> None:
    sa_name = sa_cls.__name__
    
    # --- FILTRO CRÍTICO (LA SOLUCIÓN) ---
    # Si la clase empieza con PA_PE o PA_EQ, LA IGNORAMOS porque ya está en los schemas manuales.
    # Esto evita que el generador sobrescriba nuestro trabajo manual.
    if sa_name.startswith("PA_PE") or sa_name.startswith("PA_EQ"):
        # Aseguramos que se exporten los manuales con el nombre de tabla UPPERCASE
        if hasattr(sa_cls, "__tablename__"):
            table_upper = sa_cls.__tablename__.upper()
            # Buscamos la clase Read manual (ej: PA_PE_DERead o PA_EQ_MRRead)
            read_cls_name = f"{sa_name}Read"
            
            # Si existe la clase manual Read, la asignamos como el export principal
            if read_cls_name in globals():
                globals()[table_upper] = globals()[read_cls_name]
                if table_upper not in ALL_EXPORTS:
                    ALL_EXPORTS.append(table_upper)
            # Si no existe Read pero existe la Base (ej: PA_EQ_LEBase), intentamos usar esa o la clase base
            elif sa_name in globals():
                 globals()[table_upper] = globals()[sa_name] # Usamos la clase base manual
                 if table_upper not in ALL_EXPORTS:
                    ALL_EXPORTS.append(table_upper)
        return 
    # ----------------------

    # ... (Lógica de generación para el resto de tablas - Módulos PC, IA, SYS, etc.) ...
    pk_cols, non_pk_cols = _collect_columns(sa_cls)
    
    # 1. CREATE
    create_fields = {}
    for col in pk_cols + non_pk_cols:
        py_t = _py_type(col.type)
        fname, fkw = _field_name_and_aliases(col)
        if col.primary_key and py_t is int: continue
        is_optional = col.nullable or (col.default is not None) or (col.server_default is not None)
        if is_optional: create_fields[fname] = (Optional[py_t], Field(default=None, **fkw))
        else: create_fields[fname] = (py_t, Field(..., **fkw))

    # 2. UPDATE
    update_fields = {}
    for col in non_pk_cols:
        py_t = _py_type(col.type)
        fname, fkw = _field_name_and_aliases(col)
        update_fields[fname] = (Optional[py_t], Field(default=None, **fkw))

    # 3. READ
    read_fields = {}
    for col in pk_cols + non_pk_cols:
        if col.name.lower() in ['doc1', 'doc2', 'fotografia', 'respaldo']: continue
        py_t = _py_type(col.type)
        fname, fkw = _field_name_and_aliases(col)
        read_fields[fname] = (Optional[py_t], Field(default=None, **fkw))

    BaseName, CreateName, UpdateName = f"{sa_name}Base", f"{sa_name}Create", f"{sa_name}Update"
    ReadName = f"{sa_name}Read"

    CreateCls = create_model(CreateName, __base__=_SchemaBase, **create_fields) # type: ignore
    UpdateCls = create_model(UpdateName, __base__=_SchemaBase, **update_fields) # type: ignore
    ReadCls = create_model(ReadName, __base__=_ReadBase, **read_fields) # type: ignore
    BaseCls = create_model(BaseName, __base__=_SchemaBase)

    globals()[BaseCls.__name__] = BaseCls
    globals()[CreateCls.__name__] = CreateCls
    globals()[UpdateCls.__name__] = UpdateCls
    globals()[ReadCls.__name__] = ReadCls
    
    ALL_EXPORTS.extend([BaseName, CreateName, UpdateName, ReadName])
    
    if hasattr(sa_cls, "__tablename__"):
        table_upper = sa_cls.__tablename__.upper()
        globals()[table_upper] = ReadCls
        ALL_EXPORTS.append(table_upper)

# Ejecutar generador
for _cls in _iter_sqla_models(models):
    _define_pyd_models_for(_cls)

# Agregar manualmente los exports de schemas manuales a __all__
# Esto recoge todas las clases que importamos al principio
for name, obj in list(globals().items()):
    # Incluimos PA_PE y ahora PA_EQ en la exportación global
    if (name.startswith("PA_PE") or name.startswith("PA_EQ")) and "BaseModel" in str(obj.__mro__):
        if name not in ALL_EXPORTS:
            ALL_EXPORTS.append(name)

__all__ = ALL_EXPORTS