from fastapi import FastAPI, Depends 
from fastapi.middleware.cors import CORSMiddleware 
from contextlib import asynccontextmanager 
from app.core.config import settings 
from app.core.database import engine 
from app.models.database import Base 
from app.api import meetings, users, search 
 
@asynccontextmanager 
async def lifespan(app: FastAPI): 
    # Create database tables 
    Base.metadata.create_all(bind=engine) 
    yield 
 
app = FastAPI( 
    title=settings.PROJECT_NAME, 
    description="Intelligent Meeting Note Taker & Knowledge Base", 
    version="1.0.0", 
    lifespan=lifespan 
) 
 
# CORS middleware 
app.add_middleware( 
    CORSMiddleware, 
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True, 
    allow_methods=["*"], 
    allow_headers=["*"], 
) 
 
# Include routers 
app.include_router(users.router, prefix=settings.API_V1_STR) 
app.include_router(meetings.router, prefix=settings.API_V1_STR) 
app.include_router(search.router, prefix=settings.API_V1_STR) 
 
@app.get("/") 
async def root(): 
    return {"message": "Contextualizer API", "version": "1.0.0"} 
 
@app.get("/health") 
async def health(): 
    return {"status": "healthy"} 
