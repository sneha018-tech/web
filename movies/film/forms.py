from django import forms
from film.models import nav
class navform(forms.ModelForm):
    class Meta:
        model=nav
        fields = '__all__'
