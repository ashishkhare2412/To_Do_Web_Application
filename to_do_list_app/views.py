from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .models import TodolistModel
from .forms import TodolistForm
import datetime
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        data = TodolistModel.objects.all()
        return render(request,'home.html',{'data':data})
    else:
        return redirect('ulogin')    

def cnt(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            f = TodolistForm(request.POST)
            if f.is_valid():
                t1 = f.save(commit=False)
                t1.time = datetime.datetime
                t1.user = request.user
                t1.save()
                fm = TodolistForm()
                return render(request,'cnt.html',{'fm':fm,'msg':'record added'})
            else:
                return render(request,'cnt.html',{'fm':f,'msg':'check errors'})
        else:
            fm = TodolistForm()
            return render(request,'cnt.html',{'fm':fm})
    else:
        return redirect('ulogin')

def deletetask(request,pk):
    d = TodolistModel.objects.get(id=pk)
    d.delete()
    return redirect('home')
