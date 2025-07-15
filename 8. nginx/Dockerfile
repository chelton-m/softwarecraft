FROM python:3.11

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    postgresql-client \
    gettext \
    python3-distutils \
    python3-dev

COPY . /app

# Install pip and setuptools first
RUN pip install --upgrade pip setuptools wheel

# Install requirements
RUN pip install --no-cache-dir -r requirements.txt

# Install gunicorn explicitly
RUN pip install --no-cache-dir gunicorn

# Add the project directory to PYTHONPATH
ENV PYTHONPATH=/app

RUN python manage.py collectstatic --noinput

EXPOSE 8000

# Use gunicorn with proper settings and correct path
CMD ["gunicorn", "--chdir", "/app", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "4", "--timeout", "120"]
