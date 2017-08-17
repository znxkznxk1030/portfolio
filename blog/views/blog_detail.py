from django.views.generic.base import View
from django.shortcuts import render

from category.models import Category
from blog.models import Posts

import markdown

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

class BlogDetailView(View):
    def get(self, request, *args, **kwargs):
        post = Posts.objects.get(slug=kwargs['blog_slug'])
        print(post)
        return render(
                request,
                'blog/detail.html',
                context={
                    'categories': Category.objects.all(),
                    'post': post,
                    }
                )
