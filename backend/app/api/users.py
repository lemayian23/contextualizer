from fastapi import APIRouter, Depends, HTTPException 
from sqlalchemy.orm import Session 
from app.core.database import get_db 
from app.models.database import User 
from app.core.security import get_password_hash, verify_password, create_access_token 
from pydantic import BaseModel 
 
router = APIRouter(prefix="/users", tags=["users"]) 
 
class UserCreate(BaseModel): 
    email: str 
    password: str 
    full_name: str 
 
class UserLogin(BaseModel): 
    email: str 
    password: str 
 
class Token(BaseModel): 
    access_token: str 
    token_type: str 
 
@router.post("/register") 
def register(user_data: UserCreate, db: Session = Depends(get_db)): 
    # Check if user already exists 
    existing_user = db.query(User).filter(User.email == user_data.email).first() 
    if existing_user: 
        raise HTTPException(status_code=400, detail="Email already registered") 
 
    # Create new user 
    hashed_password = get_password_hash(user_data.password) 
    user = User( 
        email=user_data.email, 
        hashed_password=hashed_password, 
        full_name=user_data.full_name 
    ) 
    db.add(user) 
    db.commit() 
    db.refresh(user) 
 
    return {"message": "User created successfully", "user_id": user.id} 
 
@router.post("/login") 
def login(login_data: UserLogin, db: Session = Depends(get_db)): 
    user = db.query(User).filter(User.email == login_data.email).first() 
    if not user or not verify_password(login_data.password, user.hashed_password): 
        raise HTTPException(status_code=401, detail="Invalid credentials") 
 
    access_token = create_access_token(subject=user.id) 
    return Token(access_token=access_token, token_type="bearer") 
