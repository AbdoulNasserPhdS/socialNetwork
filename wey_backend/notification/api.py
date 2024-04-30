from rest_framework.decorators import api_view

from django.http import JsonResponse

from notification.models import Notification
from notification.serializer import NotificationSerializer

@api_view(['POST'])
def read_notification(request,id):
    try:
        notification = Notification.objects.get(pk=id)
        if notification:
            notification.is_read=True
            notification.save()
            return JsonResponse({'notification':NotificationSerializer(notification).data})
    except Exception as ex:
        return JsonResponse({'error':str(ex)})
    
    
@api_view(['GET'])
def get_list_notifications(request):
    try:
        user = request.user
        if user:
            notifications=Notification.objects.filter(created_for=user)
            return JsonResponse({'notifications':NotificationSerializer(notifications,many=True).data})
    except Exception as ex:
        return JsonResponse({'error':str(ex)})
    