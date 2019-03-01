from django import forms
from .models import Timecard


class NewTimecard(forms.ModelForm):
    class Meta:
        model = Timecard
        fields = ['name','school','subject','hours','dateOfWork']
