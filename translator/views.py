from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from translator.models import Translation
from .forms import TranslationForm


class TranslationBaseView(SuccessMessageMixin, LoginRequiredMixin):
    """Базовый класс для перевода"""

    model = Translation


# class TypeTranslationView(TranslationBaseView, ListView):
#     """Главная страница"""
#
#     template_name = 'translator/main.html'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     """Добавляет в контекст типы переводов ( слова или текст )"""
    #
    #     context = super(TypeTranslationListView, self).get_context_data(**kwargs)
    #     context['types'] = Translation.get_types()
    #
    #     return context


class TranslationListView(TranslationBaseView, ListView):
    """Список переводов"""

    template_name = 'translator/list_translation.html'
    context_object_name = 'translations'

    def get_queryset(self):
        """Список переводов определенного типа"""

        return Translation.objects.by_type(self.kwargs['type'])


class TranslationCreateView(TranslationBaseView, CreateView):
    """Создание перевода"""

    template_name = 'translator/create_translation.html'
    form_class = TranslationForm
    success_message = 'Перевод успешно добавлен.'

    def get_success_url(self):
        """Перенаправление исходя из действий пользователя"""

        return (reverse_lazy('main') if 'exit' in self.get_form_kwargs()['data'] else
                reverse_lazy('create'))

class TranslationUpdateView(TranslationCreateView, UpdateView):
    """Изменение перевода"""

    form_class = TranslationForm
    template_name = 'translator/update_translation.html'
    success_message = 'Перевод успешно изменён.'

    def get_success_url(self):
        """Перенаправление на предыдущую страницу"""

        return reverse_lazy(
            'list', kwargs={'type':self.get_form_kwargs()['data']['translation_type']}
        )

def translation_delete(request, pk):
    """Удаление перевода"""

    translation = Translation.objects.get(pk=pk)
    translation.delete()

    return redirect('list', type=translation.translation_type)
