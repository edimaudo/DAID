import os
import httpx
from dotenv import load_dotenv

load_dotenv()

AIRIA_API_KEY = os.getenv("AIRIA_API_KEY")
AIRIA_BASE_URL = os.getenv("AIRIA_BASE_URL", "https://api.airia.ai/v1")

async def agent_framer(messy_input: str) -> str:
    """Extracts structured problem from messy input."""
    return f"Synthesized problem based on: {messy_input[:50]}..."

async def agent_solution_designer(clean_problem: str, framework_id: str) -> str:
    """
    Applies chosen framework. 
    If framework_id is 'auto-select', it asks the AI to choose the best one first.
    """
    headers = {
        "Authorization": f"Bearer {AIRIA_API_KEY}",
        "Content-Type": "application/json"
    }
    
    system_prompt = f"You are a strategy and operations consultant. Apply the {framework_id} framework to analyze the following problem. Generate the solution in a structured markdown format."
    
    if framework_id == "auto-select":
        system_prompt = "You are a strategy and operations consultant. First, analyze the problem and identify the single best strategic framework to solve it. Explain your choice, then apply that framework to generate a structured Markdown format."

    payload = {
        "model": "designer-model-id",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": clean_problem}
        ]
    }
    
    # Placeholder return for testing. In production, uncomment the httpx block below.
    return f"# \n\n**Framework Used:** {framework_id}\n\n**Analysis of:** {clean_problem}\n\n(AI generated content would appear here)"

    # async with httpx.AsyncClient() as client:
    #     response = await client.post(f"{AIRIA_BASE_URL}/chat/completions", json=payload, headers=headers)
    #     response.raise_for_status()
    #     data = response.json()
    #     return data['choices'][0]['message']['content']
