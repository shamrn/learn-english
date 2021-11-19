from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, ListView

from translator.models import Translation


class TranslationBaseView(SuccessMessageMixin, LoginRequiredMixin):
    """Базовый класс для перевода"""

    fields = '__all__'
    model = Translation


class TypeTranslationListView(TranslationBaseView, ListView):
    """Главная страница"""

    template_name = 'translator/main.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        """Добавляет в контекст типы переводов ( слова или текст )"""

        context = super(TypeTranslationListView, self).get_context_data(**kwargs)
        context['types'] = Translation.get_types()

        return context


class TranslationListView(TypeTranslationListView):
    """Список переводов"""

    template_name = 'translator/list_translation.html'


class TranslationCreateView(TranslationBaseView, CreateView):
    """Создание перевода"""

    fields = ('translation_type', 'english_version', 'russian_version', 'transcription_version')
    template_name = 'translator/create_translation.html'
    success_message = 'Перевод успешно добавлен.'

    def get_success_url(self, **kwargs):
        """Исходя из действий пользователь, перенаправляем его на главную страницу или
        оствляем на текущей
        """

        return 'main' if self.get_form_kwargs()[
                             'action'] == 'exit' else '.'  # TODO доделат эту поеботу
