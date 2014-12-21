#-*- coding:utf-8 -*-
from django.contrib.syndication.views import Feed
from .models import BlogPost

class ArticleFeed(Feed):
 	title = u"lwt's blog"
	link = "/blog/rss"
	description = "关注lwt的最新动态"

	def items(self):  
		return BlogPost.objects.order_by('-add_date')[:5]  

	def item_title(self, item):
		return item.title

	def item_description(self, item):  
		return item.abstract

	def item_link(self,item):  
		return item.get_absolute_url()

	def item_pubdate(self, item):
		return item.add_date

	def item_description(self, item):
		return item.get_html()


