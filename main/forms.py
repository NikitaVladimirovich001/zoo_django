from django import forms
from main.models import KommentModel


class KommentForm(forms.ModelForm):

    class Meta():
        model = KommentModel
        fields = ("name",'text')