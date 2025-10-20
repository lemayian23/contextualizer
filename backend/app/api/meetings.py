from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form 
from sqlalchemy.orm import Session 
from typing import Optional 
import os 
import uuid 
from app.core.database import get_db 
from app.models.database import Meeting, ProcessingLog 
from app.workers.tasks import process_meeting 
 
router = APIRouter(prefix="/meetings", tags=["meetings"]) 
 
UPLOAD_DIR = "uploads" 
os.makedirs(UPLOAD_DIR, exist_ok=True) 
 
@router.post("/upload") 
async def upload_meeting( 
    title: str = Form(...), 
    audio_file: UploadFile = File(...), 
    db: Session = Depends(get_db) 
): 
    # Validate file type 
    if not audio_file.filename.endswith('.mp3'): 
        raise HTTPException(status_code=400, detail="Only MP3 files are supported") 
 
    # Generate unique filename 
    file_extension = audio_file.filename.split('.')[-1] 
    filename = f"{uuid.uuid4()}.{file_extension}" 
    file_path = os.path.join(UPLOAD_DIR, filename) 
 
    # Save file 
    with open(file_path, "wb") as f: 
        content = await audio_file.read() 
        f.write(content) 
 
    # Create meeting record 
    meeting = Meeting( 
        title=title, 
        audio_file_path=file_path, 
        user_id=1,  # TODO: Get from authenticated user 
        status="pending" 
    ) 
    db.add(meeting) 
    db.commit() 
    db.refresh(meeting) 
 
    # Start async processing 
    process_meeting.delay(meeting.id) 
 
    return { 
        "message": "Meeting uploaded successfully",  
        "meeting_id": meeting.id, 
        "status": meeting.status 
    } 
 
@router.get("/{meeting_id}") 
def get_meeting(meeting_id: int, db: Session = Depends(get_db)): 
    meeting = db.query(Meeting).filter(Meeting.id == meeting_id).first() 
    if not meeting: 
        raise HTTPException(status_code=404, detail="Meeting not found") 
 
    return meeting 
