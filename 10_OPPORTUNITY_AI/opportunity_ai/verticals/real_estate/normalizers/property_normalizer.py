"""
============================================================
CostaBlancaFinder AI
Universal Property Normalizer
============================================================
"""

import pandas as pd


STANDARD_COLUMNS = [
    "property_id",
    "title",
    "description",
    "city",
    "zone",
    "address",
    "price_eur",
    "price_by_m2",
    "area_m2",
    "rooms",
    "bathrooms",
    "floor",
    "property_type",
    "operation",
    "latitude",
    "longitude",
    "thumbnail",
    "num_photos",
    "has_lift",
    "has_terrace",
    "has_air_conditioning",
    "has_swimming_pool",
    "has_garden",
    "has_parking",
    "source_url",
    "source_name",
    "scraped_at"
]


def get_first_available(item: dict, possible_keys: list):
    for key in possible_keys:
        value = item.get(key)

        if value not in [None, ""]:
            return value

    return None


def to_int(value):
    try:
        if value in [None, ""]:
            return None
        return int(float(value))
    except (ValueError, TypeError):
        return None


def to_float(value):
    try:
        if value in [None, ""]:
            return None
        return float(value)
    except (ValueError, TypeError):
        return None


def to_bool(value):
    if isinstance(value, bool):
        return value

    if value in [1, "1", "true", "True", "yes", "Yes", "sí", "Si"]:
        return True

    if value in [0, "0", "false", "False", "no", "No"]:
        return False

    return False


def extract_parking(item: dict) -> bool:
    parking = item.get("hasParkingSpace")

    if isinstance(parking, dict):
        return bool(parking.get("hasParkingSpace", False))

    return to_bool(parking)


def normalize_property(item: dict, source_name: str) -> dict:
    """
    Normaliza una única propiedad.
    """

    title = get_first_available(
        item,
        ["title", "name", "headline", "address"]
    )

    city = get_first_available(
        item,
        ["city", "municipality", "location"]
    )

    zone = get_first_available(
        item,
        ["zone", "district", "neighborhood", "areaName"]
    )

    return {
        "property_id": get_first_available(
            item,
            ["property_id", "propertyCode", "id", "code"]
        ),
        "title": title,
        "description": get_first_available(
            item,
            ["description", "summary", "text"]
        ),
        "city": city,
        "zone": zone,
        "address": get_first_available(
            item,
            ["address", "street", "fullAddress"]
        ),
        "price_eur": to_int(
            get_first_available(
                item,
                ["price_eur", "price", "rent_price", "monthlyPrice"]
            )
        ),
        "price_by_m2": to_float(
            get_first_available(
                item,
                ["price_by_m2", "priceByArea", "price_m2"]
            )
        ),
        "area_m2": to_float(
            get_first_available(
                item,
                ["area_m2", "size", "area", "surface", "m2"]
            )
        ),
        "rooms": to_int(
            get_first_available(
                item,
                ["rooms", "bedrooms", "numRooms"]
            )
        ),
        "bathrooms": to_int(
            get_first_available(
                item,
                ["bathrooms", "bathroomsNumber", "numBathrooms"]
            )
        ),
        "floor": get_first_available(
            item,
            ["floor", "floorInfo"]
        ),
        "property_type": get_first_available(
            item,
            ["property_type", "propertyType", "type", "typology"]
        ),
        "operation": get_first_available(
            item,
            ["operation", "operationType"]
        ),
        "latitude": to_float(
            get_first_available(
                item,
                ["latitude", "lat"]
            )
        ),
        "longitude": to_float(
            get_first_available(
                item,
                ["longitude", "lng", "lon"]
            )
        ),
        "thumbnail": get_first_available(
            item,
            ["thumbnail", "image", "image_url", "mainImage"]
        ),
        "num_photos": to_int(
            get_first_available(
                item,
                ["numPhotos", "num_photos", "photosCount"]
            )
        ),
        "has_lift": to_bool(
            get_first_available(
                item,
                ["hasLift", "lift", "has_lift"]
            )
        ),
        "has_terrace": to_bool(
            get_first_available(
                item,
                ["hasTerrace", "terrace", "has_terrace"]
            )
        ),
        "has_air_conditioning": to_bool(
            get_first_available(
                item,
                ["hasAirConditioning", "airConditioning", "has_air_conditioning"]
            )
        ),
        "has_swimming_pool": to_bool(
            get_first_available(
                item,
                ["hasSwimmingPool", "swimmingPool", "has_swimming_pool"]
            )
        ),
        "has_garden": to_bool(
            get_first_available(
                item,
                ["hasGarden", "garden", "has_garden"]
            )
        ),
        "has_parking": extract_parking(item),
        "source_url": get_first_available(
            item,
            ["source_url", "url", "detailUrl", "link"]
        ),
        "source_name": item.get("source_name", source_name),
        "scraped_at": get_first_available(
            item,
            ["scrapedAt", "scraped_at", "createdAt"]
        )
    }


def normalize_properties(
    raw_properties: list,
    source_name: str
) -> pd.DataFrame:
    """
    Normaliza una lista de propiedades al formato estándar.
    """

    normalized = []

    for item in raw_properties:
        normalized.append(
            normalize_property(
                item=item,
                source_name=source_name
            )
        )

    df = pd.DataFrame(normalized)

    for column in STANDARD_COLUMNS:
        if column not in df.columns:
            df[column] = None

    return df[STANDARD_COLUMNS]