from django import forms

from .models import Translation


class TranslationUpdateForm(forms.ModelForm):
    """Форма для редактирования объектов модели Translation"""

    class Meta:
        model = Translation
        fields = ['translation_type', 'english_version', 'russian_version', 'transcription']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.initial.update({'transcription': self.instance.transcription})

        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {
                    'class': "form-field",
                    'placeholder': f"{self.fields[f'{field}'].label}"
                }
            )


class TranslationCreateForm(TranslationUpdateForm):
    """Форма для создания объектов модели Translation"""

    class Meta(TranslationUpdateForm.Meta):
        model = Translation
        TranslationUpdateForm.Meta.fields.remove('transcription')
        fields = TranslationUpdateForm.Meta.fields

    def save(self, commit=True):

        instance = super().save(commit)

        if self.cleaned_data['translation_type'] == 0:
            instance.make_transcription(self.cleaned_data['english_version'])

        return instance
