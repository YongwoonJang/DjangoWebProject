from django import forms
from django.forms import ModelForm
from django.db import models
from .models import Content

class SourceForm(ModelForm):

    class Meta:
        model = Content
        fields = ('title','csscontents','htmlcontents','javascriptcontents')
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'csscontents' : forms.Textarea(attrs={'class':'form-control', 'rows':6},),
            'htmlcontents' : forms.Textarea(attrs={'class':'form-control', 'rows':6}),
            'javascriptcontents' : forms.Textarea(attrs={'class':'form-control', 'rows':6})
        }
