from django.http import JsonResponse
from account.models import User

from post.serializers import PostSerializer

from account.serializers import UserSerializer
from post.models import Post
from rest_framework.decorators import api_view,permission_classes,authentication_classes


@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def search(request):
    query=request.data.get('query')
    
    posts=Post.objects.filter(body__contains=query)
    users=User.objects.filter(name__contains=query)
    
    posts_serializer=PostSerializer(posts,many=True)
    users_serializer=UserSerializer(users,many=True)

    return JsonResponse({'posts':posts_serializer.data,'users':users_serializer.data})