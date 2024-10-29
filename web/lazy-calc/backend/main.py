from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os
import logging

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")

logging.basicConfig(
    filename="user_input.log",  # Log file name
    level=logging.INFO,          # Log level
    format="%(asctime)s - %(levelname)s - %(message)s"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Expression(BaseModel):
    expression: str

@app.post("/calculate")
async def calculate_expression(data: Expression):
    try:
        logging.info(f"User input: {data.expression}")
        if data.expression == "":
            raise Exception("Empty expression")
        if len(data.expression) > 12:
            raise Exception("Expression too long")
        # if data.expression == "os._exit(1)" or data.expression == "breakpoint()" or "kill" in data.expression:
        #if data.expression == "breakpoint()":
        #    raise Exception("Restricted Commands")
        print(type(data.expression))
        result = eval(data.expression)
        return {"result": result}
    except Exception as e:
        logging.error(f"Error processing expression '{data.expression}': {e}")
        raise HTTPException(status_code=400, detail=f"{e}")

@app.get("/", response_class=HTMLResponse)
async def serve_index():
    with open("static/index.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)
