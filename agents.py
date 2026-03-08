import os
import httpx
import json
from fastapi import HTTPException

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
                    f"### Revised Problem Statement\n{reframed_problem}\n\n"
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


async def agent_solution_designer(problem: str, framework_id: str):
    """Applies chosen framework. If framework_id is 'auto-select', it asks the AI to choose the best one first."""
    if not AIRIA_KEY or not AIRIA_AGENT_ID_SOLUTION:
        raise HTTPException(
            status_code=500,
            detail="Airia configuration (API Key or Solution Agent ID) is missing",
        )
    headers = {"X-API-Key": AIRIA_KEY, "Content-Type": "application/json"}

    user_input = " given " + problem + " apply " + framework_id + " framework to the problem and genrate the solution in a structured markdown format"
    if framework_id == 'auto-select':
        user_input = " given " + problem + " analyze the problem and identify the single best strategic/business/operations framework to solve it. Explain your choice, then apply that framework to generate a structured Markdown format."
   # Solution Design Payload structure
    payload = {
        "agent_id": AIRIA_AGENT_ID_SOLUTION,
        "UserInput": user_input,
        "UserId": AIRIA_USER_ID, 
    }
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                AIRIA_AGENT_URL_SOLUTION, json=payload, headers=headers, timeout=60.0
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
                framework_used = answer.get("framework_used", "")
                solution = answer.get("solution", "")
                recommended_next_steps = answer.get("recommended_next_steps", "")


                answer = (
                    f"### Problem Statement\n{problem}\n\n"
                    f"### Revised Problem Statement\n{reframed_problem}\n\n"
                    f"### Solution\n{solution}\n\n"
                    f"### Framework used\n{framework_used}\n\n"
                    f"### Reasoning\n{reasoning}\n\n"
                    f"### Next Steps\n{recommended_next_steps}\n\n"
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
