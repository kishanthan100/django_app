from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.
def index(request):
    block_title = "Lastest Post changed"
    post = [
       
    ]
    return render(request, 'index.html',{'block_title':block_title, 'posts':post})
def details(request):
    return render(request, 'details.html')

def old_url_redirect(request):
    return redirect(reverse('blog:new_page_url'))


def new_url_view(request):
    return HttpResponse("thiw is the new url")