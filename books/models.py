from django.db import models
from django.utils import timezone

class Publisher(models.Model):
    name = models.CharField(max_length=255)
    website = models.URLField()

    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField(default=timezone.now)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author, related_name='books')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='books')
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13, default="asdf")
    price = models.DecimalField(max_digits=6, decimal_places=2,default=250.00)
    pages = models.IntegerField(default=1000)

    def __str__(self):
        return self.title
# Create your models here.
