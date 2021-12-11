from django.urls import path

from accounts.api.views import(
    api_create_user,
    api_read_user_data,
    api_update_user_balance,
)

from rest_framework.authtoken.views import obtain_auth_token

app_name = 'accounts'

urlpatterns = [
    path('create', api_create_user, name='create'),
    path('login', obtain_auth_token, name='login'),
    path('read', api_read_user_data, name='read'),
    path('updateBalance', api_update_user_balance, name='updateBalance'),
]