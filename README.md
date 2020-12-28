# AviataTask

## Deploy

* `./init.sh`
* `export KIWI_API_KEY='API_SECRET'`
* `source venv/bin/activate`
* `./manage.py makemigrations`
* `./manage.py migrate`
* Uncomment the schedule at `Route/tasks.py`
* `./manage.py migrate`
* `./manage.py createsuperuser`
* In one console: `./start_celery.sh`
* In another: `redis-server`
* In yet another: `./manage.py runserver`
* Now, run `python create_cal.py` to initialize route queries. Results can be viewed on `localhost:8000/routes/`

P.S. Right now, every query made with the search API is saved and update each day. Better solution would be 
to have a config file with set routes and dates that need to be included in update.

## View calendar

To view results, for example for ALA->MOW, use REST:

`localhost:8000/api/search?fly_from=ALA&fly_to=MOW`

To view whole calendar:

`localhost:8000/api/`
