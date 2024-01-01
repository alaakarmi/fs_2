from django import forms
from .models import Request

class AddRequestForm(forms.ModelForm):
    class Meta:
        model = Request

        fields = [
            "room",
            "request",
            "department",
            "status",
        ]

class UpdateRequestForm(forms.ModelForm):
    class Meta:
        model = Request

        fields = [
            "room",
            "request",
            "department",
            "status",
            "notes"
        ]