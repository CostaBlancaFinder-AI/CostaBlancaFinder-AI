"""
============================================================
CostaBlancaFinder AI
Streamlit Dashboard
============================================================

Author:
George Apolo Gallardo

Project:
CostaBlancaFinder AI

Description:
Professional Streamlit dashboard for visualizing real estate
opportunities, AI-based scoring metrics, PostgreSQL/Supabase
data, ingestion pipeline status and intelligent property
recommendations.

Architecture:
PropTech + AI + PostgreSQL + Supabase + Streamlit

Created:
2026

Status:
MVP / Production-oriented architecture
============================================================
"""

import sys
from pathlib import Path

import streamlit as st
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

from recommendation_service import (
    load_recommendations,
    has_recommendations,
)

from map_service import (
    create_base_map,
    add_location_markers,
    add_property_markers,
    add_opportunity_heatmap,
)

from search_service import filter_properties

from scoring_service import (
    get_best_opportunity_from_df,
    get_top_opportunities,
    get_average_opportunity_score,
    get_average_price_m2,
    get_average_price_from_df,
    get_average_value_score,
    get_average_comfort_score,
    get_average_quality_score,
)

from ingestion_monitoring_service import (
    get_last_ingestion_summary,
)

from geo_clustering_service import (
    detect_geo_clusters,
)


# ============================================================
# DATABASE IMPORTS
# ============================================================

from database.property_repository import load_properties
from database.location_repository import load_locations


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="CostaBlancaFinder AI",
    page_icon="🏖️",
    layout="wide",
)


# ============================================================
# LOAD DATA
# ============================================================

df = load_properties()


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🏖️ CostaBlancaFinder AI")

st.sidebar.markdown("""
Plataforma inteligente de oportunidades inmobiliarias.
""")

st.sidebar.header("Filtros")

city_filter = st.sidebar.selectbox(
    "Ciudad",
    ["Todas"] + sorted(df["city"].dropna().unique().tolist()),
)

max_price = st.sidebar.slider(
    "Precio máximo (€)",
    min_value=int(df["price_eur"].min()),
    max_value=int(df["price_eur"].max()),
    value=int(df["price_eur"].max()),
)

rooms_filter = st.sidebar.selectbox(
    "Habitaciones mínimas",
    sorted(df["rooms"].dropna().unique().tolist()),
)


# ============================================================
# FILTER DATA
# ============================================================

df_filtered = filter_properties(
    df=df,
    city_filter=city_filter,
    max_price=max_price,
    min_rooms=rooms_filter,
)


# ============================================================
# MAIN HEADER
# ============================================================

st.title("🏖️ CostaBlancaFinder AI")
st.subheader("AI Real Estate Intelligence Platform")

st.markdown("""
Sistema inteligente para detectar oportunidades inmobiliarias
mediante scoring multicriterio, análisis de valor y confort.
""")


# ============================================================
# PIPELINE STATUS
# ============================================================

pipeline_summary = get_last_ingestion_summary()

st.success(
    f"""
🟢 Pipeline Status: {pipeline_summary['status']}

📡 Fuente: {pipeline_summary['source_name']}

🏠 Raw Properties: {pipeline_summary['total_raw']}  
🧹 Normalized: {pipeline_summary['total_normalized']}  
🎯 Filtered: {pipeline_summary['total_filtered']}  
💾 Saved: {pipeline_summary['total_saved']}  

📝 {pipeline_summary['message']}
"""
)

st.divider()


# ============================================================
# MAIN METRICS
# ============================================================

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Propiedades",
    len(df_filtered),
)

if not df_filtered.empty:

    col2.metric(
        "Precio medio (€)",
        round(get_average_price_from_df(df_filtered), 0),
    )

    col3.metric(
        "€/m² medio",
        round(get_average_price_m2(df_filtered), 2),
    )

    col4.metric(
        "Opportunity Score",
        round(get_average_opportunity_score(df_filtered), 2),
    )

else:

    col2.metric("Precio medio (€)", 0)
    col3.metric("€/m² medio", 0)
    col4.metric("Opportunity Score", 0)


# ============================================================
# SECONDARY METRICS
# ============================================================

