# -*- coding: utf-8 -*-
import calendar
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import CreateView
from .models import Post, Tag, Category, Social, Banner, Info, Message
from .serializers import PostSerializer, TagSerializer, InfoSerializer
from rest_framework import status
from .forms import MessageForm


from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

def blog(request):
    if request.method == 'GET':
        context = get_banner('blog')
    return render(request, 'posts/blog.html', context)


def home(request):
    if request.method == 'GET':
        context = get_banner('home')
    return render(request, 'posts/home.html', context)


def about(request):
    if request.method == 'GET':
        context = get_banner('about')
    return render(request, 'posts/about.html', context)


def contact(request):
    context = get_banner('contact')
    if request.method == 'GET':       
        context['form'] = MessageForm()
        return render(request, 'posts/contact.html', context)


def retails(request, id):
    if request.method == 'GET':
        post = Post.objects.get(id=id)
        post.day = post.publish.day
        post.month = calendar.month_abbr[post.publish.month]
        post.year = post.publish.year
        post.image = post.image.url
        banner = get_banner('details')
        tags = Tag.objects.all().order_by('name')
        categories = Category.objects.all().order_by('name')
        drafts = Post.objects.filter(status='DF').order_by('publish')
        recents = []
        for item in drafts:
            element = {
                'id': item.id,
                'month': calendar.month_abbr[item.publish.month],
                'day': item.publish.day,
                'year': item.publish.year,
                'author': item.author.username,
                'body': item.body,
                'category': item.category.name,
                'image': item.image.url,
                'slug': item.slug,
                'status': item.status,
                'tag': item.tag.name,
                'title': item.title,
                }
            recents.append(element)
        context = {
            'banner': banner,
            'obj': post,
            'tags': tags,
            'categories': categories,
            'recents': recents,
            }
        return render(request, 'posts/post-details.html', context)


def social_links(request):
    socials = Social.objects.all()
    data = []
    for soc in socials:
        item = {'id': soc.id, 'title': soc.title, 'link': soc.link}
        data.append(item)
    return JsonResponse({'data': data})


def parse_post(slug=None, status=None):
    posts = Post.objects.all().order_by('publish')
    socials = Social.objects.all()
    banner = []
    if slug:        
        banner = Banner.objects.get(slug=slug)
    tags = Tag.objects.all().order_by('name')
    categories = Category.objects.all().order_by('name')
    if status:
        posts = posts.filter(status)
    data = []
    for demo in posts:
        item = {
            'id': demo.id,
            'month': calendar.month_abbr[demo.publish.month],
            'day': demo.publish.day,
            'year': demo.publish.year,
            'author': demo.author.username,
            'body': demo.body,
            'category': demo.category.name,
            'image': demo.image.url,
            'slug': demo.slug,
            'status': demo.status,
            'tag': demo.tag.name,
            'title': demo.title,
            }
        data.append(item)
    return { 'data': data, 'banner': banner,'tags': tags, 'categories': categories , 'socials': socials }

def status_filter(p, keyvalue, status):
    result = list()
    for element in p:
        # Iterate over all the items in dictionary and filter items which has even keys
        for (key, value) in element.items():            
        # Check if key is even then add pair to new dictionary
            if key == keyvalue:
                if element[key] == status:
                    result.append(element)   
    return result

def get_banner(slug):
    general = parse_post(slug)   
    dt = general['data']   
    demos = []
    homes = []
    if slug == 'home':
        demos = status_filter(dt, 'status', 'BN')
        homes = status_filter(dt, 'status', 'DM')   
    context = {
        'tags': general['tags'],
        'categories': general['categories'],
        'data': status_filter(dt, 'status', 'PB'),
        'socials': general['socials'],
        'banner': general['banner'],
        'recents': status_filter(dt, 'status', 'DF'),
        'demos': demos,
        'homes': homes,
        }
    return context


def load_post(request):   
    posts = parse_post()
    data = posts['data']
    return JsonResponse({ 'data': data })


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
            return Response(post_serializer.data,
                            status=status.HTTP_201_CREATED)
    return Response(post_serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST)


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
            return Response(tag_serializer.data,
                            status=status.HTTP_201_CREATED)
    return Response(tag_serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST)


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
        return Response(post_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def info(request):
    if request.method == 'GET':
        result = Info.objects.all()
        serialize = InfoSerializer(result, many=True)
        return Response(serialize.data)


class MessageCreateView(CreateView):
    model = Message
    fields = ('name', 'email', 'subject', 'message',)
