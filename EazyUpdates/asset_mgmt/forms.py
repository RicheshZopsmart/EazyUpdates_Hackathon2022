from ast import Assert
from .models import Asset
from django import forms

class Asset_replace_form(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['Name','SerialID','Description']