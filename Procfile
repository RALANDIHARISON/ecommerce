web: gunicorn ecommerce.wsgi --chdir ecommerce --log-file -
release: sh -c "cd ecommerce && python manage.py migrate"


