{
  "build": {
    "command": "pip install -r requirements.txt",
    "base": "/app/ecommerce"
  },
  "deploy": {
    "startCommand": "gunicorn ecommerce.wsgi --bind 0.0.0.0:$PORT"
  }
}