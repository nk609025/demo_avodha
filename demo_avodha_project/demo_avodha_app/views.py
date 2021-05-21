from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . forms import ModeForm

from . models import shop
# Create your views here.

def demo(request):
    obj=shop.objects.all()
    return render(request,'home.html',{'obj':obj})
def detail(request,id):
    obj1=shop.objects.get(id=id)
    return render(request,'detail.html',{'obj1':obj1})
def add(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc = request.POST.get('desc')
        price = request.POST.get('price')
        img=request.FILES['img']

        s=shop(name=name,desc=desc,price=price,img=img)
        s.save()
        messages.info(request, 'product added')


    return render(request,'add_product.html')

def update(request,id):
    obj=shop.objects.get(id=id)
    form=ModeForm(request.POST or None,request.FILES,instance=obj)

    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'obj':obj,'form':form})
def delete(request,id):
    if request.method=='POST':
        obj=shop.objects.get(id=id)
        obj.delete()
        return redirect('/')

    return render(request,'delete.html')