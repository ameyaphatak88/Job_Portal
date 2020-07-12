from django import forms

class NameForm(forms.Form):
    company = forms.CharField(label='company', max_length=100)