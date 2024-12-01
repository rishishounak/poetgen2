from django.urls import path
from .views import PoetryGeneratorView

urlpatterns = [
    path('generate/', PoetryGeneratorView.as_view(), name='generate_poetry'),
]
