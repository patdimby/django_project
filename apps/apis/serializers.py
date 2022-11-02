from rest_framework import serializers, generics
from apps.books.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("title", "subtitle", "author", "isbn")
        
class HelloSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 20)
