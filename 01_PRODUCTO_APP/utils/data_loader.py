"""
============================================================
CostaBlancaFinder AI
Data Loader Utility
============================================================

Objetivo:
Centralizar funciones reutilizables para cargar datos.

Este módulo evita repetir pd.read_csv(...) en diferentes partes
del proyecto y prepara la futura migración a base de datos.

Futuro:
- carga desde PostgreSQL
- carga desde Supabase
- validación de esquemas
- control de errores
- cacheo de datos
============================================================
"""

import pandas as pd
import streamlit as st


# ============================================================
# LOAD CSV DATA
# ============================================================

@st.cache_data
def load_csv(path) -> pd.DataFrame:
    return pd.read_csv(path)