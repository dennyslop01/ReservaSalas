from django.shortcuts import render, redirect
from .models import Client
from .forms import ClientForm
from django.http import HttpResponse
from django.contrib import messages

def index(request):
    clients = Client.objects.filter(name__contains=request.GET.get('search', ''))
    
    context = {
        'clients': clients
    }
    return render(request, 'client/index.html', context)

def view(request, id):
    client = Client.objects.get(id=id)
    context = { 'client': client }
    return render(request, 'client/detail.html', context)

def edit(request, id):
    client = Client.objects.get(id=id)
    if request.method == 'GET':
        form = ClientForm(instance = client)
        context = { 
                    'form': form,
                    'id': id 
                  }
        return render(request, 'client/edit.html', context)
    
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid:
            form.save()
        context = { 
                    'form': form,
                    'id': id 
                  }
        messages.success(request, 'Cliente Actualizado')
        return render(request, 'client/edit.html', context)

def create(request):
    if request.method == 'GET':
        form = ClientForm()
        context = { 
                    'form': form
                }
        return render(request, 'client/create.html', context)
    
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('client')
        else:
            return redirect('error')

def delete(request, id):
    client = Client.objects.get(id=id)
    client.delete()
    return redirect('client')