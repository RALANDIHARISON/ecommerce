release: sh -c "cd ecommerce && python manage.py migrate --noinput --settings=ecommerce.settings && python manage.py collectstatic --noinput --settings=ecommerce.settings"
web: sh -c "cd ecommerce && gunicorn ecommerce.wsgi --log-file - --bind 0.0.0.0:$PORT"
