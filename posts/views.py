from django.shortcuts import render
from rest_framework import generics
from .models import Post, Tag, Category
from .serializers import PostSerializer, TagSerializer
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
def BlogPage(request):
    tags = []
    if request.method == 'GET':
        tags = Tag.objects.all().order_by('name')
        categories = Category.objects.all().order_by('name')
        posts = Post.objects.all()
        print(posts)
    return render(request,'posts/blog.html', { 'tags': tags, 'categories': categories, 'posts': posts })

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


@api_view(['GET', 'POST'])
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        posts_serializer = PostSerializer(posts, many=True)
        return Response(posts_serializer.data)
    elif request.method == 'POST':
        post_serializer = PostSerializer(data=request.data)
        if post_serializer.is_valid():
            post_serializer.save()
            return Response(post_serializer.data, status=status.HTTP_201_CREATED)
    return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def tag_list(request):
    if request.method == 'GET':
        tags = Tag.objects.all()
        tags_serializer = TagSerializer(tags, many=True)
        return Response(tags_serializer.data)
    elif request.method == 'POST':
        tag_serializer = TagSerializer(data=request.data)
        if tag_serializer.is_valid():
            tag_serializer.save()
            return Response(tag_serializer.data, status=status.HTTP_201_CREATED)
    return Response(tag_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, pk):
    try:
        post = post.objects.get(pk=pk)
    except post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        post_serializer = PostSerializer(post)
        return Response(post_serializer.data)
    elif request.method == 'PUT':
        post_serializer = PostSerializer(post, data=request.data)
        if post_serializer.is_valid():
            post_serializer.save()
            return Response(post_serializer.data)
        return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

   
