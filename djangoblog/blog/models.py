from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name}{self.last_name}'


class Blog(models.Model):
    created_at = models.DateField()
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    description = models.TextField()
    updated_at = models.DateField()

    def __str__(self):
        return self.title