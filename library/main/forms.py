from .models import Books
from django.forms import ModelForm, TextInput, DateInput, NumberInput


class BooksForm(ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'name_author', 'date', 'count_page']
        widgets = {
            'title': TextInput(attrs={
                'placeholder': 'Название книги'
            }),
            'name_author': TextInput(attrs={
                'placeholder': 'Имя автора'
            }),
            'date': DateInput(attrs={
                'placeholder': 'Дата выхода'
            }),
            'count_page': NumberInput(attrs={
                'placeholder': 'Количество страниц'
            }),

        }