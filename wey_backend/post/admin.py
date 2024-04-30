from django.contrib import admin

# Register your models here.
from account.models import User
from post.models import Post

admin.site.register(User)
admin.site.register(Post)
