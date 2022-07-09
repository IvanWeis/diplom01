from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from coolsite import settings
from women.views import * # чтобы не красное верхний coolsite Mark Sources Root

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('women.urls')), # направляем на women.urls приложения
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
