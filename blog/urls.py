from django.conf.urls import url
from blog.views.blog_detail import *
from blog.views.blog_new import BlogNewView

urlpatterns =[
    url(r'^(?P<category_slug>[-\w]+)/(?P<blog_slug>[-\w]+)/$', BlogDetailView.as_view(), name='post_detail'),
    url(r'^new/$', BlogNewView.as_view(), name='post_new'),
]
