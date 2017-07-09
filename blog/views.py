from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request, os.path.join(BASE_DIR, '/blog/post_list.html') , {})

