release: python manage.py migrate --no-input && python manage.py collectstatic --no-input
web: gunicorn ecommerce.wsgi:application --chdir ecommerce --bind 0.0.0.0:$PORT
