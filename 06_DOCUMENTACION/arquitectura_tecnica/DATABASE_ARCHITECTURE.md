# CostaBlancaFinder AI — Database Architecture

# Objetivo

Diseñar una arquitectura de datos escalable preparada para inteligencia artificial, automatización y crecimiento futuro.

---

# Filosofía

Los datos son el núcleo de CostaBlancaFinder AI.

Toda la plataforma girará alrededor de:

- recopilación
- enriquecimiento
- análisis
- scoring
- personalización
- inteligencia predictiva

---

# Arquitectura inicial

CSV
↓
Processed Data
↓
Scoring Engine
↓
Dashboard

---

# Arquitectura futura

APIs
Scrapers
Usuarios
Eventos
Sensores externos
↓
Data Lake
↓
PostgreSQL
↓
AI Engine
↓
Frontend / Mobile

---

# Entidades principales

## 1. Properties

Información de propiedades.

### Campos

- property_id
- title
- city
- zone
- address
- latitude
- longitude
- price
- area_m2
- rooms
- bathrooms
- description
- source
- url
- images
- created_at

---

## 2. Opportunity Scores

Sistema IA de puntuación.

### Campos

- score_id
- property_id
- opportunity_score
- price_score
- location_score
- tourism_score
- investment_score
- ai_confidence

---

## 3. Users

Usuarios de la plataforma.

### Campos

- user_id
- name
- email
- country
- preferred_zones
- budget
- favorites
- created_at

---

## 4. Alerts

Alertas inteligentes.

### Campos

- alert_id
- user_id
- filter_type
- max_price
- city
- notification_type

---

## 5. Tourism Intelligence

Datos turísticos.

### Campos

- beach_score
- nightlife_score
- restaurant_score
- coworking_score
- walkability_score
- family_score

---

# IA futura

La IA analizará:

- precios
- zonas
- tendencias
- comportamiento usuarios
- turismo
- demanda
- oportunidades

---

# Tecnologías futuras

## Inicial

- CSV
- pandas

## Intermedio

- PostgreSQL
- SQLAlchemy

## Avanzado

- Vector DB
- Redis
- BigQuery
- embeddings
- feature store

---

# Arquitectura IA futura

Data Collection
↓
Feature Engineering
↓
AI Scoring
↓
Recommendation Engine
↓
Personalized Insights

---

# Visión final

Crear el grafo inteligente de oportunidades y lifestyle de la Costa Blanca.