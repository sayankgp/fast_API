from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import JSONResponse

class Numbers(BaseModel):
    num: int

# Create a router
router = APIRouter()

@router.post("/check-palindrome")
def check_palindrome(number: Numbers):
    str_num = str(number.num)
    is_palindrome = str_num == str_num[::-1]
    return JSONResponse(
        status_code=200,
        content={"number": number.num, "is_palindrome": is_palindrome}
    )