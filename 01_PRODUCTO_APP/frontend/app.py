# ============================================================
# CostaBlancaFinder AI
# Streamlit Dashboard V2
# ============================================================

import streamlit as st
import sys
from pathlib import Path
from streamlit_folium import st_folium

# ============================================================
# ROOT CONFIGURATION
# ============================================================

ROOT_DIR = Path(__file__).resolve().parents[2]
APP_DIR = ROOT_DIR / "01_PRODUCTO_APP"

sys.path.append(str(APP_DIR))
sys.path.append(str(APP_DIR / "config"))
sys.path.append(str(APP_DIR / "services"))
sys.path.append(str(APP_DIR / "utils"))

# ============================================================
# CONFIG IMPORTS
# ============================================================

from settings import APP_NAME

# ============================================================
# SERVICES IMPORTS
# ============================================================

from analytics_service import (
    get_total_properties,
    get_average_price,
    get_best_opportunity,
)

from recommendation_service import (
    load_recommendations,
    has_recommendations,
)

from map_service import (
    create_base_map,
    add_location_markers,
)

from search_service import filter_properties

from scoring_service import (
    get_best_opportunity_from_df,
    get_top_opportunities,
    get_average_opportunity_score,
    get_average_price_m2,
)

# ============================================================
# DATABASE IMPORTS
# ============================================================

from database.property_repository import load_properties
from database.location_repository import load_locations

# ------------------------------------------------------------
# CONFIGURACIÓN GENERAL
# ------------------------------------------------------------

st.set_page_config(
    page_title="CostaBlancaFinder AI",
    page_icon="🏖️",
    layout="wide"
)

# ------------------------------------------------------------
# CARGA DE DATOS
# ------------------------------------------------------------

df = load_properties()

# ------------------------------------------------------------
# SIDEBAR
# ------------------------------------------------------------

st.sidebar.title("🏖️ CostaBlancaFinder AI")

st.sidebar.markdown("""
Panel inteligente de oportunidades inmobiliarias en la Costa Blanca.
""")

st.sidebar.header("Filtros")

city_filter = st.sidebar.selectbox(
    "Ciudad",
    ["Todas"] + sorted(df["city"].unique().tolist())
)

max_price = st.sidebar.slider(
    "Precio máximo (€)",
    min_value=int(df["price_eur"].min()),
    max_value=int(df["price_eur"].max()),
    value=int(df["price_eur"].max())
)

rooms_filter = st.sidebar.selectbox(
    "Habitaciones mínimas",
    sorted(df["rooms"].unique().tolist())
)

# ------------------------------------------------------------
# FILTRADO DE DATOS
# ------------------------------------------------------------

df_filtered = filter_properties(
    df=df,
    city_filter=city_filter,
    max_price=max_price,
    min_rooms=rooms_filter
)

# ------------------------------------------------------------
# CABECERA PRINCIPAL
# ------------------------------------------------------------

st.title("🏖️ CostaBlancaFinder AI")
st.subheader("Panel de Inteligencia de Mercado V2")

st.markdown("""
Plataforma inteligente para detectar oportunidades inmobiliarias
en la Costa Blanca utilizando análisis de datos e IA.
""")

st.divider()

# ------------------------------------------------------------
# MÉTRICAS PRINCIPALES
# ------------------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Propiedades filtradas",
    len(df_filtered)
)

if not df_filtered.empty:

    col2.metric(
        "Precio medio (€)",
        round(df_filtered["price_eur"].mean(), 2)
    )

    col3.metric(
    "€/m² medio",
    get_average_price_m2(df_filtered)
    )

    col4.metric(
    "Score medio",
    get_average_opportunity_score(df_filtered)
    )

else:

    col2.metric("Precio medio (€)", 0)
    col3.metric("€/m² medio", 0)
    col4.metric("Score medio", 0)

st.divider()

# ------------------------------------------------------------
# MEJOR OPORTUNIDAD
# ------------------------------------------------------------

st.subheader("🔥 Mejor oportunidad actual")

if not df_filtered.empty:

    best = get_best_opportunity_from_df(df_filtered)

    st.success(
        f"{best['city']} - {best['zone']} | "
        f"{best['price_eur']} € | "
        f"{best['area_m2']} m² | "
        f"{best['rooms']} habitaciones | "
        f"Score: {best['opportunity_score']}"
    )

else:

    st.warning(
        "No hay propiedades que cumplan los filtros seleccionados."
    )

st.divider()

# ------------------------------------------------------------
# TABLA PRINCIPAL
# ------------------------------------------------------------

st.subheader("Clasificación de oportunidades")

if not df_filtered.empty:

    st.dataframe(
        df_filtered.sort_values(
            "opportunity_score",
            ascending=False
        ),
        use_container_width=True
    )

else:

    st.info("Ajusta los filtros para ver resultados.")

# ------------------------------------------------------------
# TOP 3 OPORTUNIDADES
# ------------------------------------------------------------

st.subheader("Top 3 oportunidades")

if not df_filtered.empty:

    top3 = get_top_opportunities(df_filtered)

    st.dataframe(
        top3[[
            "city",
            "zone",
            "title",
            "price_eur",
            "area_m2",
            "rooms",
            "price_m2",
            "opportunity_score"
        ]],
        use_container_width=True
    )

else:

    st.info("No hay datos suficientes para mostrar el Top 3.")

# ------------------------------------------------------------
# GRÁFICO
# ------------------------------------------------------------

st.subheader("Puntuación de oportunidad por ciudad")

if not df_filtered.empty:

    chart_data = df_filtered[[
        "city",
        "opportunity_score"
    ]].set_index("city")

    st.bar_chart(chart_data)

else:

    st.info("No hay datos para generar el gráfico.")

st.divider()

# ------------------------------------------------------------
# INSIGHT AUTOMÁTICO
# ------------------------------------------------------------

st.subheader("Insight automático")

if not df_filtered.empty:

    st.info(
        f"El sistema ha analizado {len(df_filtered)} propiedades filtradas. "
        f"La mejor oportunidad actual se encuentra en {best['city']} "
        f"con una puntuación de {best['opportunity_score']}."
    )

else:

    st.warning(
        "No se puede generar insight porque no hay datos filtrados."
    )

# ============================================================
# MAPA COSTA BLANCA
# ============================================================

st.divider()

st.subheader("Mapa Inteligente Costa Blanca")

locations = load_locations()

m = create_base_map()
m = add_location_markers(m, locations)

st_folium(
    m,
    width=1200,
    height=500
)

# ============================================================
# RECOMENDACIONES IA
# ============================================================

st.divider()

st.subheader("Recomendaciones IA")

recommendations = load_recommendations()

if has_recommendations(recommendations):

    st.dataframe(
        recommendations[[
            "city",
            "zone",
            "title",
            "price_eur",
            "rooms",
            "lifestyle_score",
            "opportunity_score",
            "opportunity_level"
        ]],
        use_container_width=True
    )

else:

    st.info("No hay recomendaciones disponibles.")