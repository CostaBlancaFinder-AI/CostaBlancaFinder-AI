"""
========================================================
PROPERTY REPOSITORY
========================================================

Objetivo:
Centralizar el acceso a propiedades inmobiliarias.

Ventajas:
- evita leer CSV directamente
- facilita migración futura a PostgreSQL
- desacopla frontend y datos
========================================================
"""

from utils.data_loader import load_csv
from config.settings import ENRICHED_DATASET


def load_properties():
    """
    Carga el dataset enriquecido de propiedades.
    """

    return load_csv(ENRICHED_DATASET)
