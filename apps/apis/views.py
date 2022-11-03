from apps.books.models import Book
from .serializers import BookSerializer, HelloSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Poll
# Create your views here.

class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    

class HelloApiView(APIView):
    """ Test API view"""
    serializer_class = HelloSerializer
    
    def get(self, request, format=None):
        """ Return a list of apiview future"""
        an_api_view = [
            'uses HTTP methods as function(get, post, put, delete, patch)',
            'is traditional like a Django view',
            'give you the most control over application logic',
            'is mapped manually to URLS'
        ]
        return Response({'message':'Hello, ', 'an_api_view': an_api_view})
    
    def post(self, request):
        """ create a  hello message """
        serializer = self.serializer_class(request.data)
        if serializer.is_valid():
            msg = serializer.validated_data.get('message')
            name = serializer._validated_data.get('name')
            message = f'{ msg } { name }'
            return Response({ 'message': message })
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def polls_list(request):
    MAX_OBJECTS = 20
    polls = Poll.objects.all()[:MAX_OBJECTS]
    data = {"results": list(polls.values("question", "created_by__username", "pub_date"))}
    return JsonResponse(data)

def polls_detail(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    data = {"results": {
        "question": poll.question,
        "created_by": poll.created_by.username,
        "pub_date": poll.pub_date
        }}
    return JsonResponse(data)