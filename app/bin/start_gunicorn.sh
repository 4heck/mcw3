source /home/ru/projects/mcw3/venv/bin/activate
exec gunicorn -c "/home/ru/projects/mcw3/app/gunicorn_config.py" mcw_price_monitoring.wsgi
