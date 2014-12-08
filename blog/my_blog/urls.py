from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$',views.home),
	url(r'^blogpost/(?P<id>\d+)/$',views.blogpost),
	url(r'^article/(?P<id>\d+)/$',views.article),
)
