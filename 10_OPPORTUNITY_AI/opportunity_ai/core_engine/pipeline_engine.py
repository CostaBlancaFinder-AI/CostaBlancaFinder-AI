"""
============================================================
OpportunityAI Platform
Universal Pipeline Engine
============================================================

Author:
George Apolo Gallardo

Project:
OpportunityAI Platform

Description:
Generic pipeline orchestration layer for multi-vertical
opportunity detection systems.

This engine defines the standard execution flow used by
real estate, jobs, flights, investments and business modules.

Architecture:
Source → Ingestion → Normalization → Scoring → Recommendation → Persistence

Created:
2026

Status:
Base architecture / MVP evolution
============================================================
"""


class PipelineEngine:
    """
    Universal pipeline engine for OpportunityAI verticals.
    """

    def __init__(self, name: str):
        self.name = name
        self.steps = []

    def add_step(self, step_name: str, function):
        """
        Adds a processing step to the pipeline.
        """
        self.steps.append({
            "name": step_name,
            "function": function
        })

    def run(self, data=None):
        """
        Executes all pipeline steps in sequence.
        """
        current_data = data

        print(f"Starting pipeline: {self.name}")

        for step in self.steps:
            print(f"Running step: {step['name']}")
            current_data = step["function"](current_data)

        print(f"Pipeline finished: {self.name}")
        return current_data
