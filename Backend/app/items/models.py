from django.db import models
from accounts.models import User
from stores.models import Store
# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE, null=False, blank=False )


    def __str__(self):
        return 'ID {0}:{1}'.format(self.id,self.name)
