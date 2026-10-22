from django.conf import settings


def global_centext(request):
    return{
        'site_name': settings.SITENAME,
    }