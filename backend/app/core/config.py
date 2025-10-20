from pydantic_settings import BaseSettings 
from typing import Optional 
 
class Settings(BaseSettings): 
    DATABASE_URL: str = "postgresql://postgres:password@localhost:5433/contextualizer" 
    REDIS_URL: str = "redis://localhost:6380/0" 
    SECRET_KEY: str = "test-secret-key-change-in-production" 
    OPENAI_API_KEY: Optional[str] = None 
 
settings = Settings() 
