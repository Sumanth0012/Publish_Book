from django.shortcuts import render
from django.shortcuts import get_object_or_404, HttpResponseRedirect
from .forms import BooksForm
from .forms import PublisherForm
from .forms import AuthorForm

from .models import Book
from .models import Author
from .models import Publisher

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

def detailed_view(request,id):
    context = {}
    context["details"] = Book.objects.filter(id=id)
    context["display"] = "block"
    return render(request, 'books/list_view.html',context)

def update_view(request,id):
    context = {}
    obj = get_object_or_404(Book,id=id)

    form3 = BooksForm(request.POST or None,instance=obj) 
    if form3.is_valid(): 
        form3.save() 
        return HttpResponseRedirect("/"+id)
    context['form3'] = form3

    return render(request, 'books/index.html',context)

def delete_view(request,id):
    context = {}
    obj = get_object_or_404(Book,id=id)

    form3 = BooksForm(request.POST or None,instance=obj) 
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")

    return render(request, 'books/index.html',context)