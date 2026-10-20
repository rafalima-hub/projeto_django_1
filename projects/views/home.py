from django.shortcuts import render

from django.conf import settings

from projects.models import Post


def home(request):

    posts = Post.objects.filter(
        is_active=True
    ).order_by('-created_at')

    contexto = {
        'tag_title': f'{settings.SITENAME}',
        'posts' : posts
    }
    return render(
        request, 
        'projects/home.html',
        contexto
    )
