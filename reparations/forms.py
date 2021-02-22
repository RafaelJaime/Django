from django import forms
class ReparateForm(forms.Form):
    Motivo = forms.CharField(required = True, max_length=100, widget=forms.Textarea(attrs={"rows":5, "cols":20}))
class MReparateForm(forms.Form):
    Observaciones = forms.CharField(max_length=20, required=False, widget=forms.Textarea(attrs={"rows":5, "cols":20}))