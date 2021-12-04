from django import forms

from .models import Translation


class TranslationForm(forms.ModelForm):
    """Форма для создания и изменение модели Translation"""

    class Meta:
        model = Translation
        fields = ['translation_type', 'english_version', 'russian_version', 'transcription']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {
                    'class': "form-field",
                    'placeholder': f"{self.fields[f'{field}'].label}"
                }
            )
