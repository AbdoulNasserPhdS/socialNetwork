from django.urls import path
from . import api
import uuid


urlpatterns = [
    path('',api.get_conversion_list ,name='get_conversion_list'),
    path('<uuid:user_id>/',api.get_conversion_details ,name='get_conversion_details'),
    path('<uuid:conversion_id>/send/',api.send_message ,name='send_message'),
    

]
