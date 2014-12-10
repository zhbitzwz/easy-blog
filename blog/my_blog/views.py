from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import HttpResponse,Http404
from .models import BlogPost

# Create your views here.
def home(request):
	blogposts = BlogPost.objects.all().order_by("-add_date")
	paginator = Paginator(blogposts, 2)
	try:
		page = int(request.GET.get("page", '1'))
	except ValueError:
		page = 1
	try:
		blogposts = paginator.page(page)
	except (InvalidPage, EmptyPage):
		blogposts = paginator.page(paginator.num_pages)
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
