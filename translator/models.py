from typing import Union

from django.db import models

from translator.parsing import get_transcription


class TranslationManager(models.Manager):
    """Manager модели Translation"""


class TranslationQuerySet(models.QuerySet):
    """QuerySet модели Translation"""

    def by_type(self, type: int) -> Union[models.QuerySet, 'TranslationQuerySet']:  # NOQA
        """Сортировка по типоу"""

        return self.filter(translation_type=type)


class Translation(models.Model):
    """Модель Translation"""

    class TranslationType(models.IntegerChoices):
        WORD: int = 0, 'Слово'
        Sentence: int = 1, 'Предложение'

    translation_type = models.PositiveSmallIntegerField('Тип перевода',
                                                        choices=TranslationType.choices)
    english_version = models.CharField('Английский вариант', unique=True, max_length=250)
    russian_version = models.CharField('Русский вариант', max_length=250)
    transcription = models.CharField("Транскрипция", max_length=250,
                                     null=True, blank=True)
    pronunciation = models.FileField('Произношение', upload_to='pronunciation',
                                     null=True, blank=True)
    created = models.DateTimeField('Дата создания', auto_now_add=True)

    objects = TranslationManager.from_queryset(TranslationQuerySet)()

    class Meta:
        verbose_name = 'Перевод слова и предложения'
        verbose_name_plural = 'Переводы слов и предложений'

    def __str__(self):
        return f'{self.english_version} - {self.russian_version}'

    def make_transcription(self, word: str):
        """Присваиваем транскрипцию"""

        if transcription:= get_transcription(word):  # NOQA
            self.transcription = transcription
            self.save(update_fields=['transcription'])

    # @classmethod
    # def get_types(cls) -> list:
    #     """Возвращает label типов"""
    #
    #     return cls.TranslationType.labels
