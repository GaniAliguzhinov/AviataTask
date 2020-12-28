# AviataTask

## Deploy

* `./init.sh`
* `export KIWI_API_KEY='API_SECRET'`
* `source venv/bin/activate`
* `./manage.py makemigrations`
* `./manage.py migrate`
* Uncomment the schedule
* `./manage.py migrate`
* `./manage.py createsuperuser`
* In one console: `./start_celery.sh`
* In another: `redis-server`
* In yet another: `./manage.py runserver`
* Now, run `python create_cal.py` to initialize route queries. Results can be viewed on `localhost:8000/routes/`

## View calendar

To view results, for example for ALA->MOW, use REST:

`localhost:8000/api/search?fly_from=ALA&fly_to=MOW`

To view whole calendar:

`localhost:8000/api/`
