from django.shortcuts import redirect, render

# Create your views here.


from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from .models import Book
from .forms import BookForm
from django.urls import reverse_lazy

# CreateView is used for creation
class BookCreateView(SuccessMessageMixin,CreateView):
    model = Book
    form_class=BookForm
    template_name = "library/bookform.html"
    success_message="book is added successfully..."
    success_url=reverse_lazy('booklist')

# ListView is used for creation
from django.views.generic.list import ListView

class BookListView(ListView):
    model = Book
    template_name ='library/booklist.html'

# UpdateView is used for creation
from django.views.generic.edit import UpdateView

class BookUpdateView(SuccessMessageMixin,UpdateView):
    model = Book
    form_class=BookForm
    template_name ="library/bookform.html"
    success_message="book Is Updated Successfully..."
    success_url=reverse_lazy("booklist")

# DeleteView is used for creation
from django.views.generic.edit import DeleteView
class BookDeleteView(SuccessMessageMixin,DeleteView):
    model = Book
    template_name = "library/delete_confirm.html"
    success_message="book is Deleted Successfully..."
    success_url = reverse_lazy("booklist")

# function based view for searching book in a database
def SearchBook(req):
    q=req.GET['q']
    l=q.lower()
    blist=Book.objects.filter(BookName__contains=l)
    context={'object_list':blist}
    return render(req,"library/booklist.html",context)