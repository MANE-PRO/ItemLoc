from django.shortcuts import render, redirect
from .models import Item, ItemForm
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    item = Item.objects.filter(prof = request.user).order_by('-item_name')
    if 'itemname' in request.GET and request.GET['itemname'] != "":
        item = item.filter(item_name__iexact = request.GET['itemname']).order_by('-item_name')
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

def create_item(request):
    forms = ItemForm()
    if request.method == 'POST':
        forms = ItemForm(request.POST, request.FILES)
        if(forms.is_valid()):
            x = forms.save(commit=False)
            x.prof = request.user
            forms.save()
            return redirect('index')
        else:
            forms = ItemForm()
    return render(request, 'home/itemcreate.html', {"form": forms})




