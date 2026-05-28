"""
============================================================
OpportunityAI Platform
Command Line Runner
============================================================

Author:
George Apolo Gallardo

Project:
OpportunityAI Platform

Description:
Command line entry point to run OpportunityAI vertical pipelines.

Usage:
PYTHONPATH=10_OPPORTUNITY_AI python3 10_OPPORTUNITY_AI/run_opportunity_ai.py real_estate

Created:
2026

Status:
MVP CLI runner
============================================================
"""

import sys

from opportunity_ai.core_engine.orchestrator import OpportunityAIOrchestrator


def main():
    orchestrator = OpportunityAIOrchestrator()

    if len(sys.argv) < 2:
        print("No pipeline selected.")
        print("Available pipelines:")
        print(orchestrator.list_pipelines())
        print("\nUsage:")
        print("PYTHONPATH=10_OPPORTUNITY_AI python3 10_OPPORTUNITY_AI/run_opportunity_ai.py real_estate")
        return

    pipeline_name = sys.argv[1]

    print(f"Launching OpportunityAI pipeline: {pipeline_name}")
    result = orchestrator.run_pipeline(pipeline_name)

    print("\nExecution finished.")

    if hasattr(result, "head"):
        print(result.head())


if __name__ == "__main__":
    main()
