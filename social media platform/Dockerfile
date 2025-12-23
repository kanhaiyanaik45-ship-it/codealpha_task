FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app

# Install system deps
RUN apt-get update && apt-get install -y build-essential gcc libpq-dev --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY backend/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy project
COPY . /app
WORKDIR /app/backend

# Expose port
EXPOSE 8000

# Run migrations and start server (dev)
CMD ["gunicorn", "social_platform.wsgi:application", "--bind", "0.0.0.0:8000"]
