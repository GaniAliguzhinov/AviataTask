import datetime
import requests
from requests.exceptions import ConnectionError, Timeout


def query(fly_from, fly_to, date):
    """
    Search for a flight.
    """
    base_url = 'http://127.0.0.1:8000/api/'
    url = f"{base_url}search?"
    url = f"{url}&fly_from={fly_from}&fly_to={fly_to}"
    url = f"{url}&date={date}"

    try:
        requests.get(url, timeout=5, stream=True)
    except ConnectionError:
        print('ConnectionError')
    except Timeout:
        print('Timeout')
    except KeyError:
        print('Incorrect kiwi response')


routes = [('ALA', 'TSE'), ('TSE', 'ALA'),
          ('ALA', 'MOW'), ('MOW', 'ALA'),
          ('ALA', 'CIT'), ('CIT', 'ALA'),
          ('TSE', 'MOW'), ('MOW', 'TSE'),
          ('TSE', 'LED'), ('LED', 'TSE')]
date_start = datetime.datetime.date(datetime.datetime.now())

dates = []
for i in range(32):
    date = date_start
    date += datetime.timedelta(days=i)
    dates.append(date.strftime('%d/%m/%Y'))

def foo(f1, f2, d1):
    print(f'from = {f1}, to = {f2}, d = {d1}')


for date in dates:
    for route in routes:
        query(route[0], route[1], date)
