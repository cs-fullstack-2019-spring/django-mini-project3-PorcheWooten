from django import forms
from .models import Timecard


class NewTimecard(forms.ModelForm):
    class Meta:
        model = Timecard
        fields = '__all__'
