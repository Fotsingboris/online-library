from django.shortcuts import render
from django.http import HttpResponse
from books.forms import StoreForms
from multiprocessing import context

from books.forms import Store
from .models import *
# Create your views here.

def home(request):
    if request.POST:
        form = StoreForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Successfully Stored!</h1>')
    else:
        form = StoreForms()
    context = {
            'form': form
    }
    return render(request, 'index.html', context)

def result(request):
    customer = Store.objects.all()
    context = {
        'customer': customer,
    }
    return render(request, 'result.html', context)