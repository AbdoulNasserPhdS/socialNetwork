from django.forms import ModelForm

from chat.models import ConversionMessage

class ConversionMessageForm(ModelForm):
    class Meta :
        model = ConversionMessage
        fields = {'content'}