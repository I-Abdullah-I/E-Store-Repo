from . import views
from django.urls import path


app_name = "stores"
urlpatterns = [
    path('store/<str:name_of_store>/', views.StoreDetailsAPI.as_view()),
    path('storeById/<int:store_id>/', views.StoreDetailsByID_API.as_view()),
    path('stores/', views.StoreListAPI.as_view()),
    path('updateStore', views.StoreUpdateAPI.as_view()),
    path('deleteStore', views.StoreDeleteAPI.as_view()),
    path('createStore', views.StoreCreateAPI.as_view()),
    # path('deleteStores', views.StoresDeleteAPI.as_view(),name='Delete Store'),
    path('myStore/', view=views.StoreByOwnerAPI.as_view())
]