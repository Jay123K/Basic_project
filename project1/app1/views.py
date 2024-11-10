from django.shortcuts import render,redirect
from .models import Person
from .forms import PersonForm

# Create your views here.

def Home(request):
    if request.method=='POST':
        form=PersonForm(request.POST,request.FILES)
        if form.is_valid():
            name=form.cleaned_data['name']
            age=form.cleaned_data['age']
            email=form.cleaned_data['email']
            city=form.cleaned_data['city']


            form.save()
            return redirect('/')

    form=PersonForm()
    return render(request,'app1/Templates/app1/Home.html',{'form':form})
