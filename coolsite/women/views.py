from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail   # для отправки почты
from .forms import *  # из файла forms.py импортируем ВСЕ формы
from .models import *   # из файла models.py импортируем ВСЕ модели

def index(request):
    return render(request, 'women/index.html')

def category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id) # в переменную posts отфильтрованные записи таблицы Women
    cats = Category.objects.all() # в переменную posts ВСЕ записи таблицы Category
    return render(request, 'women/category.html', {'cats': cats, 'posts': posts})

def post(request, post_id):
    post = get_object_or_404(Women, pk=post_id) # в переменную post выбранную запись таблицы Women
    return render(request, 'women/post.html', {'post': post})

def addpage(request): # добавление Товара
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect ('home') # если все хорошо, уходим на Главную
    else:
        form = AddPostForm
    return render(request, 'women/addpage.html', {'form': form})

def order(request):
    if request.method == 'POST':
        form = AddOrder(request.POST)
        if form.is_valid():
             name = form.cleaned_data["name"]
             email = form.cleaned_data["email"]
             message = form.cleaned_data["message"]
             # отправка E_mail
             # send_mail(
             #    'Contact message',
             #     f'Ваше сообщение {message} принято',
             #     [weis.i@mail.ru],
             #     fail_silently=True,
             # )
             return HttpResponseRedirect('/') # возврат на Главную
        else:    # возвращаемся к правильному заполнению формы
            return render(request, 'women/order.html', context={"form": form})
    else:
        form = AddOrder()
    return render(request, 'women/order.html', context={"form": form}) # рендерим order.html

class UserLoginView(LoginView): # наследуемся от класса аутентификации LoginView
    template_name = 'women/login.html'
