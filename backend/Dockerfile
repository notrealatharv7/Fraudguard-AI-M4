# Fraud Detection API - Dockerfile
# For Railway deployment with Root Directory = backend
# This Dockerfile assumes Railway root directory is set to backend/

FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy ML model directory (relative to backend/)
COPY ml/ ./ml/

# Copy application code
COPY main.py .

# Expose port 8000
EXPOSE 8000

# Run the FastAPI application
CMD ["python", "main.py"]
