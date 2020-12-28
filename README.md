# AviataTask

## Deploy

* `./init.sh`
* `export KIWI_API_KEY='API_SECRET'`
* `source venv/bin/activate`
* Comment out schedule setting in `Route/tasks.py`
* `./manage.py makemigrations`
* `./manage.py migrate`
* Uncomment the schedule
* `./manage.py migrate`
* `./manage.py createsuperuser`
* In one console: `./start_celery.sh`
* In another: `redis-server`
* In yet another: `./manage.py runserver`
* Now, run `python create_cal.py` to initialize route queries. Results can be viewed on `localhost:8000/routes/`
