
from django.urls import path
from notification import api
import uuid


urlpatterns = [
    path('',api.get_list_notifications,name='get_list_notifications'),
    path('read/<uuid:id>',api.read_notification,name='read_notification')
]