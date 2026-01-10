# Explanation Service - Dockerfile
# For Railway deployment with Root Directory = backend/explanation_service
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies (transformers and torch are large - be patient)
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY main.py .

# Expose port 8081 (Railway will map to $PORT)
EXPOSE 8081

# Run the FastAPI application
CMD ["python", "main.py"]
