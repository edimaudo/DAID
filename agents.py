import os
import httpx
import json
from fastapi import HTTPException
from dotenv import load_dotenv

load_dotenv()

AIRIA_USER_ID = os.getenv("AIRIA_USER_ID")
AIRIA_KEY = os.getenv("AIRIA_API_KEY")
AIRIA_AGENT_URL_FRAMER = os.getenv("AIRIA_AGENT_URL_FRAMER")
AIRIA_AGENT_ID_FRAMER = os.getenv("AIRIA_AGENT_ID_FRAMER")
AIRIA_AGENT_URL_SOLUTION = os.getenv("AIRIA_AGENT_URL_SOLUTION")
AIRIA_AGENT_ID_SOLUTION = os.getenv("AIRIA_AGENT_ID_SOLUTION")

async def agent_framer(question: str):
    """Extracts structured problem from question leveraging airia"""
    if not AIRIA_KEY or not AIRIA_AGENT_ID_FRAMER:
        raise HTTPException(
            status_code=500,
            detail="Airia configuration (API Key or Framer Agent ID) is missing",
        )
    headers = {"X-API-Key": AIRIA_KEY, "Content-Type": "application/json"}

    # FRAMER Payload structure
    payload = {
        "agent_id": AIRIA_AGENT_ID_FRAMER,
        "UserInput": question,
        "UserId": AIRIA_USER_ID, 
    }
    
    async with httpx.AsyncClient() as client:
        try:
            # 3. Execution call
            response = await client.post(
                AIRIA_AGENT_URL_FRAMER, json=payload, headers=headers, timeout=60.0
            )

            response.raise_for_status()

            data = response.json()

            answer = (
                data.get("output")
                or data.get("response")
                or data.get("result")
                or data.get("text")
                or "The agent processed the request but returned an empty or unknown format."
            )

            if isinstance(answer, str):
                try:
                    answer = json.loads(answer)
                except json.JSONDecodeError:
                    pass

            if isinstance(answer, dict):
                reasoning = answer.get("reasoning", "")
                problem = answer.get("problem", "")
                reframed_problem = answer.get("reframed_problem", "")


                answer = (
                    f"### Problem Statement\n{problem}\n\n"
                    f"### Revised Problem Statemnt\n{reframed_problem}\n\n"
                    f"### Reasoning\n{reasoning}\n\n"
                )

            return str(answer)

        except httpx.HTTPStatusError as e:

            error_detail = (
                f"Airia API Error: {e.response.status_code} - {e.response.text}"
            )
            print(error_detail) 
            raise HTTPException(status_code=500, detail=error_detail)

        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Internal Logic Error: {str(e)}"
            )

# async def agent_solution_designer(clean_problem: str, framework_id: str) -> str:
#     """
#     Applies chosen framework. 
#     If framework_id is 'auto-select', it asks the AI to choose the best one first.
#     """
#     headers = {
#         "Authorization": f"Bearer {AIRIA_API_KEY}",
#         "Content-Type": "application/json"
#     }
    
#     system_prompt = f"You are a strategy and operations consultant. Apply the {framework_id} framework to analyze the following problem. Generate the solution in a structured markdown format."
    
#     if framework_id == "auto-select":
#         system_prompt = "You are a strategy and operations consultant. First, analyze the problem and identify the single best strategic framework to solve it. Explain your choice, then apply that framework to generate a structured Markdown format."

#     payload = {
#         "model": "designer-model-id",
#         "messages": [
#             {"role": "system", "content": system_prompt},
#             {"role": "user", "content": clean_problem}
#         ]
#     }
    
#     # Placeholder return for testing. In production, uncomment the httpx block below.
#     return f"# \n\n**Framework Used:** {framework_id}\n\n**Analysis of:** {clean_problem}\n\n(AI generated content would appear here)"

#     # async with httpx.AsyncClient() as client:
#     #     response = await client.post(f"{AIRIA_BASE_URL}/chat/completions", json=payload, headers=headers)
#     #     response.raise_for_status()
#     #     data = response.json()
#     #     return data['choices'][0]['message']['content']
