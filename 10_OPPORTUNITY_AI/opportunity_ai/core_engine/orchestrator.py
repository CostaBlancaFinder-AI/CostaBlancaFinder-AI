"""
============================================================
OpportunityAI Platform
Core Orchestrator
============================================================

Author:
George Apolo Gallardo

Project:
OpportunityAI Platform / CostaBlancaFinder AI

Description:
Central orchestration layer responsible for launching
vertical pipelines from one unified control point.

Created:
2026

Status:
MVP orchestration layer
============================================================
"""

from opportunity_ai.verticals.real_estate.pipelines.real_estate_pipeline import (
    build_real_estate_pipeline,
)


class OpportunityAIOrchestrator:
    """
    Central orchestrator for OpportunityAI Platform.
    """

    def __init__(self):
        self.available_pipelines = {
            "real_estate": build_real_estate_pipeline,
        }

    def list_pipelines(self):
        """
        Lists available vertical pipelines.
        """
        return list(self.available_pipelines.keys())

    def run_pipeline(self, pipeline_name: str):
        """
        Runs a selected vertical pipeline.
        """
        if pipeline_name not in self.available_pipelines:
            raise ValueError(
                f"Pipeline '{pipeline_name}' is not available. "
                f"Available pipelines: {self.list_pipelines()}"
            )

        pipeline = self.available_pipelines[pipeline_name]()
        return pipeline.run()


if __name__ == "__main__":
    orchestrator = OpportunityAIOrchestrator()

    print("Available pipelines:")
    print(orchestrator.list_pipelines())

    print("\nRunning real_estate pipeline...")
    result = orchestrator.run_pipeline("real_estate")

    print("\nPipeline result preview:")
    print(result.head() if hasattr(result, "head") else result)
