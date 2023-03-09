from django import forms


class JobForm(forms.Form):
    title = forms.CharField(required=False, label="Title", widget=forms.TextInput(attrs={'class': 'form-control'}))
    location = forms.CharField(required=False, label="Location", widget=forms.TextInput(attrs={'class': 'form-control'}) )
    payment_start = forms.FloatField(required=False, label="Payment Start", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    payment_end = forms.FloatField(required=False, label="Payment End", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    payment_type = forms.CharField(required=False, label="Payment Type", widget=forms.TextInput(attrs={'class': 'form-control'}))
    employment_type = forms.CharField(required=False, label="Employment Type", widget=forms.TextInput(attrs={'class': 'form-control'}))
    start_date = forms.DateField(required=False, label='Start Date', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    end_date = forms.DateField(required=False, label='Start Date', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
