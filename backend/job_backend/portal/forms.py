from django import forms

schoices = [('C++', 'C++'),
            ('Python', 'Python'),]

class NameForm(forms.Form):
    company = forms.CharField(label='company', max_length=100)
    city = forms.CharField(label='city', max_length=100)
    min_work_experience = forms.IntegerField(label = 'min_work_experience')
    primary_skill= forms.CharField(label='What is your primary skill?', widget=forms.RadioSelect(choices=schoices))


class SearchForm(forms.Form):
    company = forms.CharField(label='company', max_length=100)