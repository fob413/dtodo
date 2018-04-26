from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import todo_list, todo_detail

urlpatterns = {
    url(r'^todo/$', todo_list, name="create"),
    url(r'^todo/(?P<pk>[0-9]+)/$', todo_detail, name="details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
