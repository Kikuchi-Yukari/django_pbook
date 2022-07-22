from unicodedata import category
from django import forms
from .models import Pbook
import os

#VALID_EXTENSIONS = ['.jpg']

class PbookForm(forms.ModelForm):
    class Meta:
        model = Pbook
        fields = ['item','category','comment','collection_date','pbook_image']
        widgets = {
            'item': forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.TextInput(attrs={'class':'form-control'}),
            'comment': forms.TextInput(attrs={'class':'form-control'}),
            'collection_date': forms.DateInput(attrs={'class':'form-control'}),
            #'pbook_image': forms.Input(attrs={'class':'form-control'}),
        }


