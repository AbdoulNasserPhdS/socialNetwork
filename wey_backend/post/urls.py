from django.urls import path

import uuid

from . import api


urlpatterns = [
    path('', api.post_list, name='post_list'),
    path('add/',api.add_post,name='add_post'),
    path('profile/<uuid:id>/',api.posts_by_user,name='posts_by_user'),    
    path('like/<uuid:pk>', api.like_post, name='like_post'),
    path('comment/<uuid:pk>/', api.comment_post, name='comment_post'),
    path('trends/', api.get_trends, name='get_trends')

    ]