"""
========================================================
LOCATION REPOSITORY
========================================================

Objetivo:
Centralizar acceso a localizaciones geográficas.

========================================================
"""

from utils.data_loader import load_csv
from config.settings import OSM_LOCATIONS_DATASET


def load_locations():
    """
    Carga localizaciones geográficas.
    """

    return load_csv(OSM_LOCATIONS_DATASET)