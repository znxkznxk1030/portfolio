from django.shortcuts import render

from category.models import Category
from blog.models import Posts

def home(request):
    return render(
            request,
            'index.html',
            {'categories' : Category.objects.all(),
                'blogs' : Posts.objects.all()},
            )
