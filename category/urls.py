from django.conf.urls import url

from category.views.list import *

urlpatterns = [
    url(r'^(?P<slug>[-\w]+)/$', CategoryListView.as_view(), name='list'),
]
