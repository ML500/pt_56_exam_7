from django import forms

from webapp.models import Poll, Choice, Answer


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['text']


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['text']


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['choice']
        widgets = {'choice': forms.RadioSelect}

    def __init__(self, poll_choices, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['choice'].queryset = poll_choices
        self.fields['choice'].empty_label = None
