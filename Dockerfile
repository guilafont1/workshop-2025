FROM python:3.11-slim

# Do not write .pyc files and make stdout/stderr unbuffered
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install pip dependencies. Copy only requirements first to leverage Docker layer caching.
COPY requirements.txt /app/requirements.txt

RUN apt-get update \
    && apt-get install -y --no-install-recommends ca-certificates \
    && rm -rf /var/lib/apt/lists/* \
    && python -m pip install --upgrade pip setuptools wheel \
    && pip install --no-cache-dir -r /app/requirements.txt

# Copy application code
COPY . /app

# Expose the Flask default port
EXPOSE 5000

# Use the Flask CLI which will import `app` from app.py. Bind to 0.0.0.0 so the
# container is accessible from outside.
ENV FLASK_APP=app.py

# In development you might keep debug on; for production consider using gunicorn.
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
