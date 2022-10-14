from django.urls import path
from .views import PostList, PostDetail, BlogPage, load_post

urlpatterns = [
    path("api/<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path("api", PostList.as_view(), name="post_list"),
    path("posts", load_post, name="posts"),
    path("", BlogPage, name="blog"),
]