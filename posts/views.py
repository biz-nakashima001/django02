from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import post

# Create your views here.
def index(request):
    posts = post.objects.order_by('-published')
    # return HttpResponse('Hello World! このページは投稿のインデックスです。')
    return render(request, 'posts/index.html',{'posts':posts})

def post_detail(request,post_id):
    # postObj = post.objects.get(pk=post_id)
    postObj = get_object_or_404(post,pk=post_id)
    return render(request, 'posts/post_detail.html',{'post':postObj})
