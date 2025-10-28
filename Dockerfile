# Build stage
FROM python:3.11-slim as builder

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Runtime stage
FROM python:3.11-slim

WORKDIR /app

# Install curl for healthcheck
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Copy Python dependencies from builder
COPY --from=builder /root/.local /root/.local

# Copy application code
COPY app.py .
COPY templates/ templates/

# Make sure scripts in .local are usable
ENV PATH=/root/.local/bin:$PATH

# Expose port
EXPOSE 5000

# Run with gunicorn for production (single worker to avoid connection pool issues)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "1", "--timeout", "120", "app:app"]

