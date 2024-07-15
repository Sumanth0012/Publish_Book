from django import forms

from .models import Book
from .models import Author
from .models import Publisher

class PublisherForm(forms.ModelForm): 

    class Meta:  
        model = Publisher
        fields = ["name", "website"] 

class AuthorForm(forms.ModelForm): 

    class Meta:  
        model = Author
        fields = ["first_name", "last_name", "email"] 

class BooksForm(forms.ModelForm): 

    class Meta:  
        model = Book
        fields = ["title", "authors", "publisher", "publication_date"] 