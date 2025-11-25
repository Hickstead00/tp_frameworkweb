from django.forms import ModelForm
from bonnes_lectures.models import *
from django import forms

class BookForm(ModelForm):
    YEAR_CHOICES = [(year, year) for year in range(2026,1975, -1)]
    year = forms.TypedChoiceField(
        choices=YEAR_CHOICES,
        coerce=int,
        empty_value=None,
        label="Année",
        )

    class Meta:
        model = Book
        fields = ["title", "year", "isbn", "publisher", "author"]
        labels = {
            "title": "Titre",
            "year": "Année",
            "isbn": "ISBN",
            "publisher": "Editeur",
            "author": "Auteur",
        }

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['text']


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ["name", "firstname"]
        labels = {
            "name": "Nom",
            "firstname": "Prénom",
        }