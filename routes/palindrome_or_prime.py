from fastapi import APIRouter
from pydantic import BaseModel
from math import isqrt
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


@router.post("/check-prime")
def check_prime(number: Numbers):
    n = number.num
    if n < 2:
        return JSONResponse(
            status_code=200,
            content={"number": n, "is_prime": False}
        )

    if n == 2:
        return JSONResponse(
            status_code=200,
            content={"number": n, "is_prime": True}
        )

    if n % 2 == 0:
        return JSONResponse(
            status_code=200,
            content={"number": n, "is_prime": False}
        )

    for i in range(3, isqrt(n) + 1, 2):
        if n % i == 0:
            return JSONResponse(
                status_code=200,
                content={"number": n, "is_prime": False}
            )

    return JSONResponse(
        status_code=200,
        content={"number": n, "is_prime": True}
    )