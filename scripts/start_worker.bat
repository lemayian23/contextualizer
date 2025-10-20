@echo off 
echo Starting Celery Worker... 
cd ..\backend 
celery -A app.workers.celery_app worker --loglevel=info 
