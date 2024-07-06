from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:item_id>/', views.item, name = 'item'),
    path('createitem', views.create_item, name='createitem')
]