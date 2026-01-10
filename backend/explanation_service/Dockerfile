# Explanation Service - Dockerfile
# For Railway deployment with Root Directory = backend/explanation_service
# Optimized: Removed transformers/torch to reduce image size (<200MB)
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies (lightweight - just FastAPI and uvicorn)
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY main.py .

# Expose port (Railway will set $PORT)
EXPOSE 8081

# Run the FastAPI application
CMD ["python", "main.py"]
