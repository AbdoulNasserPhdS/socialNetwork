from rest_framework import serializers

from account.serializers import UserSerializer
from notification.models import Notification
from post.serializers import PostSerializer
from django.utils.timesince import timesince



class NotificationSerializer(serializers.ModelSerializer):
    post = PostSerializer(read_only=True)
    created_for =  UserSerializer(read_only=True)
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = Notification
        fields = ('id','body','is_read','type_of_notification','post','created_for','created_by') 
        
        
        