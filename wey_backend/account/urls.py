from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import api

urlpatterns = [
    path('me/', api.me, name='me'),
    path('signup/', api.signup, name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('logout/', api.logout, name='token_refresh'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('friends/<uuid:id>/',api.get_friends,name='get_friends'),
    path('friends/all_request/',api.get_friends_requests,name='get_friends_requests'),
    path('friends/request/<uuid:id>/',api.send_friend_resquest,name='send_friend_resquest'),
    path('friends/<uuid:id>/<str:status>/',api.handle_request,name='handle_request')        
]
