from django import forms
from ChildCares.models import ChildCare

class reviewForm(forms.Form):
    print(ChildCare.objects.all())
    childcare = forms.ModelChoiceField(queryset=ChildCare.objects.all())
    reviewer = forms.CharField(max_length=50)
    review = forms.CharField(widget=forms.Textarea)
    star = forms.IntegerField()