from django import forms

from .models import todo


class todo_form(forms.ModelForm):
    class Meta:
        model=todo
        fields=['name','priority','date']
