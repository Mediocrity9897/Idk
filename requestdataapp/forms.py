from django import forms

class UserBioForm(forms.Form):
    name = forms.CharField(label="Your name")
    age = forms.IntegerField(label="Your age")
    bio = forms.CharField(label="Biography")
