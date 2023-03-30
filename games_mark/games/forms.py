from django import forms
from django.shortcuts import get_object_or_404
from games.models import Game, GameMark, Profile


class GameMarkForm(forms.ModelForm):
    my_field_choices = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    )
    mark = forms.ChoiceField(choices=my_field_choices, label='Оценка')
    class Meta:
        model = GameMark
        fields = ('game', 'comment', 'mark')
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 15, 'cols': 70})
        }

    def clean_comment(self):
        data = self.cleaned_data['comment']
        if data == '':
            raise forms.ValidationError('Обязательное для заполнения поле')
        return data


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('about', 'profile_img')
