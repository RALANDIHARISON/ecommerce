{
  "build": {
    "command": "pip install -r requirements.txt && python manage.py collectstatic --noinput",
    "base": "/app/ecommerce"
  },
  "deploy": {
    "startCommand": "gunicorn ecommerce.wsgi"
  }
}