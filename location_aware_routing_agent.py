import google.generativeai as genai
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(dotenv_path='key.env')

# 1. Setup your API Key (You can get a free one from Google AI Studio)
# Best Practice: Load from environment variable
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set")
genai.configure(api_key=api_key)

# 2. Define the Tool (The function the LLM is allowed to use)
def search_nearby_places(query: str, latitude: float, longitude: float, min_rating: float) -> str:
    """Searches for a specific type of place near the given coordinates."""
    
    print(f"\n[AGENT THOUGHT PROCESS] --> Decided to call 'search_nearby_places'")
    print(f"[AGENT THOUGHT PROCESS] --> Extracted Args: Query='{query}', Lat={latitude}, Lng={longitude}, Min Rating={min_rating}\n")
    
    # In production, you would make an HTTP request to the Google Places API here.
    # For this prototype, we return a mock JSON response to simulate the API.
    
    # Simple logic to make the mock slightly dynamic
    results = []
    if "veg" in query.lower() or "food" in query.lower():
        results.append({
            "name": "Minerva Coffee Shop",
            "rating": 5.0,
            "address": "Jubilee Hills",
            "distance_meters": 1500
        })

    mock_api_response = {
        "status": "OK",
        "results": results
    }
    return json.dumps(mock_api_response)

# 3. Initialize the Agent with the Tool
# We pass the Python function directly into the 'tools' parameter
agent = genai.GenerativeModel(
    model_name="models/gemini-2.5-flash",
    tools=[search_nearby_places],
    system_instruction="You are a helpful navigation assistant. Always use the search_nearby_places tool when asked for location recommendations."
)

# 4. Provide Context and Prompt
# Providing your current coordinates (Hyderabad center)
current_lat = 17.3850
current_lon = 78.4867

user_prompt = f"My current GPS coordinates are {current_lat}, {current_lon}. Where will I find veg food nearby with a 5-star rating?"

print(f"User Prompt: {user_prompt}")

# 5. Execute the Agent
# enable_automatic_function_calling=True allows the model to run the Python function and read the result
chat = agent.start_chat(enable_automatic_function_calling=True)
response = chat.send_message(user_prompt)

print("Agent Final Answer:")
print(response.text)