from django.urls import path, re_path

from women import views
from women.views import * # чтобы не красное верхний coolsite Mark Sources Root

urlpatterns = [   # здесь прописываем все маршруты текущего приложения
    path('', index, name='home'),# http://127.0.0.1:8000/ - направляем на функцию index
    path('addpage/', addpage, name='addpage'), #  - направляем на функцию about
    path('order/', order, name='order'),  #  - направляем на функцию contact
    path('post/<int:post_id>/', post, name="post"), # - направляем на post
    path('category/<int:cat_id>/', category, name="category"), # - направляем на category
    path('login/', views.UserLoginView.as_view(), name="login"), # - направляем на login
]
