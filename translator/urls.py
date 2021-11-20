from django.urls import path
from . import views

urlpatterns = [
    path('', views.TypeTranslationListView.as_view(), name='main'),
    path('translation/<type>', views.TranslationListView.as_view(), name='list'),
    path('create/', views.TranslationCreateView.as_view(), name='create'),
    path('update/<pk>', views.TranslationUpdateView.as_view(), name='update'),
    path('delete/<pk>', views.translation_delete, name='delete')
]
