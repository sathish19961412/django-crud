from django.shortcuts import render,redirect
from myapp.form import RegisterForm
from myapp.models import Data
from django.contrib import messages
# Create your views here.

def home(request):
    myform=RegisterForm()
    mydata=Data.objects.all()
    if mydata!='':
        return render(request,'index.html',{'forms':myform,'datas':mydata})
    else:
        render(request,'index.html',{'forms':myform})

def addData(request):
    if request.method=='POST':
        myform=RegisterForm(request.POST)
        if myform.is_valid():
           myform.save()
           messages.success(request,"Record Added Successfully..!!")
           return redirect('Home')
        
def updateData(request,id):
    mydata=Data.objects.get(id=id)
    myform=RegisterForm(instance=mydata)
    if request.method=='POST':
        myform=RegisterForm(request.POST,instance=mydata)
        if myform.is_valid():
           myform.save()
           messages.success(request,"Record Update Successfully..!!")
           return redirect('Home')
    context={'forms':myform}
    return render(request,'update.html',context)

def deleteData(request,id):
    mydata=Data.objects.get(id=id)
    mydata.delete()
    messages.success(request,"Record Delete Successfully..!!")
    return redirect('Home')

