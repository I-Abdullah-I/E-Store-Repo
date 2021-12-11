from rest_framework import serializers
from stores.models import Store

class StoreSerializer(serializers.ModelSerializer):
    class Meta:#Check require when setting UI
        model = Store
        fields = '__all__'
        extra_kwargs={
                'owner':{'required':False}
            }
        