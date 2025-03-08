# Use Python 3.12 slim image as base
FROM python:3.12-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    # prevents python creating .pyc files
    PYTHONDONTWRITEBYTECODE=1 \
    \
    # pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

# Install system dependencies
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        # deps for building python deps
        build-essential \
        # postgres dependencies
        libpq-dev 

# Set working directory
WORKDIR /app

# Copy requirements files
COPY requirements.txt /app/

# Install project dependencies
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy application code
COPY . /app/

# Run collectstatic for Django
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Run the application with gunicorn for production
CMD gunicorn bookstore.wsgi:application --bind 0.0.0.0:$PORT


