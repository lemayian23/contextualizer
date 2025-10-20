from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text, Boolean, Float, JSON 
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker 
from datetime import datetime 
from app.core.config import settings 
 
engine = create_engine(settings.DATABASE_URL) 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 
Base = declarative_base() 
 
class User(Base): 
    __tablename__ = "users" 
 
    id = Column(Integer, primary_key=True, index=True) 
    email = Column(String, unique=True, index=True) 
    hashed_password = Column(String) 
    full_name = Column(String) 
    is_active = Column(Boolean, default=True) 
    created_at = Column(DateTime, default=datetime.utcnow) 
 
class Meeting(Base): 
    __tablename__ = "meetings" 
 
    id = Column(Integer, primary_key=True, index=True) 
    title = Column(String, index=True) 
    audio_file_path = Column(String) 
    user_id = Column(Integer, index=True) 
    status = Column(String, default="pending") 
    created_at = Column(DateTime, default=datetime.utcnow) 
    processed_at = Column(DateTime, nullable=True) 
 
    # Processing results 
    transcript = Column(Text, nullable=True) 
    summary = Column(Text, nullable=True) 
    action_items = Column(JSON, nullable=True) 
 
    # Cost tracking 
    processing_cost = Column(Float, default=0.0) 
    processing_duration = Column(Float, nullable=True) 
