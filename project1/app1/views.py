from django.shortcuts import render
from django.template import loader

from .models import Person
from .forms import PersonForm

# Create your views here.

def Page1(request):
    # form = PersonForm(request.POST)
    # if form.is_valid():
    #     form.save()

    template=loader.get_template("app1/Home.html")
    



