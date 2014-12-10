from django.contrib import admin
from .models import BlogPost
# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
	list_display = ('title','add_date')
	class Media:
		js = ['js/123.js']

admin.site.register(BlogPost,BlogPostAdmin)
