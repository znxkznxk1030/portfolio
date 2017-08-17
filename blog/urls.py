from django.conf.urls import url
from blog.views.blog_detail import *

urlpatterns =[
    url(r'^(?P<blog_slug>[-\w]+)/$', BlogDetailView.as_view(), name='post_detail'),
]
