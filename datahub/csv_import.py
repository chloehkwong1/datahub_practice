from django import forms

class BaseCSVImportForm(forms.Form):
    """Form used for loading a CSV file in the admin site."""