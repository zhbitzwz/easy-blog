from django.contrib import admin
from .models import BlogPost
# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
	list_display = ('title','add_date')
	search_fields = ('title',)
	class Media:
		js = ['js/tinymce/tinymce.min.js','js/tinymce/config.js']

admin.site.register(BlogPost,BlogPostAdmin)
