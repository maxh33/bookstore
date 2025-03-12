release: python manage.py migrate --noinput
web: gunicorn bookstore.wsgi:application --log-file - 
