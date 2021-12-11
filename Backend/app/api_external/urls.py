from . import views
from django.urls import path


urlpatterns = [
    path('me/', views.UserInfoAPI.as_view()),

]