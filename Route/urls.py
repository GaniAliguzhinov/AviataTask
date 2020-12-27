from django.urls import path
from . import views


urlpatterns = [
    path('', views.RouteListView.as_view(), name='list'),
]
