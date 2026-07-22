from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.api.v1.router import api_router
from app.api.websockets.stream import router as ws_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup tasks (initialize tables, models, vector store)
    print("🚀 SentinelAI Core Backend Engine initialized.")
    yield
    print("🛑 SentinelAI Core Backend Engine shut down.")

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Autonomous Cyber Resilience Platform for Critical National Infrastructure (CNI)",
    version="1.0.0",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API Routers
app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(ws_router)

@app.get("/health")
async def health_check():
    return {"status": "HEALTHY", "system": "SentinelAI Engine", "mode": "Agentic AI Mesh Operational"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
