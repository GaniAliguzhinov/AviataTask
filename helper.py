import datetime
import time
from django.conf import settings
import requests
from requests.exceptions import ConnectionError, Timeout


def convert_date(date):
    """
    Converts date from 10/01/2020 to 2020-01-10
    """
    return datetime.datetime.strptime(date, "%d/%m/%Y").strftime("%Y-%m-%d")


def check_flights(booking_token, bnum=1, pnum=1):
    """
    Check a flight for pnum passangers and bnum baggages
    """
    base_url = 'https://tequila-api.kiwi.com/v2/booking/'
    url = f"{base_url}check_flights?apikey={settings.KIWI_API_KEY}"
    url = f"{url}&booking_token={booking_token}"
    url = f"{url}&bnum={bnum}&pnum={pnum}"

    try:
        response_json = requests.get(url, timeout=5, stream=True).json()
    except ConnectionError:
        print('ConnectionError')
        return None
    except Timeout:
        print('Timeout')
        return None
    else:
        assert response_json is not None
        return response_json


def is_valid(response, booking_token):
    if response['flights_invalid']:
        return False
    num_tries = 1
    while not response['flights_checked']:
        time.sleep(2)
        response = check_flights(booking_token)
        num_tries += 1
        if num_tries >= 5:
            return False
    return True


def check_and_sort(flights):
    """
    Sort flights by price. Try to book the first flight.
    Discard invalid flights.
    """
    flights.sort(key=lambda k: k['conversion'].get('EUR', 0), reverse=False)
    flight = next(iter(flights), None)
    try:
        check_response = check_flights(flight['booking_token'])

        if not is_valid(check_response, flight['booking_token']):
            return check_and_sort(flights[1:])

        if check_response['price_change'] and \
                check_response['price'] != flight['conversion'].get('EUR', 0):
            rate = flight['conversion']['KZT']/flight['conversion']['EUR']
            flights[0]['conversion']['EUR'] = check_response['price']
            flights[0]['conversion']['KZT'] = check_response['price']*rate
            flights[0]['price'] = check_response['price']*rate
            return check_and_sort(flights)
    except Exception:
        return check_and_sort(flights[1:])
    return flights


def search(fly_from, fly_to, date_from, date_to):
    """
    Search for a flight.
    """
    base_url = 'https://tequila-api.kiwi.com/v2/'
    url = f"{base_url}search?apikey={settings.KIWI_API_KEY}"
    url = f"{url}&fly_from={fly_from}&fly_to={fly_to}"
    url = f"{url}&date_from={date_from}&date_to={date_to}"
    url = f"{url}&adults=1&curr=KZT"

    try:
        response = requests.get(url, timeout=5, stream=True).json()['data']
    except ConnectionError:
        print('ConnectionError')
        return None
    except Timeout:
        print('Timeout')
        return None
    except KeyError:
        print('Incorrect kiwi response')
        return None
    else:
        flights = response
        flights = check_and_sort(flights)
        response = next(iter(flights), None)
        assert response is not None
        return response
