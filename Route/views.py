from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Route


class RouteListView(ListView):
    model = Route
