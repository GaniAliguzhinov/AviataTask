from __future__ import absolute_import, unicode_literals
from django_celery_beat.models import PeriodicTask, CrontabSchedule
from Calendar.celery import app
from Route.models import Route
from helper import search
from helper import increment_date
from Calendar.settings import TIME_ZONE


@app.task(name="search_flight")
def search_flight(pk):
    print('Doing task')
    query = Route.objects.get(pk=pk)
    fly_from, fly_to = query.fly_from, query.fly_to
    date_from, date_to = query.date_from, query.date_to
    print(f'from={fly_from}, to={fly_to}, date={date_from}')
    response = search(fly_from, fly_to, date_from, date_to)
    if response:
        query.response = response
    else:
        query.response = {"nodata": 1}
    print('Saving result')
    query.save()


@app.task(name="update_all_routes")
def update_all_routes():
    for route in Route.objects.all():
        print('Doing update task')
        date_from, date_to = route.date_from, route.date_to

        route.date_from = increment_date(date_from)
        route.date_to = increment_date(date_to)

        print(f'Date: {date_from}, {date_to}')
        route.save()
        search_flight.delay(route.pk)


# at_0_am, _ = CrontabSchedule.objects.get_or_create(
#     minute="0", hour="0", day_of_week="*", day_of_month="*", month_of_year="*",
#     timezone=TIME_ZONE,
# )
# PeriodicTask.objects.update_or_create(
#     task="update_all_routes",
#     defaults=dict(
#         crontab=at_0_am,
#         expire_seconds=7200,
#     )
# )
