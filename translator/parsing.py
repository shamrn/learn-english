from typing import Union

import requests
from bs4 import BeautifulSoup

from django.conf import settings


def get_transcription(word: str) -> Union[None, str]:
    """Парсинг транскрипции слова"""

    transcription = None

    html_data = parsing_html(word)
    if html_data:
        items = html_data.findAll('span', class_='transcription')
        if items: transcription = items[0].get_text()  # NOQA

    return transcription


def parsing_html(word: str) -> Union[None, BeautifulSoup]:
    """Парсинг html страницы с ресурса 'wooordhunt.ru' """

    html_data = None

    response = requests.get(settings.URL_WOOORDHUNT % word)
    if response.status_code == 200:
        html_data = BeautifulSoup(response.content, 'html.parser')

    return html_data
