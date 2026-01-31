"""
Modelos SQLAlchemy - Versión Mejorada
Este archivo importa todos los modelos para facilitar su uso.
"""
from app.models.all_models import *

# Exportar todos los modelos
__all__ = [
    # PA_DI
    "PA_DI_FA", "PA_DI_PR", "PA_DI_RA",
    # PA_EQ
    "PA_EQ_AC", "PA_EQ_CA", "PA_EQ_CB", "PA_EQ_CH", "PA_EQ_CI", "PA_EQ_CV",
    "PA_EQ_DC", "PA_EQ_EQ", "PA_EQ_EX", "PA_EQ_HM", "PA_EQ_LE", "PA_EQ_MA",
    "PA_EQ_MO", "PA_EQ_MR", "PA_EQ_MV", "PA_EQ_PA", "PA_EQ_PR", "PA_EQ_RE",
    "PA_EQ_RP", "PA_EQ_VE",
    # PA_IA
    "PA_IA_AH", "PA_IA_AM", "PA_IA_AR", "PA_IA_CA", "PA_IA_LE", "PA_IA_LI",
    "PA_IA_RA", "PA_IA_RI", "PA_IA_SA", "PA_IA_SI",
    # PA_PE
    "PA_PE_AU", "PA_PE_CV", "PA_PE_DE", "PA_PE_EC", "PA_PE_EF", "PA_PE_FG",
    "PA_PE_IE", "PA_PE_IS", "PA_PE_PE", "PA_PE_PL", "PA_PE_PO", "PA_PE_PR",
    "PA_PE_RQ", "PA_PE_SE", "PA_PE_SP", "PA_PE_SU", "PA_PE_TP",
    # PA_PS
    "PA_PS_AD", "PA_PS_CR", "PA_PS_DE", "PA_PS_EV", "PA_PS_OS", "PA_PS_PR",
    "PA_PS_PS",
    # PC_ES
    "PC_ES_ES",
    # PC_LAB
    "PC_LAB_PATRONES", "PC_LAB_SOLUCIONES", "PC_LAB_SOLUCIONES_DET",
    "PC_LAB_VALIDACIONMETODOS",
    # PC_QR
    "PC_QR_QU",
    # PC_RE
    "PC_RE_AC", "PC_RE_ANALISIS", "PC_RE_CC", "PC_RE_CL", "PC_RE_CO",
    "PC_RE_MU", "PC_RE_OF", "PC_RE_PI", "PC_RE_PR", "PC_RE_SE", "PC_RE_SG",
    "PC_RE_SH", "PC_RE_SO",
    # PC_TC
    "PC_TC_TC",
    # PE_PL
    "PE_PL_AC", "PE_PL_CO", "PE_PL_ES", "PE_PL_OB", "PE_PL_PC", "PE_PL_PI",
    "PE_PL_PL", "PE_PL_RO",
    # PE_SE
    "PE_SE_AC", "PE_SE_CA", "PE_SE_CO", "PE_SE_EE", "PE_SE_EN",
    "PE_SE_MA", "PE_SE_ME", "PE_SE_RE", "PE_SE_SA", "PE_SE_SS",
    # SYS
    "SYS_FACTORESK", "TBL_LUGARES", "TBL_POSICIONES_HORNO"
]
