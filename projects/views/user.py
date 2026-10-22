
from django.shortcuts import render


def login(request):
    return render(
        request,
        'projects/home.html'
    )

def logout(request):
    return render(
        request,
        'projects/home.html'
    )

def profile(request):
    return render(
        request,
        'projects/home.html'
    )
