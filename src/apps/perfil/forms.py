# -*- coding: utf-8 -*-
from django import forms
from models import Perfil

class PerfilForm(forms.ModelForm):
    apellidos = forms.CharField(label=u'Apellidos', max_length=255)
    nombres   = forms.CharField(label=u'Nombres', max_length=255)
    email     = forms.EmailField(label=u'E-Mail')
    ingresar  = forms.BooleanField(label=u'¿Puede ingresar al admin?',required=False)

    class Meta:
        model = Perfil

    def __init__(self, *args, **kw):
        super(PerfilForm, self).__init__(*args, **kw)
        self.fields.insert(3,'apellidos',forms.CharField(widget=forms.TextInput(attrs={'class':'vTextField'})))
        self.fields.insert(4,'nombres',forms.CharField(widget=forms.TextInput(attrs={'class':'vTextField'})))
        self.fields.insert(5,'email',forms.EmailField(widget=forms.TextInput(attrs={'class':'vTextField'})))
        if self.instance.user_id is not None:
            self.fields['nombres'].initial = self.instance.user.first_name
            self.fields['apellidos'].initial = self.instance.user.last_name
            self.fields['email'].initial = self.instance.user.email
            self.fields['ingresar'].initial = self.instance.user.is_staff
