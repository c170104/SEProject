from django import forms

class contactForm(forms.Form):
    fname = forms.CharField(max_length=50)
    lname = forms.CharField(max_length=50)
    subject = forms.CharField(max_length=50)
    email = forms.EmailField()
    enquiry = forms.CharField(max_length=500)
