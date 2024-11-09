from django.db import models
from django.core.validators import EmailValidator,MaxLengthValidator,MinLengthValidator,MaxValueValidator,MinValueValidator
from django.forms import ModelForm

# Create your models here.

class Person(models.Model):
    name=models.CharField(max_length=255)
    age=models.IntegerField(blank=False,null=False)
    email=models.EmailField(blank=True,null=True)
    city=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name