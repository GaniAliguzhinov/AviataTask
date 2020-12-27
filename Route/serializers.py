from rest_framework import serializers
from Route.models import Route


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ['fly_from', 'fly_to', 'date_from', 'date_to', 'response']
