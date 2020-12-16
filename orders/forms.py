"""
definition of forms.
"""
from django import forms
from .models import *
#from django.contrib.auth.forms import authenticationform
#from django.utils.translation import ugettext_lazy as _
#from django.db import models
#from .models import comment
#from .models import blog
#
#class bootstrapauthenticationform(authenticationform):
#    """authentication form which uses boostrap css."""
#    username = forms.charfield(max_length=254,
#                               widget=forms.textinput({
#                                   'class': 'form-control',
#                                   'placeholder': 'user name'}))
#    password = forms.charfield(label=_("password"),
#                               widget=forms.passwordinput({
#                                   'class': 'form-control',
#                                   'placeholder':'password'}))
#class anketaform(forms.form):
#    name = forms.charfield(label='ваше имя', min_length=2, max_length=100)
#    city = forms.charfield(label='ваш город', min_length=2, max_length=100)
#    gender = forms.choicefield(label='ваш пол',
#        choices=[('1','мужской'),('2','женский')],
#        widget=forms.radioselect, initial=1)
#    mark = forms.charfield(label='какую марку автомобиля предпочитаете?', min_length=2, max_length=100)
#    notice = forms.booleanfield(label='получать новости сайта на e-mail?',
#                                required=false)
#    email = forms.emailfield(label='ваш e-mail', min_length=7)
#    feedback = forms.charfield(label='оставьте отзыв',
#                               widget=forms.textarea(attrs={'rows':12, 'cols':20}))

#class commentform (forms.modelform):
#    class meta:
#        model = comment # используемая модель
#        fields = ('text',) # требуется заполнить только поле text
#        labels = {'text': "комментарий"} # метка к полю формы text

#class blogform (forms.modelform):
#    class meta:
#       model = blog # используемая модель
#        fields = ('title', 'description', 'content', 'image',) # требуется заполнить только поле text
#        labels = {'title': "заголовок", 'description':"краткое содержание", 'content':"полное содержание", 'image':"картинка"} # метка к полю формы text



class CheckoutContactForm(forms.Form):
    name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    address = forms.CharField(required=True)