from django.db import models


class Translation(models.Model):
    """Модель Translation"""

    class TranslationType(models.IntegerChoices):
        WORD: int = 0, 'Word'
        Sentence: int = 1, 'Sentence'

    translation_type = models.PositiveSmallIntegerField('Тип перевода',
                                                        choices=TranslationType.choices)
    english_version = models.CharField('Английский вариант', max_length=250)
    russian_version = models.CharField('Русский вариант', max_length=250)
    transcription_version = models.CharField('Транскрипция', max_length=250,
                                             null=True, blank=True)
    pronunciationd = models.FileField('Произношение', upload_to='pronunciationd',
                                      null=True, blank=True)
    created = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Перевод слова и предложения'
        verbose_name_plural = 'Переводы слов и предложений'

    def __str__(self):
        return f'{self.english_version} - {self.russian_version}'
