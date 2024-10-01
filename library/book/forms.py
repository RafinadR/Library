from django import forms
from .models import Book
from author.models import Author


class BookForm(forms.ModelForm):
    new_author = forms.CharField(
        label="New Author (name, patronymic, surname through a space)", required=False
    )

    authors = forms.ModelMultipleChoiceField(
        queryset=Author.objects.all(),
        widget=forms.SelectMultiple(attrs={'size': '10'}),
        label="Authors",
        required=False
    )
    class Meta:
        model = Book
        fields = ["name", "description", "count", "authors"]