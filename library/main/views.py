from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView
from .models import Books
from .forms import BooksForm


# Create your views here.
def index(request):
    books_title = Books.objects.order_by('title')
    return render(request, 'main/index.html', {'books': books_title})


def index_author(request):
    books_author = Books.objects.order_by('name_author')
    return render(request, 'main/index.html', {'books': books_author})


def index_page(request):
    books_page = Books.objects.order_by('count_page')
    return render(request, 'main/index.html', {'books': books_page})


def index_date(request):
    books_date = Books.objects.order_by('date')
    return render(request, 'main/index.html', {'books': books_date})


class BooksDetailView(DetailView):
    model = Books
    template_name = 'main/details_view.html'
    context_object_name = 'book'


class BooksUpdateView(UpdateView):
    model = Books
    template_name = 'main/create.html'
    form_class = BooksForm


class BooksDeleteView(DeleteView):
    model = Books
    success_url = '/'
    template_name = 'main/books-delete.html'


def create(request):
    error = ""
    if request.method == "POST":
        form = BooksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error = 'Форма неверна!'
    form = BooksForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', data)
