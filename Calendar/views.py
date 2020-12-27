from django.shortcuts import render, redirect


def home(request):
    """
    Home view
    """
    return render(request, 'home.html')
