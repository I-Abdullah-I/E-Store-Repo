from rest_framework import serializers
from records.models import Record

class RecordSerializer(serializers.ModelSerializer):
    class Meta:#Check require when setting UI
        model = Record
        fields = '__all__'
        extra_kwargs={
                'buyer':{'required':False},
                'item_id':{'required':False},
                'date_created':{'required':False},
            }
        