from django.conf.urls import url

from category.views.list import *

urlpatterns = [
        url(r'^(?P<category_pk>\d+)/$', CategoryListView.as_view(), name='list'),
]
