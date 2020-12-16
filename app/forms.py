"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.db import models
from .models import Comment
from .models import Blog

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
class AnketaForm(forms.Form):
    name = forms.CharField(label='Ваше имя', min_length=2, max_length=100)
    city = forms.CharField(label='Ваш город', min_length=2, max_length=100)
    gender = forms.ChoiceField(label='Ваш пол',
        choices=[('1','мужской'),('2','женский')],
        widget=forms.RadioSelect, initial=1)
    mark = forms.CharField(label='Какую марку автомобиля хотите приобрести?', min_length=2, max_length=100)
    notice = forms.BooleanField(label='Получать новости сайта на e-mail?',
                                required=False)
    email = forms.EmailField(label='Ваш e-mail', min_length=7)
    feedback = forms.CharField(label='Ваше письмо',
                                widget=forms.Textarea(attrs={'rows':12, 'cols':20}))
    telephone = forms.CharField(label='Оставьте ваш номер телефона,и мы свяжемся с вами',min_length=10, max_length=12)


class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment # используемая модель
        fields = ('text',) # требуется заполнить только поле text
        labels = {'text': "Комментарий"} # метка к полю формы text

class BlogForm (forms.ModelForm):
    class Meta:
        model = Blog # используемая модель
        fields = ('title', 'description', 'content', 'image',) # требуется заполнить только поле text
        labels = {'title': "Заголовок", 'description':"Краткое содержание", 'content':"Полное содержание", 'image':"Картинка"} # метка к полю формы text