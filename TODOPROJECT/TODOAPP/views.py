from django.http import HttpResponse
from django.shortcuts import render, redirect

from . form import todo_form
from .models import todo
# Create your views here.
def fun(request):
    x=todo.objects.all()


    if request.method=='POST':
        name=request.POST.get('name','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=todo(name=name,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'task':x})
def delete(request,id):
    x=todo.objects.get(id=id)
    if request.method=='POST':
        x.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    xy=todo.objects.get(id=id)
    zx=todo_form(request.POST or None,instance=xy)
    if zx.is_valid():
        zx.save()
        return redirect("/")
    return render(request,'update.html',{"zx":zx,xy:xy})








