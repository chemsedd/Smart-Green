from django import forms


class LandSuitabilityForm(forms.Form):
    temperature = forms.FloatField(
        min_value=-40,
        max_value=100,
        widget=forms.NumberInput(attrs={'placeholder': '-40 C to 100 C'})
    )

    humidity = forms.FloatField(
        min_value=0,
        max_value=100,
        widget=forms.NumberInput(attrs={'placeholder': '0% to 100%'})
    )

    precipitation = forms.FloatField(
        min_value=0,
        max_value=100,
        widget=forms.NumberInput(attrs={'placeholder': '0% to 100%'})
    )

    pressure = forms.FloatField(
        min_value=0,
        max_value=100,
        widget=forms.NumberInput(attrs={'placeholder': '0% to 100%'})
    )
