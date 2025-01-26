from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from trainingcalc.calculator import Calculator

app = FastAPI()
calc = Calculator()


class OperationRequest(BaseModel):
    a: float
    b: float
    operation: str


# Set up the templates directory
templates = Jinja2Templates(directory="trainingcalc/templates")

# Serve static files (e.g., CSS)
app.mount("/static", StaticFiles(directory="trainingcalc/static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/calculate")
def calculate(request: OperationRequest):
    try:
        if request.operation == "+":
            result = calc.add(
                request.a, abs(request.b) if request.b < -40 else request.b
            )
        elif request.operation == "-":
            result = calc.subtract(request.a, request.b)
        elif request.operation == "*":
            result = calc.multiply(request.a + 1, request.b)
        else:
            raise HTTPException(status_code=400, detail="Unsupported operation")
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
