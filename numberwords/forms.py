from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator


class NumberForm(forms.Form):
    number = forms.IntegerField(validators=[
            MaxValueValidator(1000000000),
            MinValueValidator(0)
        ])
