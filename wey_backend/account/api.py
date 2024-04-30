from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes,permission_classes

from account.models import FriendshipRequest, User
from account.serializers import FriendshipRequestSerializer, UserSerializer
from .forms import SignupForm
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.response import Response



@api_view(['GET'])
def me(request):
    return JsonResponse(
        {
            'id': request.user.id,
            'name': request.user.name,
            'email': request.user.email,
        }
    )


@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def signup(request):
    data=request.data
    message='success'
    
    form=SignupForm({
        'email':data.get('email'),
        'name':data.get('name'),
        'password1':data.get('password1'),
        'password2':data.get('password2'),
    })

    if form.is_valid():
        user = form.save()
        user.is_active = True
        user.save()
        # url = f'{settings.WEBSITE_URL}/activateemail/?email={user.email}&id={user.id}'

        # send_mail(
        #     "Please verify your email",
        #     f"The url for activating your account is: {url}",
        #     "noreply@wey.com",
        #     [user.email],
        #     fail_silently=False,
        # )
    else:
        message = form.errors.as_json()
    print(message)
    
    return JsonResponse({'message': message}, safe=True)




@api_view(['POST'])

def logout(request):
    try:
        refresh_token = request.data['refresh_token']
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response(status=status.HTTP_205_RESET_CONTENT)
    except Exception as e:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def handle_request(request,id,status):
    
    if request.method=='POST':
        
        friendshipRequest = FriendshipRequest.objects.get(pk=id)
        
        self_user = request.user
        created_for= friendshipRequest.created_for
        created_by= friendshipRequest.created_by

        if  self_user == created_for :
            
            if status =="accepted":
                self_user.friends.add(created_by)
                self_user.save()
                
                created_by.friends.add(self_user)
                created_by.save()                    
                    
            friendshipRequest.status=status
            friendshipRequest.save()
            
        fpRequestSerializer=FriendshipRequestSerializer(friendshipRequest)
        friendSerializer = UserSerializer(created_by)

        return JsonResponse({'message' :'accepted','friend':friendSerializer.data,'friendshipRequest':fpRequestSerializer.data})

    return JsonResponse({'message':'friendship handle error'})


@api_view(['POST'])
def send_friend_resquest(request,id):
    
    if request.method=='POST':
        
        user = User.objects.get(pk=id)
        user2 = request.user
        
    
        check = FriendshipRequest.objects.filter(created_for=user2).filter(created_by=user)
        check2 = FriendshipRequest.objects.filter(created_for=user).filter(created_for=user2)
        
        print(check,'_________',check2)
        
        if not (check or check2): 
            request_object = FriendshipRequest.objects.create(created_by=user2,created_for=user)
            request_object_serializer=FriendshipRequestSerializer(request_object)
            return JsonResponse({'request':request_object_serializer.data,'message':'request send !'},status=200)
        else:
            print('deja envoyé')
            return JsonResponse({'message':'You are already send a request !'})
        
        

@api_view(['GET'])
def get_friends(request,id): 
    user = User.objects.get(pk=id)
    friendsSerializer = UserSerializer(user.friends,many=True)   
    return JsonResponse({'friends':friendsSerializer.data})


@api_view(['GET'])
def get_friends_requests(request):
    requests= FriendshipRequest.objects.filter(created_for=request.user,status='sent')
    
    if requests :
        requestsSerializer = FriendshipRequestSerializer(requests,many=True)
        return JsonResponse({'message':"You have friend request !", 'data':requestsSerializer.data})
    else:
        return JsonResponse({'message':"You don't have yet a friend request !"})    
    # return JsonResponse({'message':'get_friends_request'})



@api_view(['GET'])
def get_friends_requests_send(request):
    return JsonResponse({'message':'get_friends_requests_send'})




