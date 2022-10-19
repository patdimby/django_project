from django.urls import path
from .views import info, blog, load_post, retails, about, contact, social_links, home

urlpatterns = [  
    path("info", info, name="info"),
    path("posts/<int:id>", retails, name="retails"),
    path("posts", load_post, name="posts"),
    path("socials", social_links, name="socials"),
    path("", home, name="home"),
    path("blog", blog, name="blog"),
    path("about", about, name="about"),
    path("contact", contact, name="contact"),
]