
from django import forms
from .models import Message
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit



class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('name', 'email', 'subject', 'message',)
        
        labels = {
            'name':'',
            'email':'',
            'subject':'',
            'message':'',
        }
        
        widgets = {
            'name' : forms.TextInput(attrs={'placeholder':'Your name'}),
            'email': forms.EmailInput(attrs={'placeholder':'Your email'}),
            'subject': forms.TextInput(attrs={'placeholder':'Subject'}),
            'message': forms.Textarea(attrs={'placeholder':'Message'}),
        }
        
              
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['name'].widget.attrs['placeholder'] = self.instance.placeholder