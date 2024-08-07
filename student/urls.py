from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.view,name='home'),
    path('add',views.add,name='add'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('history',views.history,name='history'),
    
]