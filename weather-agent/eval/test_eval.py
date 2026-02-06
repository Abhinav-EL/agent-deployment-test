import pathlib
import pytest
from google.adk.evaluation.agent_evaluator import AgentEvaluator


# Examples: https://github.com/google/adk-samples/tree/main/python

@pytest.mark.asyncio
async def test_with_single_test_file():
    """Test the agent's basic ability via a session file."""
    await AgentEvaluator.evaluate(
        agent_module="weather_agent.agent",
        eval_dataset_file_path_or_dir=str(
            pathlib.Path(__file__).parent / "data/weather_agent_eval_v2.test.json"
        ),
        num_runs=1,
    )