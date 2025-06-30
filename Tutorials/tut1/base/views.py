from django.http import HttpResponse
from django.shortcuts import render
from .models import Roome



def home(request):
    context = {'rooms': Roome.objects.all()}
    return render(request,'base/home.html',context)

def room(request,id):
    room = Roome.objects.get(id=id)
    context = {'room':room}
    return render(request,'base/room.html',context)
