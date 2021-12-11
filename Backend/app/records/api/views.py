from accounts.models import User
from items.models import Item
from stores.models import Store
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from records.models import Record
from . import serializers


# class RecordDetailsAPI(APIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#     def get(self, request):
#         if request.user != User.ENDUSER:
#             return Response(data={'Error':'Your account isnot enduser'},status=status.HTTP_404_NOT_FOUND)
#         try:
#             record = Record.objects.get(buyer=request.user)
#         except Record.DoesNotExist:
#             return Response(data={'Error':'Your account doesnot own a Record'},status=status.HTTP_404_NOT_FOUND)
        
#         record_serializer = serializers.recordserializer(record)
#         return Response(record_serializer.data)

class RecordByUserAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        if request.user.type != User.ENDUSER:
            return Response(data={'Error':'Your account isnot enduser'},status=status.HTTP_404_NOT_FOUND)
        try:
            record = Record.objects.filter(buyer=request.user)
        except (Record.DoesNotExist):
            return Response(data={'Error':'Your account doesnot own a Record'},status=status.HTTP_404_NOT_FOUND)
        
        if record.count() > 0:
            record_serializer = serializers.RecordSerializer(record, many=True)
            return Response(record_serializer.data)
        else :
            return Response(data={'Error':'Your account doesnot own a Record'},status=status.HTTP_404_NOT_FOUND)

class RecordByVendorAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        record_list=[]
        if request.user.type != User.VENDOR:
            return Response(data={'Error':'Your account isnot vendor'},status=status.HTTP_404_NOT_FOUND)
        try:
            store = Store.objects.get(owner=request.user)
            items = Item.objects.filter(store_id=store)
            
            for item in items:
                
                records =  Record.objects.filter(item_id=item)
              
                if records.exists():
                    r = Record.objects.get(item_id=item)
                    record_list.append(r)
                    
            
        except (Record.DoesNotExist,Store.DoesNotExist,Item.DoesNotExist) :
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        record_serializer = serializers.RecordSerializer(record_list, many=True)
        return Response(record_serializer.data)

# class RecordUpdateAPI(APIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#     def put(self, request):
#         try:
#             record = Record.objects.get(owner=request.user)
#         except Record.DoesNotExist:
#             return Response(data={'Error':'Your account doesnot own a Record'},status=status.HTTP_404_NOT_FOUND)
        
#         record_serializer = serializers.recordserializer(record, data=request.data)
#         data = {}
#         if record_serializer.is_valid():
#             record_serializer.save()
#             data["update"] = "Successfully Updated"
#             return Response(data=data , status=status.HTTP_200_OK)
#         else :
#             print(record_serializer.errors)
#             return Response(data=record_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class RecordDeleteAPI(APIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#     def delete(self, request):
#         try:
#             record = Record.objects.get(owner=request.user)
#         except Record.DoesNotExist:
#             return Response(data={'Error':'Your account doesnot own a Record'},status=status.HTTP_404_NOT_FOUND)
        
#         operation = record.delete()
#         data = {}
#         if operation:
#             data["delete"] = "Successfully Deleted"
#             return Response(data=data , status=status.HTTP_200_OK)
#         else :
#             data["delete"] = "Delete is failed"
#             return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

class RecordCreateAPI(APIView): #Startfromhere
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        if request.user.type != User.ENDUSER:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        record= Record(buyer=request.user)
        # try:
        #     item = Item.objects.get(id=request.data['id'])
        # except Item.DoesNotExist:
        #     return Response(data={'Info':'No item with this ID'},status=status.HTTP_400_BAD_REQUEST)
        # record.item_id = item
        # record.quantity = request.data['quantity']
        record_serializer = serializers.RecordSerializer(record, data=request.data)
        
        data={}
        try:
            if record_serializer.is_valid():
                record_serializer.save()
                data["Create"]="Record is successfully created"
                return Response(data=data,status=status.HTTP_200_OK)
            else:
                return Response(record_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response(data={'Creation':'Check You havenot a Record'},status=status.HTTP_400_BAD_REQUEST)


class RecordListAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        if request.user.type != User.ADMIN:
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            record = Record.objects.all()
        except Record.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        record_serializer = serializers.RecordSerializer(record, many=True)
     
        return Response(record_serializer.data)


# class recordsDeleteAPI(APIView):
#     def delete(self, request):
#         try:
#             record = Record.objects.all()
#         except Record.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
        
#         operation = record.delete()
#         data = {}
#         if operation:
#             data["delete"] = "Successfully Deleted"
#             return Response(data=data , status=status.HTTP_200_OK)
#         else :
#             data["delete"] = "Delete is failed"
#             return Response(data=data, status=status.HTTP_400_BAD_REQUEST)