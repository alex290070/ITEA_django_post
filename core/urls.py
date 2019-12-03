from django.urls import path, re_path
from core.views import (
    index_view,
    comment_list_view,
    comment_detail_view,
    post_list_view,
    post_detail_view,
    ContactUsFormView,
)

app_name = 'core'

urlpatterns = [
    #path('', index_view, name='index'),
    path('', post_list_view, name='post-list'),
    path('comments/', comment_list_view, name='comment-list'),
    path('comments/<slug>/<pk>/', comment_detail_view, name='comment'),
    path('posts/', post_list_view, name='post-list'),
    path('posts/<slug>/', post_detail_view, name='post'),
    path('contactus/', ContactUsFormView.as_view(), name='contactus'),
    # re_path(r'^posts/(?P<slug>[\w-_]+)/$', func, name='post')
]
