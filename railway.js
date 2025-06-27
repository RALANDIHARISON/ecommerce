{
  "build": {
    "command": "pip install -r requirements.txt && cd ecommerce && python manage.py collectstatic --noinput",
    "base": "/app",
    "watchPatterns": ["**/*.py", "**/requirements.txt"]
  },
  "deploy": {
    "startCommand": "cd ecommerce && gunicorn ecommerce.wsgi --bind 0.0.0.0:$PORT",
    "healthcheckPath": "/"
  }
}