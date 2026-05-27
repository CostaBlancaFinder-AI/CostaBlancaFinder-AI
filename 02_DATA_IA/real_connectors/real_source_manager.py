"""
============================================================
CostaBlancaFinder AI
Real Source Manager
============================================================
"""

from apify_idealista import fetch_idealista_properties
from apify_fotocasa import fetch_fotocasa_properties
from apify_habitaclia import fetch_habitaclia_properties


def attach_source(properties: list, source_name: str) -> list:
    """
    Añade source_name a cada propiedad.
    """

    enriched = []

    for item in properties:
        item_copy = item.copy()

        if not item_copy.get("source_name"):
            item_copy["source_name"] = source_name

        enriched.append(item_copy)

    return enriched


def fetch_all_real_sources() -> list:
    """
    Ejecuta todos los conectores reales disponibles.
    """

    all_properties = []

    print("\n====================================================")
    print("EJECUTANDO CONECTORES REALES")
    print("====================================================")

    # ========================================================
    # IDEALISTA
    # ========================================================

    try:
        idealista_properties = fetch_idealista_properties()

        if idealista_properties:
            idealista_properties = attach_source(
                idealista_properties,
                "idealista_apify"
            )

            all_properties.extend(idealista_properties)

            print(
                f"Idealista OK → "
                f"{len(idealista_properties)} propiedades"
            )
        else:
            print("Idealista → sin resultados.")

    except Exception as error:
        print("Error en Idealista:")
        print(error)

    # ========================================================
    # FOTOCASA
    # ========================================================

    try:
        fotocasa_properties = fetch_fotocasa_properties()

        if fotocasa_properties:
            fotocasa_properties = attach_source(
                fotocasa_properties,
                "fotocasa_apify"
            )

            all_properties.extend(fotocasa_properties)

            print(
                f"Fotocasa OK → "
                f"{len(fotocasa_properties)} propiedades"
            )
        else:
            print("Fotocasa → sin resultados.")

    except Exception as error:
        print("Error en Fotocasa:")
        print(error)

    # ========================================================
    # HABITACLIA
    # ========================================================

    try:
        habitaclia_properties = fetch_habitaclia_properties()

        if habitaclia_properties:
            habitaclia_properties = attach_source(
                habitaclia_properties,
                "habitaclia_apify"
            )

            all_properties.extend(habitaclia_properties)

            print(
                f"Habitaclia OK → "
                f"{len(habitaclia_properties)} propiedades"
            )
        else:
            print("Habitaclia → sin resultados.")

    except Exception as error:
        print("Error en Habitaclia:")
        print(error)

    print("====================================================")
    print(f"TOTAL PROPIEDADES REALES: {len(all_properties)}")
    print("====================================================")

    return all_properties


if __name__ == "__main__":
    properties = fetch_all_real_sources()

    print(
        f"\nTotal propiedades reales obtenidas: "
        f"{len(properties)}"
    )