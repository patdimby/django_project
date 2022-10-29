from .views import ListTodo, DetailTodo
from django.urls import path


urlpatterns = [
    path("<int:pk>/", DetailTodo.as_view(), name="detail"),
    path("", ListTodo.as_view(), name="list"),
]