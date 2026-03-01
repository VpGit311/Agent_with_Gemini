# Location-Aware Routing Agent

This Python script demonstrates a simple location-aware routing agent using Google's Gemini API. The agent can take a user's current location (latitude and longitude) and a query (e.g., "veg food") and use a tool to find nearby places that match the query.

## How it Works

The script uses the `google.generativeai` library to create a generative model that is configured to use a custom tool. The tool, `search_nearby_places`, is a Python function that simulates a call to a places API.

When the user provides a prompt with their location and a query, the agent is able to parse the prompt, extract the relevant arguments, and call the `search_nearby_places` tool. The tool returns a mock JSON response, which the agent then uses to formulate a natural language response to the user.

## Setup

### 1. Installation

This script requires Python 3 and the following Python libraries:

*   `google-generativeai`
*   `python-dotenv`

You can install these dependencies using pip:

```bash
pip install google-generativeai python-dotenv
```

### 2. Configuration

The script requires a Gemini API key to be configured. The key is loaded from an environment variable named `GEMINI_API_KEY`.

1.  Create a file named `key.env` in the same directory as the script.
2.  Add the following line to the `key.env` file, replacing `YOUR_API_KEY` with your actual Gemini API key:

```
GEMINI_API_KEY=YOUR_API_KEY
```

The script will automatically load the API key from the `key.env` file.

## Usage

To run the script, execute the following command in your terminal:

```bash
python location_aware_routing_agent.py
```

The script will then print the user prompt, the agent's thought process, and the final answer.

### Example Output

```
User Prompt: My current GPS coordinates are 17.385, 78.4867. Where will I find veg food nearby with a 5-star rating?

[AGENT THOUGHT PROCESS] --> Decided to call 'search_nearby_places'
[AGENT THOUGHT PROCESS] --> Extracted Args: Query='veg food', Lat=17.385, Lng=78.4867, Min Rating=5.0

Agent Final Answer:
You can find a 5-star rated veg food option at Minerva Coffee Shop in Jubilee Hills, which is approximately 1500 meters from your current location.
```
