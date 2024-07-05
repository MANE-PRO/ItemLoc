from django.db import models
from signin.models import Profile

class Item(models.Model):
    prof = models.ForeignKey(Profile, on_delete = models.CASCADE)
    item_name = models.CharField(max_length=100)
    item_loc = models.CharField(max_length=100, blank = True)
    precise_loc = models.TextField(blank= True)
    item_desc = models.TextField(blank=True)
    img = models.ImageField(upload_to='photos/', blank=True)
    is_published = models.BooleanField(default=True)
    def __str__(self):
        return self.item_name
