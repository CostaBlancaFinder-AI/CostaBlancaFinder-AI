"""
========================================================
RECOMMENDATION REPOSITORY
========================================================

Objetivo:
Centralizar el acceso a recomendaciones IA.
========================================================
"""

from utils.data_loader import load_csv
from config.settings import RECOMMENDATIONS_DATASET


def load_recommendations_data():
    """
    Carga recomendaciones IA.
    """

    return load_csv(RECOMMENDATIONS_DATASET)