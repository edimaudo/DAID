import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from agent import agent_framer #,

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

#@app.post("/api/frame_problem")
@app.post("/framer")
async def frame_problem(request: Request):
    data = await request.json()
    messy_input = data.get('messyInput', '')
    try:
        result = await agent_framer(messy_input)
        return {"framedProblem": result, "success": True}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e), "success": False})

# Solution Design
@app.get("/app", response_class=HTMLResponse)
async def main_app(request: Request):
    return templates.TemplateResponse("app.html", {"request": request})

@app.post("/app")
#@app.post("/api/generate_analysis")
async def generate_analysis(request: Request):
    data = await request.json()
    clean_problem = data.get('cleanProblem', '')
    framework_id = data.get('frameworkId', 'auto-select')
    try:
        result = await agent_solution_designer(clean_problem, framework_id)
        return {"analysisData": result, "success": True}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e), "success": False})

# Decision Information Page
@app.get("/decision-information", response_class=HTMLResponse)
async def decision_info(request: Request):
    return templates.TemplateResponse("decision_info.html", {"request": request})

# 404 Handler
@app.exception_handler(404)
async def custom_404_handler(request: Request, __):
    return templates.TemplateResponse("404.html", {"request": request}, status_code=404)



