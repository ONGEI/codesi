# -*- coding: utf-8 -*-
from django.forms import ModelForm, Textarea, TextInput, HiddenInput
from models import Comentario

class ComentarioForm(ModelForm):

    class Meta:
        model = Comentario
        fields = ('objetivo', 'ciudadano','email', 'comentario')
        widgets = {
            'objetivo' : HiddenInput(attrs={'class':'input-xlarge',}),
            'ciudadano' : TextInput(attrs={'class':'input-xlarge','autofocus':'autofocus'}),
            'email': TextInput(attrs={'class':'input-xlarge',}),
            'comentario' : Textarea(attrs={'class':'input-xlarge','rows':'3',}),
        }
