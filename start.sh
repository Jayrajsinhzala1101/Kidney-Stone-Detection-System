#!/usr/bin/env bash
# Start FastAPI and Django together

# Start FastAPI model service in the background on port 8001
uvicorn models.api:app --host 0.0.0.0 --port 8001 --workers 1 &

# Start Django app in the foreground on the port Render provides
gunicorn kidney_stone_detection.wsgi:application --bind 0.0.0.0:$PORT
