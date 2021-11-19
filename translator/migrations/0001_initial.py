# Generated by Django 3.2.9 on 2021-11-19 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('translation_type', models.PositiveSmallIntegerField(choices=[(0, 'Word'), (1, 'Sentence')], verbose_name='Тип перевода')),
                ('english_version', models.CharField(max_length=250, verbose_name='Английский вариант')),
                ('russian_version', models.CharField(max_length=250, verbose_name='Русский вариант')),
                ('transcription_version', models.CharField(blank=True, max_length=250, null=True, verbose_name='Транскрипция')),
                ('pronunciationd', models.FileField(blank=True, null=True, upload_to='pronunciationd', verbose_name='Произношение')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Перевод слова и предложения',
                'verbose_name_plural': 'Переводы слов и предложений',
            },
        ),
    ]
