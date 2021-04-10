from django import forms
from .models import Questboard, Questcard

class QuestboardForm(forms.ModelForm):

    class Meta:
        model = Questboard
        fields = "__all__"


class QuestcardForm(forms.ModelForm):

    class Meta:
        model = Questcard
        fields = "name", "description", "stars", "questboard"


class QuestcardForm_(forms.ModelForm):

    class Meta:
        model = Questcard
        exclude = ("questboard",)



