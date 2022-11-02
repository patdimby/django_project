from django.urls import path
from .views import BookAPIView, HelloApiView

urlpatterns = [
    path("", BookAPIView.as_view(), name="index"),
    path("hello-view", HelloApiView.as_view(), name="hello"),
]
