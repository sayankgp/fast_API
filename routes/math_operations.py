# routes/math_operations.py
from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import JSONResponse

# Pydantic model for numbers
class Numbers(BaseModel):
    num1: int
    num2: int

# Create a router
router = APIRouter()

@router.post("/sum")
def summerize(num: Numbers):
    result = num.num1 + num.num2
    return JSONResponse(status_code=200, content={"sum": result})

@router.post("/subtract")
def subtract(num: Numbers):
    result = num.num1 - num.num2
    return JSONResponse(status_code=200, content={"operation": "subtract", "result": result})

@router.post("/multiply")
def multiply(num: Numbers):
    result = num.num1 * num.num2
    return JSONResponse(status_code=200, content={"operation": "multiply", "result": result})

@router.post("/divide")
def divide(num: Numbers):
    if num.num2 == 0:
        return JSONResponse(status_code=400, content={"error": "Division by zero is not allowed"})
    result = num.num1 / num.num2
    return JSONResponse(status_code=200, content={"operation": "divide", "result": result})
