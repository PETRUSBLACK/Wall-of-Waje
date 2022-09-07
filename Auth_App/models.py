from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.TextField( )
    last_name = models.TextField( )
    
    def __str__(self):
        return self.first_name


class Book(models.Model):
    name = models.TextField(max_length=30)
    isbn = models.TextField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    