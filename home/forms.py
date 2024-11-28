from django import forms
from . import models


class ProjectCreateForm(forms.ModelForm):
    
    class Meta:
        model = models.Project
        fields = ('category', 'title' ,'description')
        widgets = {
            'category': forms.Select(),
            'title' : forms.Textarea(),
            'description': forms.Textarea()
        }



class ProjectUpdateForm(forms.ModelForm):
    
    class Meta:
        model = models.Project
        fields = ('category', 'title' ,'status')
        widgets = {
            'category': forms.Select(),
            'title' : forms.Textarea(),
            'status': forms.Select()
        }

