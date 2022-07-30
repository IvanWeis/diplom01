from django.views.static import serve as mediaserve
from django.conf.urls import url

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

else:
    urlpatterns += [
        url(f'^{settings.MEDIA_URL.lstrip("/")}(?P<path>.*)$',
        mediaserve, {'document_root':settings.MEDIA_ROOT}),
        url(f'^{settings.STATIC_URL.lstrip("/")}(?P<path>.*)$',
        mediaserve, {'document_root':settings.STATIC_ROOT}),
    ]