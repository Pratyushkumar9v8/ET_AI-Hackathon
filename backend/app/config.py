import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "SentinelAI"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "SENTINEL_AI_SUPER_SECRET_KEY_CNI_SECURITY_2026_PRODUCTION"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24 hours
    
    # Database
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL", 
        "postgresql+asyncpg://sentinel:sentinel_secret@localhost:5432/sentinel_db"
    )
    SYNC_DATABASE_URL: str = os.getenv(
        "SYNC_DATABASE_URL", 
        "postgresql://sentinel:sentinel_secret@localhost:5432/sentinel_db"
    )
    
    # Redis
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    
    # OpenAI / Gemini AI Key
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "demo-mock-key")
    
    # CORS
    BACKEND_CORS_ORIGINS: list[str] = ["http://localhost:3000", "http://127.0.0.1:3000"]

    class Config:
        case_sensitive = True

settings = Settings()
