from django.views.generic.base import View
from django.shortcuts import render

from category.models import Category
from blog.models import Posts

class BlogDetailView(View):
    def get(self, request, *args, **kwargs):
        post = Posts.objects.get(id=kwargs['blog_pk'])
        return render(
                request,
                'blog/detail.html',
                context={
                    'categories': Category.objects.all(),
                    'post': post,
                    }
                )
