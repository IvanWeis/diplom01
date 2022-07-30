from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail   # для отправки почты
from .forms import *  # из файла forms.py импортируем ВСЕ формы
from .models import *   # из файла models.py импортируем ВСЕ модели

def index(request):
    return render(request, 'women/index.html') # просто открываем страницу index.html

def category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id) # в переменную posts отфильтрованные записи таблицы Women
    cats = Category.objects.all() # в переменную cats ВСЕ записи таблицы Category
    return render(request, 'women/category.html', {'cats': cats, 'posts': posts})

def post(request, post_id):
    post = get_object_or_404(Women, pk=post_id) # в переменную post выбранную запись таблицы Women
    return render(request, 'women/post.html', {'post': post})

def addpage(request): # добавление Товара
    if request.method == 'POST':  # если запрос соответствует типу POST
        title = request.POST.get("title") # получение значения поля title
        return HttpResponse('<h2>Товар "{0}" добавлен в Базу данных</h2>'.format(title))
    else:  # если  не POST, то снова к заполнению Формы
        form = AddPostForm
        return render(request, 'women/addpage.html', context={'form': form})

def order(request):
    if request.method == "POST": # если метод типа POST, отправляем
        name = request.POST.get("name") # получение значения поля name
        phone = request.POST.get("phone") # получение значения поля phone
        email = request.POST.get("email") # получение значения поля email
        message = request.POST.get("name") # получение значения поля name
        return HttpResponse("<h2>{0}, Ваш заказ отправлен</h2>".format(name))
    else: # если метод не соответствует типу POST, возвращаемся к заполнению Формы
        userform = AddOrder()
        return render(request, "women/order.html", {"form": userform})

class UserLoginView(LoginView): # наследуемся от класса аутентификации LoginView
    template_name = 'women/login.html'
    # def reg(request):
    #     return HttpResponse("Ваш заh</h2>")