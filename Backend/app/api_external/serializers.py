from rest_framework import serializers


class EndUserSerializer(serializers.Serializer):
    full_name = serializers.CharField()
    email = serializers.CharField()
    type = serializers.CharField()
    balance = serializers.IntegerField()
    my_purchased_items = serializers.StringRelatedField(many=True)
    

class VendorSerializer(serializers.Serializer):
    full_name = serializers.CharField()
    email = serializers.CharField()
    type = serializers.CharField()
    balance = serializers.IntegerField()
    my_store = serializers.CharField()
    all_items_in_my_store = serializers.StringRelatedField(many=True)
    my_unsold_items = serializers.StringRelatedField(many=True)
    my_sold_items = serializers.StringRelatedField(many=True)
    

class AdminSerializer(serializers.Serializer):
    full_name = serializers.CharField()
    email = serializers.CharField()
    type = serializers.CharField() 