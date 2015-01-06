from django import forms
from .models import BlogPost

class BlogPostAdminForm(forms.ModelForm):
    class Meta:
        model = BlogPost

    def _media(self):
		# 这里可为后台添加可视化编辑器插件
		js = []
        return forms.Media(js=js)

    media = property(_media)
