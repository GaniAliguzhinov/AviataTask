from django.db import models
from django.conf import settings


class Route(models.Model):
    """
    Container for a single route. Ex: ALA-CIT
    Stores Route properties (from, to), as well as
    last query results.
    """
    fly_from = models.TextField(max_length=250)
    fly_to = models.TextField(max_length=250)

    date_from = models.TextField()
    date_to = models.TextField()
    response = models.JSONField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            self.fly_from = kwargs['fly_from']
            self.fly_to = kwargs['fly_to']
            self.date_from = kwargs['date_from']
            self.date_to = kwargs['date_to']
        except KeyError:
            super().__init__(*args, **kwargs)
            return

        self.response = {}

    def __str__(self):
        if 'price' in self.response.keys():
            result = f"{self.fly_from} -\
            {self.fly_to}: {self.response['price']} KZT.\
            {self.response['departure_date']}"
        else:
            result = f"{self.fly_from} -\
            {self.fly_to}: {self.response}"
        return result
