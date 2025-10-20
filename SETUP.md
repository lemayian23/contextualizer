# Contextualizer - Setup Instructions 
 
## Prerequisites 
- Docker Desktop installed and running 
- Python 3.11+ installed 
 
## Quick Start 
 
1. **Start Infrastructure** 
```bash 
docker-compose -f infra/docker-compose.yml up -d 
``` 
 
2. **Install Python Dependencies** 
```bash 
cd backend 
pip install -r requirements.txt 
cd ../frontend 
pip install -r requirements.txt 
``` 
 
3. **Start the Application** 
   - Backend API: Run `scripts\start_backend.bat` 
   - Celery Worker: Run `scripts\start_worker.bat` 
   - Frontend: Run `scripts\start_frontend.bat` 
 
4. **Access the Application** 
   - Frontend: http://localhost:8501 
   - Backend API: http://localhost:8000 
   - API Documentation: http://localhost:8000/docs 
 
## Testing the API 
 
Use the FastAPI docs at http://localhost:8000/docs to test the endpoints: 
- Register a user at `/api/v1/users/register` 
- Login at `/api/v1/users/login` 
- Upload a meeting at `/api/v1/meetings/upload` 
- Search meetings at `/api/v1/search/` 
