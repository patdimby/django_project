# -*- coding: utf-8 -*-
import calendar
from django.conf import settings
# from pathlib import Path
# from email.mime.image import MIMEImage
# from anymail.message import attach_inline_image_file

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import CreateView
from .models import Post, Tag, Category, Social, Banner, Info, Message, Comment
from .serializers import PostSerializer, TagSerializer, InfoSerializer
from rest_framework import status

from .forms import MessageForm
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail


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
    else:
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        email = request.POST.get('email')       
        form = MessageForm(request.POST)
        image_path = '/media/hand.jpg'
        # image_name = Path(image_path).name
        if form.is_valid():
            form.save()            
            send_mail(subject, message, email, [email])
            msg = EmailMultiAlternatives(
                subject = subject,
                body = message,
                from_email = name + " <"+ email + ">",
                to = ["Dimbisoa Patrick RANOELISON <patdimby@outlook.fr>", "patdimby@outlook.fr"],
                reply_to = ["Helpdesk <patdimby@outlook.fr>"])
            msg.tags = ["activation", "onboarding"]
            # Include an inline image in the html:
            # logo_cid = attach_inline_image_file(msg, settings.STATIC_URL + "images/hand.jpg")
            # html = """<img alt="Logo" src="cid:{logo_cid}">
            # <p>Please <a href="https://example.com/activate">activate</a>
            # your account</p>""".format(logo_cid=logo_cid)
            # msg.attach_alternative(html, "text/html")          
            # Send it:
            msg.send()
            context = get_banner('message')
            context['form'] = form
            return render(request, 'posts/send.html', context)
        else:
            return HttpResponse('Error')


def retails(request, id):
    if request.method == 'GET':       
        post = Post.objects.get(id=id)
        post.day = post.publish.day
        post.month = calendar.month_abbr[post.publish.month]
        post.year = post.publish.year
        post.image = post.image.url
        comments = list()       
        arr = Comment.objects.filter(post=post)
        for demo in arr:
            item = {
            'id': demo.id,
            'body': demo.body,
            'month': calendar.month_abbr[demo.updated_at.month],
            'image': settings.MEDIA_URL + str(demo.author.image),
            'day': demo.updated_at.day,
            'year': demo.updated_at.year,
            'author': demo.author.first_name + " " + demo.author.last_name,}
            comments.append(item)            
        context = get_banner('details')
        context['numbers'] = len(comments)
        context['comments'] = comments      
        context['form'] = MessageForm()
        context['obj'] = post
        return render(request, 'posts/post-details.html', context)
    else:
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        email = request.POST.get('email')       
        form = MessageForm(request.POST)
        # image_path = '/media/hand.jpg'
        # image_name = Path(image_path).name
        if form.is_valid():
            form.save()            
            send_mail(subject, message, email, [email])
            msg = EmailMultiAlternatives(
                subject = subject,
                body = message,
                from_email = name + " <"+ email + ">",
                to = ["Dimbisoa Patrick RANOELISON <patdimby@outlook.fr>", "patdimby@outlook.fr"],
                reply_to = ["Helpdesk <patdimby@outlook.fr>"])
            msg.tags = ["activation", "onboarding"]
            # Include an inline image in the html:
            # logo_cid = attach_inline_image_file(msg, settings.STATIC_URL + "images/hand.jpg")
            # html = """<img alt="Logo" src="cid:{logo_cid}">
            # <p>Please <a href="https://example.com/activate">activate</a>
            # your account</p>""".format(logo_cid=logo_cid)
            # msg.attach_alternative(html, "text/html")          
            # Send it:
            msg.send()
            context = get_banner('message')
            context['form'] = form
            return render(request, 'posts/send.html', context)
        else:
            return HttpResponse('Error')



def social_links(request):
    socials = Social.objects.all()
    data = []
    for soc in socials:
        item = {'id': soc.id, 'title': soc.title, 'link': soc.link}
        data.append(item)
    return JsonResponse({ 'data': data })

def simple_parse(posts):
    data = list()
    for demo in posts:
        item = {
            'id': demo.id,
            'month': calendar.month_abbr[demo.publish.month],
            'commentlength': len(Comment.objects.filter(post=demo)),
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
    return data

def parse_post(slug=None, status=None):
    posts = Post.objects.all().order_by('publish')
    socials = Social.objects.all()
    tags = Tag.objects.all().order_by('name')
    categories = Category.objects.all().order_by('name')    
    if slug:        
        banner = Banner.objects.get(slug=slug)
    else:
        banner = []
    if status:
        if slug != 'blog':
            posts = posts.filter(status)    
    data = simple_parse(posts)   
    return { 'data': data, 'banner': banner,'tags': tags, 'categories': categories , 'socials': socials }

def status_filter(p, keyvalue, status):
    result = list()
    for element in p:   
        for (key, value) in element.items():
            if key == keyvalue:
                if element[key] == status:
                    result.append(element)   
    return result

def get_banner(slug):
    general = parse_post(slug)   
    dt = general['data']
    if slug == 'home':
        demos = status_filter(dt, 'status', 'BN')
        homes = status_filter(dt, 'status', 'DM')
    else:
        demos = []
        homes = []   
    return { 'tags': general['tags'],'categories': general['categories'],
        'data': status_filter(dt, 'status', 'PB'), 'socials': general['socials'],
        'banner': general['banner'], 'recents': status_filter(dt, 'status', 'DF'),
        'demos': demos,'homes': homes, }


def load_post(request):   
    posts = parse_post()
    data = posts['data']
    return JsonResponse({ 'data': data })





@api_view(['GET'])
def info(request):
    if request.method == 'GET':
        result = Info.objects.all()
        serialize = InfoSerializer(result, many=True)        
        return Response(serialize.data)


