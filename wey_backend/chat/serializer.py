from rest_framework import serializers

from account.serializers import UserSerializer
from chat.models import Conversion, ConversionMessage

class ConversionSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    with_user = UserSerializer(read_only=True)
    class Meta:
        model = Conversion
        fields = ('id','created_by','with_user','created_at_formatted_comment')
        
class ConversionMessageSerializer(serializers.ModelSerializer):
    conversion = ConversionSerializer(read_only=True)
    sent_to = UserSerializer(read_only=True)
    class Meta:
        model = ConversionMessage
        fields = ('id','content','created_at_formatted_comment','conversion','sent_to')
        
    