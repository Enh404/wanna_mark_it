from django import forms
from games.models import GameMark, Profile


class GameMarkForm(forms.ModelForm):
    class Meta:
        model = GameMark
        fields = ('comment', 'game', 'mark')

        def clean_text(self):
            data = self.cleaned_data['comment']
            if data == '':
                raise forms.ValidationError('Обязательное для заполнения поле')
            return data


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('about', 'profile_img')
