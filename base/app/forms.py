from django import forms
from django.contrib.auth import get_user_model
from .models import Ritual


class RitualStepForm(forms.ModelForm):
    class Meta:
        model = Ritual
        fields = ('name', 'description')