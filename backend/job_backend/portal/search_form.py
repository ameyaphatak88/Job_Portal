from django import forms

class SearchForm(forms.Form):
    company = forms.CharField(label='company', max_length=100)