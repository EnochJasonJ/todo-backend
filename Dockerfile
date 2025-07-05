# Use Python 3.10
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install OS packages for psycopg2
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port (Render uses PORT env var)
EXPOSE 8000

# Start the server
CMD gunicorn project.wsgi:application --bind 0.0.0.0:$PORT
