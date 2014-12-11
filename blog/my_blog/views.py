from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from django.http import HttpResponse,Http404
from .models import BlogPost
from .utils import make_paginator

# Create your views here.
def home(request):
	blogposts = BlogPost.objects.all().order_by("-add_date")
	blogposts = make_paginator(request,blogposts)
	return render(request,'my_blog/index.html',dict(blogposts=blogposts))

def article(request,id):
	article = get_object_or_404(BlogPost, pk=id)
	return render(request,'my_blog/article.html',dict(article=article))

def blogpost(request,id):
	if id.isdigit():
		try:
			url = BlogPost.objects.all()[int(id)].get_absolute_url()
			return redirect(url)
		except:
			raise Http404
	else:
		return redirect('/')

def contact(request):
	return render(request,'my_blog/contact.html')
