from django.db import models
from django.contrib.auth.models import User
from django import forms

class Item(models.Model):
    prof = models.ForeignKey(User, on_delete = models.CASCADE, default=None)
    item_name = models.CharField(max_length=100)
    item_location = models.CharField(max_length=100, blank = True)
    precise_loc = models.TextField(blank= True)
    item_desc = models.TextField(blank=True)
    item_image = models.ImageField(upload_to='photos/', blank=True)
    is_published = models.BooleanField(default=True)
    def __str__(self):
        return self.item_name

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ('is_published', 'prof')

    