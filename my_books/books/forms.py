from django import forms
from .models import Comment
from django_summernote.widgets import SummernoteWidget
from captcha.fields import CaptchaField


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25, required=True,
                           widget=forms.TextInput(attrs={"class": "form-control mb-1"}), label="Имя")
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={"class": "form-control mb-1"}), label="Ваша почта")
    to = forms.EmailField(required=True,
                          widget=forms.TextInput(attrs={"class": "form-control mb-1"}), label="Почта получателя")
    comments = forms.CharField(required=False,
                               widget=forms.Textarea(
                                   attrs={"class": "form-control mb-1", }), label='Комментарий')

    captcha = CaptchaField(required=True, label='Капча')


class CommentForm(forms.ModelForm):
    body = forms.CharField(required=True,
                           widget=SummernoteWidget(
                               attrs={"class": "form-control",
                                      'summernote': {'width': '100%', 'height': '300px'}}), label='Комментарий')

    class Meta:
        model = Comment
        fields = ['body']


class SearchForm(forms.Form):
    query = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control mb-1", 'placeholder': 'Введите поисковой запрос'}))
