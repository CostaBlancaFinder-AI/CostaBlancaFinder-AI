# CostaBlancaFinder AI — Pipeline Documentation

## Estado actual

El pipeline automático V1 funciona correctamente.

## Flujo actual

1. Scraper placeholder
2. Opportunity Scoring Agent V2
3. Location Enrichment Engine
4. Recommendation Engine
5. Dashboard actualizado

## Archivos principales

- `02_DATA_IA/scrapers/idealista_scraper.py`
- `02_DATA_IA/scoring_engine/opportunity_score_v2.py`
- `02_DATA_IA/feature_engineering/location_enrichment.py`
- `02_DATA_IA/recommendation_system/recommendation_engine.py`
- `03_AUTOMATIZACIONES/update_pipeline.py`

## Salidas generadas

- `02_DATA_IA/processed_data/rentals_scored_v2.csv`
- `02_DATA_IA/processed_data/rentals_enriched.csv`
- `02_DATA_IA/recommendations/recommended_properties.csv`

## Estado del scraper

Actualmente el scraper es un placeholder y trabaja sobre dataset manual.

Más adelante se sustituirá por:

- APIs oficiales
- OpenStreetMap
- Google Places
- scraping controlado
- datasets reales

## Próximos pasos

- Mejorar dashboard con recomendaciones IA
- Añadir logs del pipeline
- Crear ejecución automática diaria
- Integrar fuentes reales