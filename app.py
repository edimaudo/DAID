import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# TODO: Create agents.py with these new Airia.ai agent functions
# from agents import agent_framer, agent_solution_designer 

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Landing Page
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# The Framer
@app.get("/framer", response_class=HTMLResponse)
async def framer_page(request: Request):
    return templates.TemplateResponse("framer.html", {"request": request})

# Solution Designer / Framework Selector
@app.get("/app", response_class=HTMLResponse)
async def main_app(request: Request):
    return templates.TemplateResponse("app.html", {"request": request})

# Decision Information Page
@app.get("/decision-information", response_class=HTMLResponse)
async def decision_info(request: Request):
    return templates.TemplateResponse("decision_info.html", {"request": request})


# # API Step 1: Process Messy Input
# @app.post("/api/frame_problem")
# async def frame_problem(request: Request):
#     data = await request.json()
#     messy_input = data.get('messyInput', '')
    
#     try:
#         # result = await agent_framer(messy_input) # Call Airia Agent 1
        
#         # MOCK RESPONSE FOR TESTING FRONTEND
#         result = "Based on your input, the root cause appears to be an operational bottleneck in Q3 rather than a sales team failure. Is this the problem we should solve?"
        
#         return {"framedProblem": result, "success": True}
#     except Exception as e:
#         return JSONResponse(status_code=500, content={"error": str(e), "success": False})

# # API Step 2: Generate Final Framework Analysis
# @app.post("/api/design_solution")
# async def design_solution(request: Request):
#     data = await request.json()
#     clean_problem = data.get('cleanProblem', '')
#     framework_id = data.get('frameworkId', '')
    
#     try:
#         # result = await agent_solution_designer(clean_problem, framework_id) # Call Airia Agent 2
        
#         # MOCK RESPONSE FOR TESTING FRONTEND
#         result = f"Strategic Memo generated using {framework_id} for the problem: {clean_problem[:30]}..."
        
#         return {"analysisData": result, "success": True}
#     except Exception as e:
#         return JSONResponse(status_code=500, content={"error": str(e), "success": False})

# Custom 404 Handler
@app.exception_handler(404)
async def custom_404_handler(request: Request, __):
    return templates.TemplateResponse("404.html", {"request": request}, status_code=404)
