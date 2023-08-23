from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='client'),
    path('view/<int:id>', views.view, name='client_view'),
    path('edit/<int:id>', views.edit, name='client_edit'),
    path('create/', views.create, name='client_create'),
    path('delete/<int:id>', views.delete, name='client_delete')
]