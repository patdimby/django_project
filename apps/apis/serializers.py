from rest_framework import serializers, generics
from apps.books.models import Book
from .models import Poll, Choice, Vote

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'

class ChoiceSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, required=False)
    class Meta:
        model = Choice
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("title", "subtitle", "author", "isbn")
        
class HelloSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 20)
    

class PollSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = Poll
        fields = '__all__'
