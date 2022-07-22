from gc import collect
from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Friend, Pbook
from .forms import PbookForm
from django.views.generic import ListView

def index(request):
    data = Friend.objects.all()
    params = {
        'title': 'Hello',
        'data': data,
    }
    return render(request, 'hello/index.html', params)

def flower(request):
    return render(request, 'hello/flower.html')

def insect(request):
    return render(request, 'hello/insect.html')

def everything(request):
    return render(request, 'hello/everything.html')

def login(request):
    return render(request, 'hello/login.html')

def account(request):
    return render(request, 'hello/account.html')

# def create(request):
#     return render(request, 'hello/create.html')

def success(request):
    return render(request, 'hello/success.html')

def upgrading(request):
    return render(request, 'hello/upgrading.html')

def create(request):
    if (request.method == 'POST'):
        obj = Pbook()
        pbook = PbookForm(request.POST, instance=obj)
        pbook.save()
        return redirect(to='success')
    params = {
        'form': PbookForm(),
    }
    return render(request, 'hello/create.html', params)

class PbookList(ListView):
    model = Pbook




