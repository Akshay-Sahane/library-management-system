from django.urls import path
from django.views.generic.base import TemplateView
from .views  import *

urlpatterns = [
    path('',TemplateView.as_view(template_name="library/home.html"),name="Home"),
    path('addbook/',BookCreateView.as_view(),name="addbook"),
    path('booklist/',BookListView.as_view(),name="booklist"),
    path('updatebook/<int:pk>',BookUpdateView.as_view(),name="updatebook"),
    path('deletebook/<int:pk>',BookDeleteView.as_view(),name='deletebook'),
    path('searchbook',SearchBook,name="searchbook"),
]