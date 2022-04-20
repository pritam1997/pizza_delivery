from django.urls import path
from . import views

urlpatterns = [
    path('1/', views.HelloAuthView.as_view(), name="hello_auth"),

]