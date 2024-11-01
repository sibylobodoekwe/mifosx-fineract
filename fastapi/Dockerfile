# Dockerfile for FastAPI service
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /app

COPY ./app /app

# Install required packages
RUN pip install fastapi[all] requests

# Expose the FastAPI service
EXPOSE 8000

# Start the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]