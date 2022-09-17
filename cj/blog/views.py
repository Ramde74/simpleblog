from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    cats = Category.objects.all()
    data = {

        'cats': cats
    }

    return render(request,'home.html',data)

def category(request,url):
    cat=Category.objects.get(url=url)
    return render(request,'category.html',{'cat':cat})