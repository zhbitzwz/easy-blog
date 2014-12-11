from django.contrib import admin
from .models import BlogPost
from .forms import BlogPostAdminForm
# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
	list_display = ('title','add_date')
	search_fields = ('title',)
	exclude = ('html_file',)
	form = BlogPostAdminForm

	def save_model(self, request, obj, form, change):
		if change:
			obj.html_file.delete(save=False)
		obj.save()

admin.site.register(BlogPost,BlogPostAdmin)
