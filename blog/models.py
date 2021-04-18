from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post (models.Model):  #cada clase va ser la propia tabla
    title = models.CharField(max_length=100) # cada atributo es un campo diferente en la bbdd
    content = models.TextField()
    data_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
