from django.http import JsonResponse

from account.models import User
from account.serializers import UserSerializer
from notification.models import Notification
from notification.utils import create_notification
from post.forms import CommentForm, PostAttachmentForm, PostForm
from .models import Post, PostAttachment, Trend
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


from .models import Like,Comment

from .serializers import PostAttachmentSerializer, PostSerializer, TrendSerializer
from django.core import serializers
from rest_framework import status



@api_view(['GET'])
# @permission_classes([])
# @authentication_classes([])
def post_list(request):
    
    # if request.user.id :
    #     user_ids = [request.user.id]
    
    #     user_ids = [request.user.id]

    #     for user in request.user.friends.all():
    #         user_ids.append(user.id)

    #     posts = Post.objects.filter(created_by_id__in=user_ids)
    # else :
    #     posts = Post.objects.all()
    
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    # print(serializer.data)
    return JsonResponse({'data':serializer.data})
    
    
@api_view(['POST'])
def add_post(request):    
    
    if request.method =="POST":
    
        try :
                        
            post_form = PostForm(request.POST)
            attachementForm = PostAttachmentForm(request.POST, request.FILES)

            if attachementForm.is_valid() and post_form.is_valid():

                post = post_form.save(commit=False)
                
                request.user.posts_count+=1
                
                request.user.save()
                                
                post.created_by = request.user
                post.save()

                attachement = attachementForm.save(commit=False)
                attachement.created_by = request.user
                attachement.save()

                post.attachments.add(attachement)
                post.save()
                
                postSerialize = PostSerializer(post)
                return JsonResponse({'post': postSerialize.data}, status=200)
            else:
                post = post_form.save(commit=False)
                post.created_by = request.user
                post.save()
                postSerialize = PostSerializer(post)
                return JsonResponse({'post': postSerialize.data}, status=200)

        except Exception as e :
            print(str(e))
            return JsonResponse({'errors':str(e)})            

@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def posts_by_user(request,id):
        
    user=User.objects.get(pk=id)    
    user_serializer=UserSerializer(user)

    posts = Post.objects.filter(created_by_id=id)
    posts_serializer=PostSerializer(posts,many=True)

    return JsonResponse({'data':posts_serializer.data,'user':user_serializer.data})


@api_view(['POST'])
def like_post(request,pk):
    
    try:
        
        post=Post.objects.get(pk=pk)
    
        # search if user already like the post
        likes = post.like.all()

        
        result = likes.filter(created_by=request.user)
        # if yes dislike and if no like
        if result.exists():
            like_to_delete = result.first()
            like_to_delete.delete()
            post.likes_count -= 1
        else:
            like = Like.objects.create(created_by=request.user)
            post.likes_count=post.likes_count+1;
            post.like.add(like)
                
        post.save()
        
        create_notification(request, 'post_like', post_id=post.id)
            
        postSerializer=PostSerializer(post)
        
            
        return JsonResponse({'post':postSerializer.data})

    except Exception as ex:
        print(str(ex))
        JsonResponse({'error':str(ex)})
    

   
    
@api_view(['POST'])
def comment_post(request,pk):
    
    if request.method=="POST":

        comment_form=CommentForm(request.data)
        
        if comment_form.is_valid():
            comment=comment_form.save(commit=False)
            comment.created_by=request.user
            # comment_form.save()
            comment.save()
            
            post=Post.objects.get(pk=pk)
            post.comments.add(comment)
            post.comments_count+=1
            
            post.save()
            
            postSerializer=PostSerializer(post)   
            
            # print(postSerializer.data
                     
            return JsonResponse({'post':postSerializer.data})

    return JsonResponse({'message':'Add comment error.'})


@api_view(['GET'])
def get_trends(request):       
    trendSerializer = TrendSerializer(Trend.objects.all(),many=True) 
    return JsonResponse({'trends':trendSerializer.data})
    