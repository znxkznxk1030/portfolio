from django.conf.urls import url
from blog.views.blog_detail import *
from blog.views.blog_new import BlogNewView

urlpatterns =[
    url(r'^(?P<blog_pk>\d+)/$', BlogDetailView.as_view(), name='post_detail'),
    url(r'^new/$', BlogNewView.as_view(), name='post_new'),
]
