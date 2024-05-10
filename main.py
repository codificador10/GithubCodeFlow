from fastapi import FastAPI
from firebase_admin import credentials, initialize_app
from middleware.auth import firebase_auth_middleware
from routes.functionsRoute import router as functionsRouter
from routes.parserRoute import router as parseRouter

# Create FastAPI instance
app = FastAPI()

# Initialize Firebase Admin SDK with service account credentials
cred = credentials.Certificate("/Users/ayushraj/auth.json")
initialize_app(cred)

# Attach the middleware to the application
app.middleware("http")(firebase_auth_middleware)

# Define root route
@app.get("/")
async def root():
    return {"message": "Hello, to the Project!"}

# Include routers
app.include_router(functionsRouter)
app.include_router(parseRouter)
