from django.shortcuts import render

from django.conf import settings


def home(request):

    context = { 'tag_tittle': f'{settings.SITENAME}' }
    
    return render(
        request,
        'projects/home.html',
        context
    )
