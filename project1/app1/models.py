from django.db import models
from django.core.validators import EmailValidator,MaxLengthValidator,MinLengthValidator,MaxValueValidator,MinValueValidator
from django.forms import ModelForm

# Create your models here.

class Person(models.Model):
    name=models.CharField(max_length=255)
    age=models.IntegerField(blank=False,null=False)
    email=models.EmailField(unique=True,blank=True,null=True)
    city=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    person=models.ForeignKey(Person,on_delete=models.CASCADE)
    order_date=models.DateField(null=True,blank=True)
    