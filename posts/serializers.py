from rest_framework import serializers
from .models import Post, Tag


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "author", "title", "body", "created_at", "image",)
        model = Post
        

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "name",)
        model = Tag
