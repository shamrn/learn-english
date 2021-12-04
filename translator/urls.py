from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', login_required(TemplateView.as_view(template_name="translator/main.html")), name='main'),
    path('translation/<type>/', views.TranslationListView.as_view(), name='list'),
    path('create/', views.TranslationCreateView.as_view(), name='create'),
    path('update/<pk>/', views.TranslationUpdateView.as_view(), name='update'),
    path('delete/<pk>/', views.translation_delete, name='delete')
]
