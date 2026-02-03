import os
import asyncio

from dotenv import load_dotenv
import vertexai
import test_weather_agent 

load_dotenv()

# Initialize Vertex AI
vertexai.init(
    project=os.getenv("GOOGLE_CLOUD_PROJECT"),
    location=os.getenv("GOOGLE_CLOUD_LOCATION"),
)

async def main():
    """Print hello world."""
    print("hello, starting the agent tests now!")
    await test_weather_agent.test_agent_deployment()
    #await test_deployment.cleanup_deployed_agents()


if __name__ == "__main__":
    asyncio.run(main())