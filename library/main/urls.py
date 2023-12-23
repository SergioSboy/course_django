from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='main'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.BooksDetailView.as_view(), name='book-detail'),
    path('<int:pk>/update', views.BooksUpdateView.as_view(), name='book-update'),
    path('<int:pk>/delete', views.BooksDeleteView.as_view(), name='book-delete'),
    path('sort-page', views.index_page, name='index_page'),
    path('sort-author', views.index_author, name='index_author'),
    path('sort-date', views.index_date, name='index_date'),

]
