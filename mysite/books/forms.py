from django import forms


class CreateBookForm(forms.Form):
    title = forms.CharField(max_length=100)
    author = forms.CharField()
    publisher = forms.CharField()
    category = forms.CharField()
    publication_date = forms.DateField(required=False)
