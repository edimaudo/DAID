import os
import httpx
from dotenv import load_dotenv

load_dotenv()

AIRIA_API_KEY = os.getenv("AIRIA_API_KEY")
AIRIA_BASE_URL = os.getenv("AIRIA_BASE_URL", "https://api.airia.ai/v1") # Replace with actual Airia endpoint

async def agent_framer(messy_input: str) -> str:
    """
    Agent 1: Takes messy input and returns a structured problem statement.
    """
    headers = {
        "Authorization": f"Bearer {AIRIA_API_KEY}",
        "Content-Type": "application/json"
    }
    
    # Structure the payload according to Airia's expected format
    payload = {
        "model": "framer-model-id", # Replace with your specific Airia model ID
        "messages": [
            {"role": "system", "content": "You are a diagnostic agent. Use the 5 Whys and Design Thinking to extract the core problem from the user's input. Return ONLY a concise, clean problem statement."},
            {"role": "user", "content": messy_input}
        ]
    }
    
    async with httpx.AsyncClient() as client:
        # Mocking the call for safety. Replace with actual POST request when ready:
        # response = await client.post(f"{AIRIA_BASE_URL}/chat/completions", json=payload, headers=headers)
        # response.raise_for_status()
        # data = response.json()
        # return data['choices'][0]['message']['content']
        
        # Placeholder return for local testing
        return f"Synthesized problem based on: {messy_input[:50]}..."

async def agent_solution_designer(clean_problem: str, framework_id: str) -> str:
    """
    Agent 2: Takes the clean problem and applies the chosen framework logic.
    """
    headers = {
        "Authorization": f"Bearer {AIRIA_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "designer-model-id", # Replace with your specific Airia model ID
        "messages": [
            {"role": "system", "content": f"You are a strategic advisor. Apply the {framework_id} framework to analyze the following problem. Generate a structured Markdown memo."},
            {"role": "user", "content": clean_problem}
        ]
    }
    
    async with httpx.AsyncClient() as client:
        # Mocking the call:
        # response = await client.post(f"{AIRIA_BASE_URL}/chat/completions", json=payload, headers=headers)
        # response.raise_for_status()
        # data = response.json()
        # return data['choices'][0]['message']['content']
        
        # Placeholder return for local testing
        return f"# Strategic Memo\n\n**Framework:** {framework_id}\n**Problem:** {clean_problem}\n\n### Analysis\n(Agent 2 generated content here...)"
