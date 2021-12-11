from accounts.models import User
from stores.models import Store
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from items.models import Item
from . import serializers



class ItemInStoreVendorAPI(APIView): #Name_of_item for vendors
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, name_of_item):
        if request.user.type != User.VENDOR:
            return Response(data={'Note':'You are not a vendor'},status=status.HTTP_404_NOT_FOUND)
        try:
            store = Store.objects.get(owner = request.user)
            items = Item.objects.filter(store_id=store, name=name_of_item)
        except (Item.DoesNotExist , Store.DoesNotExist):
            return Response(data={'Error':'There is no Items in store or There is no store with this name'},status=status.HTTP_404_NOT_FOUND)
        
        if items.count()>0:
            item_serializer = serializers.ItemSerializer(items, many=True)
            return Response(item_serializer.data)
        else:
            return Response(data={'Note':'No Items Found'},status=status.HTTP_404_NOT_FOUND)

class ItemInStoreEndUserAPI(APIView): #Name_of_item / Name_of_store for EndUsers
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, name_of_store, name_of_item):
        if request.user.type != User.ENDUSER:
            return Response(data={'Note':'You are not an end user'},status=status.HTTP_404_NOT_FOUND)
        try:
            store = Store.objects.get(name=name_of_store)
            items = Item.objects.filter(store_id=store, name=name_of_item)
        except (Item.DoesNotExist , Store.DoesNotExist):
            return Response(data={'Error':'There is no Items in store or There is no store with this name'},status=status.HTTP_404_NOT_FOUND)
        
        if items.count()>0:
            item_serializer = serializers.ItemSerializer(items, many=True)
            return Response(item_serializer.data)
        else:
            return Response(data={'Note':'No Items Found'},status=status.HTTP_404_NOT_FOUND)

class ItemInStoreAPI(APIView): #All Items in a specific store for endUser
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, name_of_store):
        if request.user.type != User.ENDUSER:
            return Response(data={'Note':'You are not an end user'},status=status.HTTP_404_NOT_FOUND)
        try:
            store = Store.objects.get(name=name_of_store)
            items = Item.objects.filter(store_id=store)
        except (Item.DoesNotExist , Store.DoesNotExist):
            return Response(data={'Error':'There is no Items in store or There is no store with this name'},status=status.HTTP_404_NOT_FOUND)
        
        if items.count()>0:
            item_serializer = serializers.ItemSerializer(items, many=True)
            return Response(item_serializer.data)
        else:
            return Response(data={'Note':'No Items Found'},status=status.HTTP_404_NOT_FOUND)

class ItemByUserAPI(APIView): #All items in Vendor Users
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        if request.user.type != User.VENDOR:
            return Response(data={'Note':'You are not a vendor, Therefore You don\'t own a store'},status=status.HTTP_404_NOT_FOUND)
        try:
            store = Store.objects.get(owner=request.user)
            items = Item.objects.filter(store_id=store)
        except (Item.DoesNotExist , Store.DoesNotExist):
            return Response(data={'Error':'Your account doesnot own a store or There is no Items in store'},status=status.HTTP_404_NOT_FOUND)
        
        if items.count()>0:
            item_serializer = serializers.ItemSerializer(items, many=True)
            return Response(item_serializer.data)
        else:
            return Response(data={'Note':'No Items Found'},status=status.HTTP_404_NOT_FOUND)


class ItemUpdateAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def put(self, request, name_of_item):
        if request.user.type != User.VENDOR:
            return Response(data={'Note':'You are not a vendor, Therefore You don\'t own a store'},status=status.HTTP_404_NOT_FOUND)
        try:
            store = Store.objects.get(owner=request.user)
            
            item = Item.objects.get(store_id=store, name=name_of_item)
            
        except (Item.DoesNotExist , Store.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        item_serializer = serializers.ItemSerializer(item, data=request.data)
        data = {}
        if item_serializer.is_valid():
            item_serializer.save()
            data["update"] = "Successfully Updated"
            return Response(data=data , status=status.HTTP_200_OK)
        else :
            
            return Response(data=item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemUpdatebyID_API(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def put(self, request, item_id):
        if request.user.type != User.VENDOR:
            return Response(data={'Note':'You are not a vendor, Therefore You don\'t own a store'},status=status.HTTP_404_NOT_FOUND)
        try:
            
            item = Item.objects.get(id=item_id)
            
        except (Item.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        item_serializer = serializers.ItemSerializer(item, data=request.data)
        data = {}
        if item_serializer.is_valid():
            item_serializer.save()
            data["update"] = "Successfully Updated"
            return Response(data=data , status=status.HTTP_200_OK)
        else :
            
            return Response(data=item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ItemDeleteAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def delete(self, request, name_of_item):
        if request.user.type != User.VENDOR:
            return Response(data={'Note':'You are not a vendor, Therefore You don\'t own a store'},status=status.HTTP_404_NOT_FOUND)
        try:
            store = Store.objects.get(owner=request.user)
            item = Item.objects.get(store_id=store, name=name_of_item)
        except (Item.DoesNotExist , Store.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        operation = item.delete()
        data = {}
        if operation:
            data["delete"] = "Successfully Deleted"
            return Response(data=data , status=status.HTTP_200_OK)
        else :
            data["delete"] = "Delete is failed"
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


class ItemDeleteByID_API(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def delete(self, request, item_id):
        if request.user.type != User.VENDOR:
            return Response(data={'Note':'You are not a vendor, Therefore You don\'t own a store'},status=status.HTTP_404_NOT_FOUND)
        try:
            store = Store.objects.get(owner=request.user)
            item = Item.objects.get(store_id=store, id=item_id)
        except (Item.DoesNotExist , Store.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        operation = item.delete()
        data = {}
        if operation:
            data["delete"] = "Successfully Deleted"
            return Response(data=data , status=status.HTTP_200_OK)
        else :
            data["delete"] = "Delete is failed"
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

class ItemCreateAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        if request.user.type != User.VENDOR:
            return Response(data={'Note':'You are not a vendor, Therefore You don\'t own a store'},status=status.HTTP_404_NOT_FOUND)
        try:
            store = Store.objects.get(owner=request.user)
        except (Item.DoesNotExist , Store.DoesNotExist):
            return Response(data={'Error':'Your Vendor account doesnot own a store'},status=status.HTTP_404_NOT_FOUND)
        item = Item(store_id=store)
        if int(request.data['quantity']) < 0 or int(request.data['price']) < 0:
            return Response(data={'Error':'No Negative Numbers'},status=status.HTTP_400_BAD_REQUEST)
        item_serializer = serializers.ItemSerializer(item,data=request.data)
        
        data={}

        if item_serializer.is_valid():
            item_serializer.save()
            data["Create"]="Item is successfully created"
            return Response(data=data,status=status.HTTP_200_OK)
        else:
            return Response(item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemListAPI(APIView): #All items in system for end User , Restricted Items for Vendor
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        if request.user.type == User.VENDOR:
            try:
                store = Store.objects.get(owner=request.user)
                item = Item.objects.filter(store_id=store)
            except (Item.DoesNotExist , Store.DoesNotExist):
                return Response(data={'Error':'There is no Items in store or There is no store with this name'},status=status.HTTP_404_NOT_FOUND)
        else :
            try:
                item = Item.objects.all()
            except Item.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        
        item_serializer = serializers.ItemSerializer(item, many=True)
     
        return Response(item_serializer.data)


class ItemListByItemNameAPI(APIView): #All Items in system by specific name for End Users
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, name_of_item):
        if request.user.type != User.VENDOR:
            try:
                items = Item.objects.filter(name=name_of_item)
            except Item.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else :
            return Response(data={'Note':'For endusers and admins only'})
        
        if items.count()>0:
            item_serializer = serializers.ItemSerializer(items, many=True)
            return Response(item_serializer.data)
        else:
            return Response(data={'Note':'No Items Found'},status=status.HTTP_404_NOT_FOUND)

class ItemsDeleteAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def delete(self, request):
        if request.user.type != User.VENDOR:
            return Response(data={'Note':'You are not a vendor, Therefore You don\'t own a store'},status=status.HTTP_404_NOT_FOUND)
        try:
            store = Store.objects.get(owner=request.user)
            item = Item.objects.filter(store_id=store)
        except (Item.DoesNotExist , Store.DoesNotExist):
            return Response(data={'Error':'There is no Items in store or There is no store with this name'},status=status.HTTP_404_NOT_FOUND)

        operation = item.delete()
        data = {}
        if operation:
            data["delete"] = "Successfully Deleted"
            return Response(data=data , status=status.HTTP_200_OK)
        else :
            data["delete"] = "Delete is failed"
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


class ItemByID_API(APIView): #Get Item by ID for vendors and endusers
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, item_id):
        try:
            item = Item.objects.get(id=item_id)
        except (Item.DoesNotExist , Store.DoesNotExist):
            return Response(data={'Error':'There is no Items in store or There is no store with this name'},status=status.HTTP_404_NOT_FOUND)
        
   
        item_serializer = serializers.ItemSerializer(item)
        return Response(item_serializer.data)
