python manage.py collectstatic --no-input

gunicorn Ticketta.wsgi:application --bind 0.0.0.0:"$PORT"
