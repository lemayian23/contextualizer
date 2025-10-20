# Add these imports to the existing main.py file 
from app.api import meetings, users, search 
 
# Add this after the CORS middleware in main.py 
# Include routers 
app.include_router(users.router, prefix=settings.API_V1_STR) 
app.include_router(meetings.router, prefix=settings.API_V1_STR) 
app.include_router(search.router, prefix=settings.API_V1_STR) 
