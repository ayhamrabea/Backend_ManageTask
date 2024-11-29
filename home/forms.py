from django import forms
from . import models


atrs = {'class' : 'form-control'}

class ProjectCreateForm(forms.ModelForm):
    
    class Meta:
        model = models.Project
        fields = ('category', 'title' ,'description')
        widgets = {
            'category': forms.Select(attrs=atrs),
            'title' : forms.TextInput(attrs=atrs),
            'description': forms.Textarea(attrs=atrs)
        }



class ProjectUpdateForm(forms.ModelForm):
    
    class Meta:
        model = models.Project
        fields = ('category', 'title' ,'status')
        widgets = {
            'category': forms.Select(attrs=atrs),
            'title' : forms.TextInput(attrs=atrs),
            'status': forms.Select(attrs=atrs)
        }

