from rest_framework import serializers
from .models import Post, Tag, Info


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "author", "title", "body", "created_at", "image",)
        model = Post


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "name",)
        model = Tag


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "name", "phone", "adresse", "complement", "mail", "website",)
        model = Info
