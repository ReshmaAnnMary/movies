from django.http import HttpResponse
from django.shortcuts import render, redirect
from  .forms import Form
from .models import movies


# Create your views here.


def index(request):
    data = movies.objects.all()
    context = {'movie_list': data}
    return render(request, 'index.html', context)


def details(request, id):
    data = movies.objects.get(id=id)
    return render(request, 'details.html', {'val': data})


def add(request):
    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']
        data = movies(name=name, desc=desc, year=year, img=img)
        data.save()
    return render(request, 'add.html')

def update(request,id):
    value=movies.objects.get(id=id)
    form=Form(request.POST or None,request.FILES,instance=value)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':value})

def delete(request,id):
    if request.method=='POST':
        id=movies.objects.get(id=id)
        id.delete()
        return redirect('/')
    return render(request,'delete.html')