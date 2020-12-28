from django.shortcuts import render
from Route.models import Route
from Route.serializers import RouteSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from helper import convert_date
from Route.tasks import search_flight

import datetime


@api_view(['GET'])
def search(request):
    """
    API method of creating a Route object.
    This implicitly checks flights for given route.
    Parameters: fly_from, fly_to, date
    Without date, returns flights for all cached 
    dates for the given route.
    """
    if request.method == 'GET':
        fly_from = request.GET.get('fly_from', None)
        fly_to = request.GET.get('fly_to', None)
        date_from = request.GET.get('date', None)
        date_to = request.GET.get('date', None)

        if all(v is not None for v in [fly_from, fly_to, date_from, date_to]):
            try:
                route = Route.objects.all().filter(fly_from=fly_from,
                                                   fly_to=fly_to,
                                                   date_from=date_from,
                                                   date_to=date_to).first()
                if route is None:
                    route = Route(fly_from=fly_from,
                                  fly_to=fly_to,
                                  date_from=date_from,
                                  date_to=date_to)
                    route.save()
                if not route.response:
                    route.response = {'executing': 1}
                    route.save()
                    search_flight.delay(route.pk)
                serializer = RouteSerializer(route)
                return Response(serializer.data)
            except AssertionError:
                print('No flights found')
                return Response()
        elif all(v is not None for v in [fly_from, fly_to]):
            try:
                routes = Route.objects.all().filter(fly_from=fly_from,
                                                   fly_to=fly_to)
                serializer = RouteSerializer(routes)
                return Response(serializer.data)
            except AssertionError:
                print('No flights found')
                return Response()
    return Response()
