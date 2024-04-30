import uuid
from django.db import models

from account.models import User
from django.utils.timesince import timesince

# Create your models here.
class Conversion(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    created_by=models.ForeignKey(User,related_name='created_by',on_delete=models.CASCADE)
    with_user=models.ForeignKey(User,related_name='with_user',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('created_by', 'with_user')
        
    def created_at_formatted_comment(self):
      return timesince(self.created_at)
  
  
class ConversionMessage(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    conversion=models.ForeignKey(Conversion,on_delete=models.CASCADE)
    content =models.TextField(blank=True, null=True)
    sent_to = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def created_at_formatted_comment(self):
      return timesince(self.created_at)

    
     