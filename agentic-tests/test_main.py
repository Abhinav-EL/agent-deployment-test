import os
import asyncio

from dotenv import load_dotenv
import pytest
import vertexai
from test_deployment import test_agent_deployment, cleanup_deployed_agents

load_dotenv()

# Initialize Vertex AI
vertexai.init(
    project=os.getenv("GOOGLE_CLOUD_PROJECT"),
    location=os.getenv("GOOGLE_CLOUD_LOCATION"),
)

@pytest.mark.asyncio
async def main():
    print("hello, starting the agent tests now!")
    await test_agent_deployment()
    #await cleanup_deployed_agents()


if __name__ == "__main__":
    asyncio.run(main())