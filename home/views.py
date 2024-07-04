from django.shortcuts import render
from .models import Item
# Create your views here.
def index(request):
    item = Item.objects.all()
    context = {
        'item': item
    }
    return render(request, 'home/home.html', context)