from django import forms
from django_select2 import forms as select2_forms
from .models import Game, Developer, Publisher, Platform

class GameForm(forms.ModelForm):
    developer = forms.ModelChoiceField(
        queryset=Developer.objects.all(),
        widget=select2_forms.Select2Widget
    )
    publisher = forms.ModelChoiceField(
        queryset=Publisher.objects.all(),
        widget=select2_forms.Select2Widget
    )
    platforms = forms.ModelMultipleChoiceField(
        queryset=Platform.objects.all(),
        widget=select2_forms.Select2MultipleWidget
    )

    class Meta:
        model = Game
        fields = [
            'title',
            'developer',
            'publisher',
            'platforms',
            'release_year',
            'price',
            'genre'
        ]