from django import forms
from .models import Book

# form to add new book
class BookForm(forms.ModelForm):
    CHOICES=(
        ('Story','story'),
        ('Novel','novel'),
        ('Fantasy','fantasy'),
        ('Historical','historical')
        )
    BookType = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    class Meta:
        model=Book
        fields="__all__"
        widgets={
            'BookName':forms.TextInput(attrs=
            {'class':'form-control'})
        }