from django import forms

from categories.models import Category
from .models import Supplier


class SuppliersForm(forms.ModelForm):

    class Meta:
        model = Supplier
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
        }
        labels = {
            'name': 'Nome',
            'description': 'Descrição'
        }
