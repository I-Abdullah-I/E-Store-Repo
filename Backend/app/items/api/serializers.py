from rest_framework import serializers
from items.models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:#Check require when setting UI
        model = Item
        fields = '__all__'
        extra_kwargs={
                'store_id':{'required':False}
            }
        