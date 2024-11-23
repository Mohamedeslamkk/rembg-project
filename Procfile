release: python -m ensurepip && pip install -r requirements.txt
web: gunicorn app:app
web: gunicorn --bind 0.0.0.0:$PORT app:app
