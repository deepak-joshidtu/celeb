from django import forms

class NameForm(forms.Form):
    
    username = forms.CharField()
    passw = forms.CharField()