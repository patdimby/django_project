from django.urls import path
from .views import *

urlpatterns = [
    path("", toy_list),
    path("<int:pk>", toy_detail),
]
