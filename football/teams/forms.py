from django import forms


class TakeControlForm(forms.Form):
    team_id = forms.IntegerField(widget=forms.HiddenInput())
