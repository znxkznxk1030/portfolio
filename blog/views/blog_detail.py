from django.views.generic.base import View
from django.shortcuts import render

from category.models import Category
from blog.models import Posts

class BlogDetailView(View):
    def get(self, request, *args, **kwargs):
        print(Posts.objects.filter(slug=kwargs['blog_slug']))        
        return render(
                request,
                'blog/detail.html',
                context={
                    'categories': Category.objects.all(),
                    'post':Posts.objects.filter(slug=kwargs['blog_slug']),
                    }
                )
