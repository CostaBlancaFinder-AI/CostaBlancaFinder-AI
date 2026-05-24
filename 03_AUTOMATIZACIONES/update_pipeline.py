# ============================================================
# CostaBlancaFinder AI
# Automated Data Pipeline with Error Control
# ============================================================

import os
import time
import subprocess
from datetime import datetime

log_path = "03_AUTOMATIZACIONES/logs/pipeline.log"


def write_log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_message = f"[{timestamp}] {message}"

    print(full_message)

    with open(log_path, "a") as log_file:
        log_file.write(full_message + "\n")


def run_step(step_name, command):
    write_log(f"Ejecutando: {step_name}")

    result = subprocess.run(
        command,
        shell=True
    )

    if result.returncode == 0:
        write_log(f"OK: {step_name}")
    else:
        write_log(f"ERROR: {step_name}")
        raise RuntimeError(f"Falló el paso: {step_name}")


write_log("===================================")
write_log("CostaBlancaFinder AI Pipeline")
write_log("===================================")

try:
    run_step(
        "[1/5] Scraper",
        "python3 02_DATA_IA/scrapers/idealista_scraper.py"
    )

    time.sleep(1)

    run_step(
        "[2/5] AI Scoring Agent",
        "python3 02_DATA_IA/scoring_engine/opportunity_score_v2.py"
    )

    time.sleep(1)

    run_step(
        "[3/5] Location Enrichment",
        "python3 02_DATA_IA/feature_engineering/location_enrichment.py"
    )

    time.sleep(1)

    run_step(
        "[4/5] Recommendation Engine",
        "python3 02_DATA_IA/recommendation_system/recommendation_engine.py"
    )

    time.sleep(1)

    write_log("[5/5] Dashboard actualizado.")
    write_log("Pipeline completado correctamente.")

except Exception as error:
    write_log(f"Pipeline detenido por error: {error}")