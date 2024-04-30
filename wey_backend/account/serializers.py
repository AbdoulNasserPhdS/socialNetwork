from rest_framework import serializers
from .models import FriendshipRequest, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email','posts_count']
        

class FriendshipRequestSerializer(serializers.ModelSerializer):
    created_by=UserSerializer(read_only=True)
    created_for=UserSerializer(read_only=True)
    class Meta:
        model= FriendshipRequest
        fields = ['id','created_by','created_at_formatted','created_for']