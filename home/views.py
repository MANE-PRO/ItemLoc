from django.shortcuts import render
from .models import Item
from signin.models import Profile
# Create your views here.
def index(request):
    if request.GET:
        if 'itemname' in request.GET:
            item = Item.objects.filter(item_name__iexact = request.GET['itemname']).order_by('-item_name')
        else:
            prof = Profile.objects.filter(username = request.GET['username'])
            item = Item.objects.filter(prof = prof[0]).order_by('-item_name')
    context = {
        'item': item,
        'value':request.GET
    }
    return render(request, 'home/home.html', context)

def item(request, item_id):
    item = Item.objects.filter(id = item_id)
    context = {
        'item': item[0]
    }
    return render(request, 'home/item.html', context)