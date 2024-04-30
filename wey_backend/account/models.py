from datetime import timezone,datetime
import uuid
from django.db import models
from django.utils.timesince import timesince


from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,UserManager, PermissionsMixin

class CustomUserManager(UserManager):
    def _create_user(self,name,email, password,**extra_fields):
        if not email:
            raise ValueError("The email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self,name=None, email=None,password=None, **extra_fields):
        extra_fields.setdefault('is_staff',False)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(name,email,password,**extra_fields)
    
    def create_superuser(self,name=None, email=None,password=None, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(name,email,password,**extra_fields)
    
    
class User(AbstractBaseUser,PermissionsMixin):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    email =models.EmailField(blank=True,default='',unique=True)
    name = models.CharField(max_length=255, blank=True,default='')
    avatar =models.ImageField(upload_to='avatars',blank=True,null=True)
    
    friends=models.ManyToManyField('self')
    friends_count=models.IntegerField(default=0)

    is_active = models.BooleanField(default=True)
    is_superuser= models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    posts_count=models.IntegerField(default=0)

    date_joined =models.DateTimeField(default=datetime.now())
    last_login = models.DateTimeField(blank=True,null=True)
    
    objects = CustomUserManager()

    USERNAME_FIELD= 'email'
    EAMIL_FIELD = 'email'
    REQUIRED_FIELDS = []
        
class FriendshipRequest(models.Model):
    SENT = 'sent'
    ACCEPTED = 'accepted'
    REJECTED = 'rejected'
    
    STATUS_CHOICES = {
        (SENT,'sent'),
        (ACCEPTED,'accepted'),
        (REJECTED, 'rejected')
    }
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name="created_friendshiprequests")
    created_for = models.ForeignKey(User,on_delete = models.CASCADE, related_name="received_friendshiprequests")
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default=SENT)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def created_at_formatted(self):
      return timesince(self.created_at)
