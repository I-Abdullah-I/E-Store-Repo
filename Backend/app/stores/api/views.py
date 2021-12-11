from accounts.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from stores.models import Store
from . import serializers


class StoreDetailsAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, name_of_store):
        try:
            store = Store.objects.get(name=name_of_store)
        except Store.DoesNotExist:
            return Response(data={'Error':'Your account doesnot own a store Or no store with this name'},status=status.HTTP_404_NOT_FOUND)
        
        store_serializer = serializers.StoreSerializer(store)
        return Response(store_serializer.data)

class StoreDetailsByID_API(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request,store_id):
        try:
            store = Store.objects.get(id = store_id)
        except Store.DoesNotExist:
            return Response(data={'Error':'Your account doesnot own a store, Or no store with this ID'},status=status.HTTP_404_NOT_FOUND)
        
        store_serializer = serializers.StoreSerializer(store)
        return Response(store_serializer.data)

class StoreByOwnerAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            store = Store.objects.get(owner=request.user)
        except Store.DoesNotExist:
            return Response(data={'Error':'Your account doesnot own a store'},status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

        
        store_serializer = serializers.StoreSerializer(store)
        data_of_user = {'Store':store_serializer.data,'Owner':{'Name':str(request.user.full_name) or 'No name', 'Email': str(request.user)}}
        return Response(data=data_of_user)


class StoreUpdateAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def put(self, request):
        try:
            store = Store.objects.get(owner=request.user)
        except Store.DoesNotExist:
            return Response(data={'Error':'Your account doesnot own a store'},status=status.HTTP_404_NOT_FOUND)
        
        store_serializer = serializers.StoreSerializer(store, data=request.data)
        data = {}
        if store_serializer.is_valid():
            store_serializer.save()
            data["update"] = "Successfully Updated"
            return Response(data=data , status=status.HTTP_200_OK)
        else :
            
            return Response(data=store_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StoreDeleteAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def delete(self, request):
        try:
            store = Store.objects.get(owner=request.user)
        except Store.DoesNotExist:
            return Response(data={'Error':'Your account doesnot own a store'},status=status.HTTP_404_NOT_FOUND)
        
        operation = store.delete()
        data = {}
        if operation:
            data["delete"] = "Successfully Deleted"
            return Response(data=data , status=status.HTTP_200_OK)
        else :
            data["delete"] = "Delete is failed"
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

class StoreCreateAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        if request.user.type != User.VENDOR:
            return Response(data={'User':'User is not vendor'},status=status.HTTP_400_BAD_REQUEST)
        store = Store(owner=request.user)
        store_serializer = serializers.StoreSerializer(store,data=request.data)
        
        data={}
        try:
            if store_serializer.is_valid():
                store_serializer.save()
                data["Create"]="Store is successfully created"
                return Response(data=data,status=status.HTTP_200_OK)
            else:
                return Response(store_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response(data={'Creation':'Check You havenot a store , May be another Error'},status=status.HTTP_400_BAD_REQUEST)


class StoreListAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = []
    def get(self, request):
        try:
            store = Store.objects.all()
        except Store.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        store_serializer = serializers.StoreSerializer(store, many=True)
     
        return Response(store_serializer.data)


# class StoresDeleteAPI(APIView):
#     def delete(self, request):
#         try:
#             store = Store.objects.all()
#         except Store.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
        
#         operation = store.delete()
#         data = {}
#         if operation:
#             data["delete"] = "Successfully Deleted"
#             return Response(data=data , status=status.HTTP_200_OK)
#         else :
#             data["delete"] = "Delete is failed"
#             return Response(data=data, status=status.HTTP_400_BAD_REQUEST)