from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm
from django.http import HttpResponse
from django.contrib import messages

def index(request):
    rooms = Room.objects.filter(name__contains=request.GET.get('search', ''))
    
    context = {
        'rooms': rooms
    }
    return render(request, 'room/index.html', context)

def view(request, id):
    room = Room.objects.get(id=id)
    context = { 'room': room }
    return render(request, 'room/detail.html', context)

def edit(request, id):
    room = Room.objects.get(id=id)
    if request.method == 'GET':
        form = RoomForm(instance = room)
        context = { 
                    'form': form,
                    'id': id 
                  }
        return render(request, 'room/edit.html', context)
    
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid:
            form.save()
        context = { 
                    'form': form,
                    'id': id 
                  }
        messages.success(request, 'Sala Actualizada')
        return render(request, 'room/edit.html', context)

def create(request):
    if request.method == 'GET':
        form = RoomForm()
        context = { 
                    'form': form
                }
        return render(request, 'room/create.html', context)
    
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('room')
        else:
            return redirect('error')

def delete(request, id):
    room = Room.objects.get(id=id)
    room.delete()
    return redirect('room')