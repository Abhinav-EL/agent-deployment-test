import asyncio
import test_deployment 

async def main():
    """Print hello world."""
    print("hello, starting the agent tests now!")
    await test_deployment.test_agent_deployment()
    #await test_deployment.cleanup_deployed_agents()


if __name__ == "__main__":
    asyncio.run(main())