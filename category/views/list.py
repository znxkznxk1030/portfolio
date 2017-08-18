from django.views.generic.base import View
from django.shortcuts import render

from category.models import Category
from blog.models import Posts

class CategoryListView(View):
    def get(self, request, *args, **kwargs):
        category_set = Category.objects.filter(id=kwargs['category_pk'])

        if 5 == kwargs['category_pk']:
            print('same')

        print(kwargs['category_pk'])
        return render(
                request,
                'category/list.html',
                context={
                    'seleted_category_pk': int(kwargs['category_pk']),
                    'categories': Category.objects.all(),
                    'posts': Posts.objects.filter(category=category_set),
                    }
                )
