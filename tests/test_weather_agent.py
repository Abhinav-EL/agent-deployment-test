import os

from vertexai import agent_engines

async def test_agent_deployment():
    if not os.getenv("GOOGLE_CLOUD_PROJECT") or not os.getenv("GOOGLE_CLOUD_LOCATION"):
        print("❌ GOOGLE_CLOUD_PROJECT and GOOGLE_CLOUD_LOCATION must be set.")
        return
    
    print("✨ Starting Deployment Test for : ", os.getenv("GOOGLE_CLOUD_LOCATION"))
    # Get the most recently deployed agent
    agents_list = list(agent_engines.list())
    if agents_list:
        remote_agent = agents_list[0]  # Get the first (most recent) agent
        client = agent_engines
        print(f"✅ Connected to deployed agent: {remote_agent.resource_name}")

        # Test a sample query
        async for item in remote_agent.async_stream_query(
            message="What is the weather in NYC?",
            user_id="user_43",
        ):
            print(item)
    else:
        print("❌ No agents found. Please deploy first.")

async def cleanup_deployed_agents():
    print("🧹 Starting Cleanup of Deployed Agents...")

    agents_list = list(agent_engines.list())
    for agent in agents_list:
        print(f"Deleting agent: {agent.resource_name}")
        agent.delete()
    print("✅ Cleanup completed.")