from django import forms
from django.shortcuts import get_object_or_404
from games.models import Game, GameMark, Profile


class GameMarkForm(forms.ModelForm):
    class Meta:
        model = GameMark
        fields = ('comment', 'game', 'mark')

    def clean_comment(self):
        data = self.cleaned_data['comment']
        if data == '':
            raise forms.ValidationError('Обязательное для заполнения поле')
        return data


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('about', 'profile_img')
