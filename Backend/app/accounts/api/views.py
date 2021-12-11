from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from accounts.models import User
from stores.models import Store
from accounts.api.serializers import UserSerializer

@api_view(['POST', ])
@permission_classes(())
def api_create_user(request):
    user = User()
    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        response = {}
        response['message'] = 'Success!'
        return Response(response, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
def api_read_user_data(request):
    serializer = UserSerializer(request.user)
    dic_serializer = serializer.data

    try:
        if request.user.type==User.VENDOR:
            store = Store.objects.get(owner=request.user)
            if store is not None:
                dic_serializer['has_store'] = store.name
            else:
                dic_serializer['has_store'] = 'NO'
        else:
            dic_serializer['has_store'] = 'NOT_VENDOR'
    except Store.DoesNotExist:
            dic_serializer['has_store']='NO'
            return Response(dic_serializer)
    

    return Response(dic_serializer)

@api_view(['PUT', ])
@permission_classes((IsAuthenticated,))
def api_update_user_balance(request):
    request.user.balance = int(request.data['balance'])
    request.user.save()
    data = {}
    data['message'] = 'Balance Updated Successfully!'
    return Response(data)



