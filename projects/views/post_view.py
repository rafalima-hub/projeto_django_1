
from django.shortcuts import get_object_or_404, render

from projects.models import Post


def post_view(request, id):

    # Obtém o post solicitado pelo id
    post = get_object_or_404(Post, id=id)

    # Trata nomde do autor
    if post.user.first_name and post.user.last_name:
        author_name = f'{post.user.first_name} {post.user.last_name}'
    elif post.user.first_name:
        author_name = post.user.first_name
    else:
        author_name = post.user.username

    # Obtém os posts do mesmo autor aleatóriamente
    posts = Post.objects.filter(
        user=post.user,
        is_activate=True,
        is_deleted=False
    ) .exclude(
        # Excluindo o post atual
        id=post.id
    ).order_by('?')[:3]  # Fatia somente 3 posts

    return render(
        request,
        'projects/post_view.html',
        {
        'post': post,  # Post orginal
        'posts': posts,  # Posts do autor
        'author_name': author_name,  # Nome do autor do post
        }
    )
