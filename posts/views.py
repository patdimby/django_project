import re
from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from rest_framework import generics
from .models import Post, Tag, Category, Social
from .serializers import PostSerializer, TagSerializer
from rest_framework import status
# from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
def BlogPage(request):
    tags = []
    if request.method == 'GET':
        tags = Tag.objects.all().order_by('name')
        categories = Category.objects.all().order_by('name')
        posts = Post.objects.all()
        data = []
        for post in posts:
            item = {
                'id': post.id,
                'day': post.publish.day,
                'year': post.publish.year,
                'author': post.author.username,
                'body' : post.body, 
                'category' : post.category.name,
                'image' : post.image.url,            
                'slug' : post.slug,
                'status' : post.status,
                'tag' : post.tag.name,
                'title' : post.title
            }
            data.append(item)
       
    return render(request,'posts/blog.html', { 'tags': tags, 'categories': categories , 'data': data })

def about(request):
    if request.method == 'GET':
        tags = Tag.objects.all().order_by('name')
        categories = Category.objects.all().order_by('name')
        socials = Social.objects.all()
        context= {'tags': tags, 'categories': categories , 'socials': socials }
    return render(request, 'posts/about.html', context)


def contact(request):
    return render(request, 'posts/contact.html')


def retails(request, id):
    if request.method == 'GET':
        post = Post.objects.get(id=id)
        print(post)
        return render(request, "posts/post-details.html", {'post': post })

def social_links(request):
    socials = Social.objects.all()
    data = []
    for soc in socials:
        item = {
            'id': soc.id,
            'title': soc.title,
            'link': soc.link            
        }
        data.append(item)
    return JsonResponse({ 'data': data })

def load_post(request):
    posts = Post.objects.all()
    data = []
    for post in posts:
        item = {
            'id': post.id,
            'day': post.publish.day,
            'month':post.publish.month,
            'year': post.publish.year,
            'author': post.author.username,
            'body' : post.body, 
            'category' : post.category.name,
            'image' : post.image.url,            
            'slug' : post.slug,
            'status' : post.status,
            'tag' : post.tag.name,
            'title' : post.title
        }
        data.append(item)
    return JsonResponse({ 'data': data })

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

