from django.shortcuts import render
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response


def home(request):
    """
    Home view
    """
    return render(request, 'home.html')


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []
