# CostaBlancaFinder AI — Ingestion Pipeline

## Objetivo

Este módulo gestiona el flujo principal de datos inmobiliarios:

```text
Fuentes reales / Mock
→ JSON bruto
→ Normalización universal
→ Deduplicación
→ Filtros
→ Scoring
→ CSV limpio
→ Top oportunidades
→ Resumen ejecutivo