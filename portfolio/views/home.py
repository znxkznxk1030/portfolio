from django.shortcuts import render

from category.models import Category

def home(request):
    return render(
            request,
            'index.html',
            {'categories' : Category.objects.all()},
            )
