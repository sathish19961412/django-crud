from django.shortcuts import render
from myapp.form import RegisterForm
# Create your views here.

def home(request):
    myform=RegisterForm()
    return render(request,'index.html',{'forms':myform})
