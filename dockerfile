FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

# Collect static files
#RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--workers=3", "--bind", "0.0.0.0:8000", "fruitmart.wsgi:application"]