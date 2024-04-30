from django.http import JsonResponse
from rest_framework.decorators import api_view

from account.models import User
from chat.forms import ConversionMessageForm
from chat.models import Conversion, ConversionMessage

from chat.serializer import ConversionSerializer,ConversionMessageSerializer
from django.core.exceptions import ObjectDoesNotExist


@api_view(['GET'])
def get_conversion_list(request):
    try : 
        user = request.user
        
        if user :
            conversions_created_by_user = Conversion.objects.filter(created_by=user)
            conversions_with_user = Conversion.objects.filter(with_user=user)
            all_conversions = conversions_created_by_user | conversions_with_user
            
            conversionSerializer = ConversionSerializer(all_conversions,many=True)
            
            return JsonResponse({'conversions':conversionSerializer.data})
        
    except ObjectDoesNotExist:
            return JsonResponse({'message':'user not exist'})
    except Exception as ex :
            return JsonResponse({'message':str(ex)})

        

        
    

    
        
    return JsonResponse({})

    
    
@api_view(['GET'])
def get_conversion_details(request, user_id):
    try:
        user = request.user
        with_user = User.objects.get(pk=user_id)
        
        if user != with_user:
            
            try:
                conversion = Conversion.objects.get(created_by=user, with_user=with_user)
            except ObjectDoesNotExist:
                try:
                    conversion = Conversion.objects.get(created_by=with_user, with_user=user)
                except ObjectDoesNotExist:
                    conversion = Conversion.objects.create(created_by=user, with_user=with_user)
                
            messages = ConversionMessage.objects.filter(conversion=conversion)
        
            conversion_serializer = ConversionSerializer(conversion)
            message_serializer = ConversionMessageSerializer(messages,many=True)

            return JsonResponse({'conversion': conversion_serializer.data, 'messages': message_serializer.data})
        else:
            return JsonResponse({'message': 'Error retrieving conversion details'})
    except ObjectDoesNotExist:
        return JsonResponse({'message': 'User not found'})
    except Exception as e:
        return JsonResponse({'message': str(e)})


  
    

   
@api_view(['POST'])
def send_message(request,conversion_id):
    
    try: 
        if request.method =='POST':
            conversionMessageForm = ConversionMessageForm(request.data)
            
            if conversionMessageForm.is_valid() : 
                conversion = Conversion.objects.get(pk=conversion_id)
                user = request.user
                
                if (user == conversion.created_by or user == conversion.with_user) :
                    conversionMessage =conversionMessageForm.save(commit=False)
                    conversionMessage.conversion = conversion
                    
                    if request.user == conversion.created_by :
                        conversionMessage.sent_to=conversion.with_user
                    else :
                        conversionMessage.sent_to=conversion.created_by

                        
                    conversionMessage.save()
                    
                    conversionMessageSerializer = ConversionMessageSerializer(conversionMessage)
                    
                    return JsonResponse({'conversionMessage':conversionMessageSerializer.data})
                else:
                    return JsonResponse({'message': 'Error sending message'})
    except Exception as e:
        return JsonResponse({'message': str(e)})         

    


