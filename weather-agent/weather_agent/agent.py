from dotenv import load_dotenv
from google.adk.agents import Agent
import vertexai
import os
import logging
from typing import Optional
from google.genai import types 
from google.adk.models import LlmResponse, LlmRequest
from google.adk.agents.callback_context import CallbackContext

load_dotenv()

vertexai.init(
    project=os.getenv("GOOGLE_CLOUD_PROJECT"),
    location=os.getenv("GOOGLE_CLOUD_LOCATION"),
)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s'
)

#TODO: Extracts city name from the user's question.
# Reference: https://github.com/google/adk-python/blob/main/src/google/adk/models/llm_request.py
def check_city_in_question(
    callback_context: CallbackContext, llm_request: LlmRequest
) -> Optional[LlmResponse]:
    logging.info(f"Checking city in question for agent: {callback_context.agent_name}")
    llm_context = llm_request.contents
    logging.info(f"Checking city in question: {llm_context}")
    if not llm_context:
        return LlmResponse(
            content=types.Content(
                role="model",
                parts=[types.Part(text="LLM call was blocked by before_model_callback because it has no contents.")],
            ))
    return None

def get_available_cities() -> list:
    """Returns a list of available cities."""
    return ["San Francisco", "New York", "London", "Tokyo", "Paris"]

def get_weather(city: str) -> dict:
    """
    Returns weather information for a given city.

    This is a TOOL that the agent can call when users ask about weather.
    In production, this would call a real weather API (e.g., OpenWeatherMap).
    For this demo, we use mock data.

    Args:
        city: Name of the city (e.g., "Tokyo", "New York")

    Returns:
        dict: Dictionary with status and weather report or error message
    """
    # Mock weather database with structured responses
    weather_data = {
        "san francisco": {"status": "success", "report": "The weather in San Francisco is sunny with a temperature of 72°F (22°C)."},
        "new york": {"status": "success", "report": "The weather in New York is cloudy with a temperature of 65°F (18°C)."},
        "london": {"status": "success", "report": "The weather in London is rainy with a temperature of 58°F (14°C)."},
        "tokyo": {"status": "success", "report": "The weather in Tokyo is clear with a temperature of 70°F (21°C)."},
        "paris": {"status": "success", "report": "The weather in Paris is partly cloudy with a temperature of 68°F (20°C)."}
    }

    city_lower = city.lower()
    logging.info(f"Fetching weather for city: {city_lower}")
    if city_lower in weather_data:
        return weather_data[city_lower]
    else:
        available_cities = ", ".join([c.title() for c in get_available_cities()])
        logging.error(f"Only weather available for cities: {available_cities}")
        return {
            "status": "error",
            "error_message": f"Weather information for '{city}' is not available. Try: {available_cities}"
        }

root_agent = Agent(
    name="weather_assistant",
    model="gemini-2.5-flash-lite",  # Fast, cost-effective Gemini model
    description="A helpful weather assistant that provides weather information for cities.",
    instruction="""
    You are a friendly weather assistant. When users ask about the weather:

    1. Identify the city name from their question.
    2. Use the get_weather tool to fetch current weather information
    3. Conversational tone is not needed, just provide the weather report based on the tool's response.
    4. If there is an error from get_weather tool, inform the user.

    Be helpful and concise in your responses.
    """,
    tools=[get_weather],
    before_model_callback=check_city_in_question # Block LLM calls without appropriate city
)