# main.py
from fastapi import FastAPI
from routes.users import router as users_router
from routes.math_operations import router as math_operations_router

app = FastAPI()

# Include the routes
app.include_router(users_router)
app.include_router(math_operations_router)
# this is a demo app
