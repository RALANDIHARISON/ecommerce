release: python ecommerce/manage.py migrate --no-input && python ecommerce/manage.py collectstatic --no-input
web: gunicorn ecommerce.wsgi:application --chdir ecommerce --bind 0.0.0.0:$PORT
