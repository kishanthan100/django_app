from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from .models import Post
# Create your views here.


# posts = [
#        {'id':1,'title': 'Post 1', 'content': 'this is the content of post 1'},
#        {'id':2,'title': 'Post 2', 'content': 'this is the content of post 2'}
#     ]
def index(request):
    posts = Post.objects.all()
    block_title = "Lastest Post changed"
    
    return render(request, 'index.html',{'block_title':block_title, 'posts':posts})
def details(request,post_id):
    post = Post.objects.get(pk=post_id)
    
    #post = next((item for item in posts if item["id"] == post_id), None)
    # logger = logging.getLogger("testing")
    # logger.debug(f"post variable is {post}")
    
    return render(request, 'details.html',{'post':post})

def old_url_redirect(request):
    return redirect(reverse('blog:new_page_url'))


def new_url_view(request):
    return HttpResponse("thiw is the new url")