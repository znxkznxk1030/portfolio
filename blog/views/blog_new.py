from django.shortcuts import render
from django.views.generic.base import View


from category.models import Category
from blog.models import Posts

class BlogNewView(View):
    def get(self, request, *args, **kwargs):

        return render(
                request,
                'blog/new.html',
                context={
                    'categories': Category.objects.all(),
                    }
                )
