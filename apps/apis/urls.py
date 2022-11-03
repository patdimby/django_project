from django.urls import path
from .views import BookAPIView, HelloApiView
from .apiviews import PollList, PollDetail

urlpatterns = [
    path("", BookAPIView.as_view(), name="index"),
    path("hello-view", HelloApiView.as_view(), name="hello"),
    path("polls", PollList.as_view(), name="polls_list"),
    path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
]
