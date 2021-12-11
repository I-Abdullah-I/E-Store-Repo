from django.db import reset_queries
from accounts.models import User
from records.models import Record
from stores.models import Store
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from items.models import Item
from .serializers import *

class UserInfoAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        if request.user.type == User.ENDUSER:
            records = Record.objects.filter(buyer=request.user).values()
            res = []
            for record in records:
                record['item'] = Item.objects.get(id=record['item_id_id']).name
                res.append(record)
            result = {
                'full_name':request.user.full_name, 'email':str(request.user), 'type': request.user.type, 'balance': request.user.balance, 'my_purchased_items':res
            }
            enduserserializer = EndUserSerializer(result)
            return Response(data=enduserserializer.data)
        elif request.user.type == User.VENDOR:
            try:
                owned_store = Store.objects.get(owner=request.user)
                all_items = Item.objects.filter(store_id=owned_store)
               
                unsold_items = all_items.exclude(quantity=0).values()
            
                sold_items = []
             
                if all_items.count() > 0:
                    for item in all_items:
                        records = Record.objects.filter(item_id=item).values()
                        if records.count() > 0:
                            for record in records:
                                sold_items.append(record)
                
            except (Store.DoesNotExist, Item.DoesNotExist, Record.DoesNotExist):
                return Response({'Note':'Error may be no store/item/record'}, status=status.HTTP_400_BAD_REQUEST)

            res = []
            for sold_item in sold_items:
                sold_item['item'] = Item.objects.get(id=sold_item['item_id_id']).name
                res.append(sold_item)
            result = {
                'full_name':request.user.full_name, 'email':str(request.user), 'type': request.user.type, 'balance': request.user.balance, 'my_store':owned_store.name,
                'all_items_in_my_store':all_items.values(), 'my_unsold_items':unsold_items, 'my_sold_items':res
            }
            # vendorserializer = VendorSerializer(result)
            return Response(result)
        elif request.user.type == User.ADMIN:
            result = {
                'full_name':request.user.full_name, 'email':str(request.user), 'type': request.user.type
            }
            adminserializer = AdminSerializer(result)
            return Response(data=adminserializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
