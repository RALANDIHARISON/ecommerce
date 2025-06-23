release: cd ecommerce && python manage.py migrate && python manage.py collectstatic --noinput
web: gunicorn ecommerce.wsgi --chdir ecommerce
