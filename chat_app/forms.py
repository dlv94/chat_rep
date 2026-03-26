from django import forms
from .models import Chat

class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['text']
        labels = {'text': ''}
        widgets = {
            'text': forms.Textarea(attrs={
                'cols': 90,
                'rows': 10,
                'placeholder': 'Digite sua mensagem chuchu...'
            })
        }