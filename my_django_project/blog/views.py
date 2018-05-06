from django.shortcuts import render, get_object_or_404, get_list_or_404, reverse, redirect

# Create your views here.

from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
import datetime

# Create a simple view function
# Every view function must accept request object and return HttpResponse 
def index(request):
	return HttpResponse("Hello Django")
	
# Create a new view that displays the current time
from django.conf import settings

def today_is(request):
    now = datetime.datetime.now()
    return render(request, 'blog/datetime.html', {'now': now,'template_name': 'blog/nav.html' ,'base_dir': settings.BASE_DIR })
	
# view function to display a list of posts
from .models import Author, Tag, Category, Post
def post_list(request):
    posts = Post.objects.order_by("-id").all()
    return render(request, 'blog/post_list.html', {'posts': posts})

	
# view function to display a single post
def post_detail(request, pk, post_slug):    
	try:
		post = get_object_or_404(Post, pk=pk)
	except Post.DoesNotExist:
		return Http404("Post not found")
	return render(request, 'blog/post_detail.html', {'post': post})

# view function to display post by category
def post_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posts = get_list_or_404(Post.objects.order_by("-id"), category=category)
    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'blog/post_by_category.html', context)


# view function to display post by tag
def post_by_tag(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = get_list_or_404(Post.objects.order_by("-id"), tags=tag)
    context = {
        'tag': tag,
        'posts': posts,
    }
    return render(request, 'blog/post_by_tag.html', context )
	
def test_redirect(request):
    return redirect(reverse('post_list'))
