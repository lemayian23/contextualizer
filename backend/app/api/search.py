from fastapi import APIRouter, Depends, HTTPException 
from sqlalchemy.orm import Session 
from app.core.database import get_db 
from app.models.database import Meeting 
from pydantic import BaseModel 
 
router = APIRouter(prefix="/search", tags=["search"]) 
 
class SearchQuery(BaseModel): 
    query: str 
 
@router.post("/") 
def search_meetings(search_query: SearchQuery, db: Session = Depends(get_db)): 
    # Simple keyword search for MVP 
    query = f"%{search_query.query}%" 
    meetings = db.query(Meeting).filter( 
        (Meeting.summary.ilike(query)) 
    ).all() 
 
    return { 
        "query": search_query.query, 
        "results": meetings, 
        "count": len(meetings) 
    } 
