from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('client/', include('client.urls')),
    path('room/', include('room.urls')),
    path('', views.index, name='index')
]
