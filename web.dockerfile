FROM tiangolo/uvicorn-gunicorn:python3.8-slim

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

# Mounted in docker-compose.yml
# COPY ./app /app
