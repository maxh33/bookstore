FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --require-hashes -r requirements.txt

COPY . .

# SECRET_KEY descartavel: so para o collectstatic em build; o real vem do ambiente em runtime
RUN SECRET_KEY=collectstatic-only python manage.py collectstatic --noinput \
    && useradd --system --uid 10001 app

USER app
EXPOSE 8000

CMD ["gunicorn", "bookstore.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "2", "--timeout", "30", "--access-logfile", "-"]
