# routes/users.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

# Simulated mock database of users
users_db = [
    {"id": 1, "name": "Alice", "age": 30, "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "age": 25, "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "age": 35, "email": "charlie@example.com"},
]

# Pydantic model to represent the user structure
class User(BaseModel):
    id: int
    name: str
    age: int
    email: str

# Create a router
router = APIRouter()

@router.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    user = next((user for user in users_db if user["id"] == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user["email"]

@router.get("/users", response_model=List[User])
def get_users():
    return users_db
