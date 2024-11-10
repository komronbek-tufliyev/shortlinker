from django import forms
from .models import UrlShortener

class UrlShortenerForm(forms.ModelForm):
    url = forms.URLField(widget=forms.URLInput(attrs={"class": "form-control form-control-lg", "placeholder":"Your URL to shorten"}))

    class Meta:
        model = UrlShortener
        fields = ('url', )