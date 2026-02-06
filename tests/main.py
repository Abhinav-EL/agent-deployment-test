import os
import asyncio

from dotenv import load_dotenv
import vertexai
from google.adk.evaluation.agent_evaluator import AgentEvaluator

load_dotenv()

# Initialize Vertex AI
vertexai.init(
    project=os.getenv("GOOGLE_CLOUD_PROJECT"),
    location=os.getenv("GOOGLE_CLOUD_LOCATION"),
)

async def main():
    #print("hello, starting the agent tests now!")
    #await test_deployment_agent.test_agent_deployment()
    #await test_deployment.cleanup_deployed_agents()
    await AgentEvaluator.migrate_eval_data_to_new_schema(
        old_eval_data_file="tests/integration/fixture/weather_agent_eval.test.json",
        new_eval_data_file="tests/integration/fixture/weather_agent_eval_v2.test.json")


if __name__ == "__main__":
    asyncio.run(main())