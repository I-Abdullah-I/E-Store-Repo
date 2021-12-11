from django.db import models
from accounts.models import User
from stores.models import Store
from items.models import Item
from django.core.exceptions import ValidationError
# Create your models here.

class Record(models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE ,null=False)
    quantity = models.IntegerField()
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True, null=False)

    def save(self):
        if self.buyer.type != User.ENDUSER:
            raise ValidationError(message='Only EndUsers can buy')

        if self.item_id.quantity >= self.quantity and self.buyer.balance > (self.quantity*self.item_id.price) :
            self.item_id.quantity -= self.quantity
            self.item_id.store_id.owner.balance = self.item_id.store_id.owner.balance + (self.quantity*self.item_id.price)
            self.buyer.balance = self.buyer.balance - (self.quantity*self.item_id.price)
            
            self.item_id.save()
            self.item_id.store_id.owner.save()
            self.buyer.save()
        else:
            raise ValidationError(message='Transaction not succeed')
        super(Record,self).save()

    def __str__(self):
        return 'Record {}'.format(self.id)