from . import views
from django.urls import path


app_name = "records"


urlpatterns = [
    path('vendorRecords/', views.RecordByVendorAPI.as_view(),name='Vendor Records'),
    path('records/', views.RecordListAPI.as_view(),name='Show Records'),
    path('myRecords/', views.RecordByUserAPI.as_view(), name='My Records'),
    path('createRecord', views.RecordCreateAPI.as_view(), name='Create Record')
]