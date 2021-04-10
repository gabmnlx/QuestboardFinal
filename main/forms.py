from django import forms
from .models import *

class QuestboardForm(forms.ModelForm):

    class Meta:
        model = Questboard
        fields = "__all__"


class QuestcardForm(forms.ModelForm):
    is_for_everyone = forms.BooleanField(widget=forms.CheckboxInput, required=False, label="Is this quest for everyone?")
    class Meta:
        model = Questcard
        fields = "name", "description", "stars", "questboard", "is_for_everyone"


class addPersonForm(forms.ModelForm):

    class Meta:
        model = addPerson
        fields = "__all__"


class addPerson1Form(forms.ModelForm):

    class Meta:
        model = addPerson1
        fields = "__all__"

class addPerson2Form(forms.ModelForm):

    class Meta:
        model = addPerson2
        fields = "__all__"

class addPerson3Form(forms.ModelForm):

    class Meta:
        model = addPerson3
        fields = "__all__"


class addPersonOneForm(forms.ModelForm):

    class Meta:
        model = addPersonOne
        fields = "__all__"

class addPersonTwoForm(forms.ModelForm):

    class Meta:
        model = addPersonTwo
        fields = "__all__"

class addPersonThreeForm(forms.ModelForm):

    class Meta:
        model = addPersonThree
        fields = "__all__"



