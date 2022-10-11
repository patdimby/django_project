from django.urls import path
from .views import PostList, PostDetail, BlogPage

urlpatterns = [
    path("api/<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path("api", PostList.as_view(), name="post_list"),
    path("", BlogPage, name="blog"),
]