from django.urls import path
from . import views

urlpatterns = [
    path('', views.TypeTranslationListView.as_view(), name='main'),
    path('translation/<type>', views.TranslationListView.as_view(), name='list_translation'),
    path('create/', views.TranslationCreateView.as_view(), name='create_translation'),
]
