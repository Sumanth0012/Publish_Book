from django.shortcuts import render
from django.shortcuts import get_object_or_404, HttpResponseRedirect
from .forms import BooksForm
from .forms import PublisherForm
from .forms import AuthorForm

from .models import Book
from .models import Author
from .models import Publisher

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy    

class list(ListView):
    model = Book
    template_name = "books/list_view.html"
    context_object_name = "details"
class detail(DetailView):
    model = Book
    template_name = "books/list_view.html"
    context_object_name = "details"
    pk_url_kwarg = "custom_pk"
class create(CreateView):
    model = Book
    fields = ["title", "authors", "publisher", "publication_date"]
    success_url = reverse_lazy('books')
    template_name = "books/index.html"
    form_class = BooksForm
class update(UpdateView):
    model = Book
    fields = ["title", "authors", "publisher", "publication_date"]
    template_name = "books/index.html"
    success_url = reverse_lazy('books')
class delete(DeleteView):
    model = Book
    template_name = "books/index.html"
    context_object_name = 'details'
    success_url = reverse_lazy('books')
    pk_url_kwarg = 'custom_pk'

    

# Create your views here.
def lib(request):
    context = {}
    form1 = AuthorForm(request.POST or None) 
    form2 = PublisherForm(request.POST or None) 
    form3 = BooksForm(request.POST or None) 
    if form1.is_valid(): 
        form1.save() 
    context['form1'] = form1
    if form2.is_valid(): 
        form2.save() 
    context['form2'] = form2
    if form3.is_valid(): 
        form3.save() 
    context['form3'] = form3
    # books = Book.objects.filter(title__contains='Book')
    return render(request, 'books/index.html',context)

def list_view(request):
    context = {}
    context["details"] = Book.objects.all()
    context["display"] = "none"
    return render(request, 'books/list_view.html',context)

def detailed_view(request,title):
    context = {}
    context["details"] = Book.objects.filter(title=title)
    context["display"] = "block"
    return render(request, 'books/list_view.html',context)

def update_view(request,title):
    context = {}
    obj = get_object_or_404(Book,title=title)

    form3 = BooksForm(request.POST or None,instance=obj) 
    if form3.is_valid(): 
        form3.save() 
        return HttpResponseRedirect("/"+id)
    context['form3'] = form3

    return render(request, 'books/index.html',context)

def delete_view(request,title):
    context = {}
    obj = get_object_or_404(Book,title=title)

    form3 = BooksForm(request.POST or None,instance=obj) 
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")

    return render(request, 'books/index.html',context)