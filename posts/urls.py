from django.urls import path
from .views import PostList, PostDetail, BlogPage, load_post, retails, about, contact, social_links

urlpatterns = [
    path("api/<int:pk>", PostDetail.as_view(), name="post_detail"),
    path("api", PostList.as_view(), name="post_list"),
    path("posts/<int:id>", retails, name="retails"),
    path("posts", load_post, name="posts"),
    path("socials", social_links, name="socials"),
    path("", BlogPage, name="blog"),
    path("about", about, name="about"),
    path("contact", contact, name="contact"),
]