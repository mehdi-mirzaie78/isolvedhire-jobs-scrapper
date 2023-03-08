from django import forms


class JobForm(forms.Form):
    title = forms.CharField(required=False, max_length=120, label="Title", widget=forms.TextInput(attrs={'class': 'form-control'}))
    start_date = forms.DateField(required=False, label='Start Date', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    end_date = forms.DateField(required=False, label='Start Date', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
