from django.shortcuts import render

from django.conf import settings

from projects.models import Post


def home(request):

    # Obtém os posts ordenados pelos mais recentes
    # Filtrados por 'is_activate' e 'is_deleted'
    posts = Post.objects.filter(
        is_active=True
    ).order_by('-created_at')

    # Total de regitros
    total = len(posts)

    return render(
        request,
        'projects/_.html',
        {
            'tag_title': f'{settings.SITENAME}',
            'posts': posts,
            'total': total
        }
    )