if not df_filtered.empty:

    st.divider()

    col5, col6, col7 = st.columns(3)

    col5.metric(
        "Value Score",
        round(get_average_value_score(df_filtered), 2),
    )

    col6.metric(
        "Comfort Score",
        round(get_average_comfort_score(df_filtered), 2),
    )

    col7.metric(
        "Quality Score",
        round(get_average_quality_score(df_filtered), 2),
    )


# ============================================================
# BEST OPPORTUNITY
# ============================================================

st.divider()

st.subheader("🔥 Mejor oportunidad detectada")

if not df_filtered.empty:

    best = get_best_opportunity_from_df(df_filtered)

    st.success(
        f"""
🏆 {best['city']} - {best['zone']}

💰 {best['price_eur']} €  
📐 {best['area_m2']} m²  
🛏️ {best['rooms']} habitaciones  
📊 Opportunity Score: {best['opportunity_score']}

💎 Value Score: {round(best['value_score'], 2)}  
🌴 Comfort Score: {round(best['comfort_score'], 2)}  
📸 Quality Score: {round(best['quality_score'], 2)}
"""
    )

else:

    st.warning(
        "No hay propiedades que cumplan los filtros."
    )


# ============================================================
# MAIN TABLE
# ============================================================

st.divider()

st.subheader("🏆 Ranking Inteligente")

if not df_filtered.empty:

    ranking_df = get_top_opportunities(
        df_filtered,
        top_n=len(df_filtered),
    )

    st.dataframe(
        ranking_df[[
            "city",
            "zone",
            "title",
            "price_eur",
            "area_m2",
            "rooms",
            "price_by_m2",
            "value_score",
            "comfort_score",
            "quality_score",
            "opportunity_score",
            "opportunity_level",
        ]],
        use_container_width=True,
    )

else:

    st.info("No hay resultados.")


# ============================================================
# TOP 3 CARDS
# ============================================================

st.divider()

st.subheader("🥇 Top 3 oportunidades")

if not df_filtered.empty:

    top3 = get_top_opportunities(
        df_filtered,
        top_n=3,
    )

    for _, row in top3.iterrows():

        st.markdown("---")

        st.markdown(
            f"""
### 🏠 {row['title']}

📍 {row['city']} — {row['zone']}

💰 {row['price_eur']} €  
📐 {row['area_m2']} m²  
🛏️ {row['rooms']} habitaciones  
📊 Opportunity Score: **{row['opportunity_score']}**  
🏅 Nivel: **{row['opportunity_level']}**
"""
        )


# ============================================================
# CHART
# ============================================================

st.divider()

st.subheader("📈 Opportunity Score por ciudad")

if not df_filtered.empty:

    chart_data = df_filtered[[
        "city",
        "opportunity_score",
    ]].set_index("city")

    st.bar_chart(chart_data)


# ============================================================
# GEOAI CLUSTERS
# ============================================================

st.divider()

st.subheader("🧠 Clusters GeoAI de oportunidades")

clusters_df = detect_geo_clusters(df_filtered)

if not clusters_df.empty:

    st.dataframe(
        clusters_df,
        width="stretch"
    )

else:

    st.info("No hay datos suficientes para calcular clusters GeoAI.")

# ============================================================
# AI INSIGHT
# ============================================================

st.divider()

st.subheader("🤖 Insight IA")

if not df_filtered.empty:

    best_city = (
        df_filtered
        .sort_values(
            by="opportunity_score",
            ascending=False,
        )
        .iloc[0]["city"]
    )

    st.info(
        f"""
El sistema ha analizado {len(df_filtered)} propiedades.

La ciudad con mejores oportunidades actuales es:
🏆 {best_city}

El modelo detecta oportunidades combinando:
- valor económico,
- precio/m²,
- confort,
- amenities,
- calidad del anuncio.
"""
    )


# ============================================================
# MAP
# ============================================================

st.divider()

st.subheader("🗺️ Mapa Inteligente Costa Blanca")

locations = load_locations()

m = create_base_map()

m = add_opportunity_heatmap(
    m,
    df_filtered
)

m = add_location_markers(
    m,
    locations
)

m = add_property_markers(
    m,
    df_filtered
)

st_folium(
    m,
    width=1200,
    height=500,
)


# ============================================================
# AI RECOMMENDATIONS
# ============================================================

st.divider()

st.subheader("🤖 Recomendaciones IA")

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
            "opportunity_level",
        ]],
        use_container_width=True,
    )

else:

    st.info("No hay recomendaciones disponibles.")