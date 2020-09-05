from django.db import forms


class Todoform(forms.Form):
    text = forms.CharField(max_length=40)

    