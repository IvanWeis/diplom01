from django.urls import path
from women.views import * # чтобы не красное верхний coolsite Mark Sources Root

urlpatterns = [   # здесь прописываем все маршруты текущего приложения
    path('', index),  # http://127.0.0.1:8000/ - направляем на функцию index
    path('cats/<int:catid>/', categories), # http://127.0.0.1:8000/cats/2/ на categories
]
