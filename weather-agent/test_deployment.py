import os
import vertexai
from vertexai import agent_engines

async def test_agent_deployment():
    print("✨ Starting Deployment Test...")
    # Initialize Vertex AI
    vertexai.init(
        project=os.getenv("GOOGLE_CLOUD_PROJECT"),
        location=os.getenv("GOOGLE_CLOUD_LOCATION"),
    )
    # Get the most recently deployed agent
    agents_list = list(agent_engines.list())
    if agents_list:
        remote_agent = agents_list[0]  # Get the first (most recent) agent
        client = agent_engines
        print(f"✅ Connected to deployed agent: {remote_agent.resource_name}")

        # Test a sample query
        async for item in remote_agent.async_stream_query(
            message="What is the weather in Tokyo?",
            user_id="user_42",
        ):
            print(item)
    else:
        print("❌ No agents found. Please deploy first.")

async def cleanup_deployed_agents():
    print("🧹 Starting Cleanup of Deployed Agents...")
    vertexai.init(
        project="gemini-kaggle-project-486119",
        location="us-east4",
    )
    agents_list = list(agent_engines.list())
    for agent in agents_list:
        print(f"Deleting agent: {agent.resource_name}")
        agent.delete()
    print("✅ Cleanup completed.")