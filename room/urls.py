from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='room'),
    path('view/<int:id>', views.view, name='room_view'),
    path('edit/<int:id>', views.edit, name='room_edit'),
    path('create/', views.create, name='room_create'),
    path('delete/<int:id>', views.delete, name='room_delete')
]