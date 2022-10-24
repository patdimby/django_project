from turtle import width
from attr import fields
from django import forms
from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('name', 'email', 'subject', 'message',)
        widget = {
            # Placeholders
            'name': forms.TimeInput(attrs={'placeholder':'Your name'}),
            'email': forms.TimeInput(attrs={'placeholder':'Your email'}),
            'subject': forms.TimeInput(attrs={'placeholder':'Subject'}),
            'message': forms.TimeInput(attrs={'placeholder':'Your message'}),
        }