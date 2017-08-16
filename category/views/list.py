from django.views.generic.base import View
from django.shortcuts import render

from category.models import Category
from blog.models import Posts

class CategoryListView(View):
    def get(self, request, *args, **kwargs):
        print(kwargs['slug'])
        category_set = Category.objects.filter(slug=kwargs['slug'])

        return render(
                request,
                'category/list.html',
                context={
                    'seleted_category_slug': kwargs['slug'],
                    'categories': Category.objects.all(),
                    'posts': Posts.objects.filter(category=category_set),
                    }
                )
