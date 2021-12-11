from . import views
from django.urls import path


app_name = "items"
urlpatterns = [
    path('items_in_store/<str:name_of_store>/', views.ItemInStoreAPI.as_view(),name='Show Item'),
    path('items_sys/', views.ItemListAPI.as_view(),name='Show Items'),
    path('updateItem/<str:name_of_item>', views.ItemUpdateAPI.as_view(),name='Update Item'),
    path('updateItembyID/<int:item_id>', views.ItemUpdatebyID_API.as_view()),
    path('deleteItem/<str:name_of_item>', views.ItemDeleteAPI.as_view(),name='Delete Item'),
    path('deleteItembyID/<int:item_id>', views.ItemDeleteByID_API.as_view(),name='Delete Item'),
    path('createItem', views.ItemCreateAPI.as_view(),name='Create Item'),
    path('deleteItems', views.ItemsDeleteAPI.as_view(),name='Delete Items'),
    path('myItems/', view=views.ItemByUserAPI.as_view(), name='My Item'),
    path('byItemName/<str:name_of_item>/',views.ItemListByItemNameAPI.as_view(), name='Items ByName'),
    path('item_in_store_vendor/<str:name_of_item>/', views.ItemInStoreVendorAPI.as_view(), name='Item Vendor'),
    path('item_in_store_enduser/<str:name_of_store>/<str:name_of_item>/', views.ItemInStoreEndUserAPI.as_view(), name='Item User'),
    path('item_by_ID/<int:item_id>/', views.ItemByID_API.as_view(), name='Item ID'),

]