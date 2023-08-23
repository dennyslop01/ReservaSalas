from django.shortcuts import render
from .models import Client

def index(request):
    clients = Client.objects.filter(name__contains=request.GET.get('search', ''))
    
    context = {
        'clients': clients
    }
    return render(request, 'client/index.html', context)

def view(request, id):
    client = Client.objects.get(id=id)
    context = { 'client': client}
    return render(request, 'client/detail.html', context)