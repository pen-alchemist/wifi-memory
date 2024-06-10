from django import forms


class WifiScannerForm(forms.Form):
    """Form for entering an interface name."""
    interface = forms.CharField(max_length=20, label="Network Interface")


class WifiSignalForm(forms.Form):
    """Form for entering an interface name."""
    interface = forms.CharField(max_length=20, label="Network Interface")
