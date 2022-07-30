from django import forms
from .models import *

# Форма НЕ связанная с Базой Данных ===== Урок 13 =========================
# class AddPostForm(forms.Form):  # наследование от Класса Form
#     title = forms.CharField(max_length=255, label="Наименование")
#     content = forms.CharField(widget=forms.Textarea(attrs={"cools":60, "rows":10}), label="Описание")
#     price = forms.IntegerField(label="Цена")
#     photo = forms.ImageField(label="Фото")
# #   is_published = forms.BooleanField(label="Опубликовать")
#     cat = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категория", empty_label="Категория не выбрана")

# Форма связанная с Базой Данных ===== Урок 14 =========================
class AddPostForm(forms.ModelForm): # наследование от Класса ModelForm
    class Meta:
        model = Women     # связываем с моделью Women
        #fields ='__all__' # ВСЕ поля, кроме заполняемых автоматически
        # на практике указывают только необходимые поля:
        fields = ['title', 'content', 'price', 'photo', 'cat']

class AddOrder(forms.Form):
    name = forms.CharField()
    phone = forms.CharField(label="Ваш телефон")
    email = forms.EmailField(label="Ваш E-mail")
    message = forms.CharField(label="Номер лота")
