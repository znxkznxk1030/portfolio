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
                    'categories': Category.objects.all(),
                    'posts': Posts.objects.filter(category=category_set),
                    }
                )
