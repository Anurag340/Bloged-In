from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Roome
from .forms import RoomForm



def home(request):
    context = {'rooms': Roome.objects.all()}
    return render(request,'base/home.html',context)

def room(request,id):
    room = Roome.objects.get(id=id)
    context = {'room':room}
    return render(request,'base/room.html',context)


def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request,'base/room_form.html',context)

def updateRoom(request,id):
    room = Roome.objects.get(id=id)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form,'room':room}
    return render(request,'base/room_form.html',context)

def deleteRoom(request,id):
    room = Roome.objects.get(id=id)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request,'base/delete.html',{'obj':room})

