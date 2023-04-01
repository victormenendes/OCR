from django.urls import path
from .views import upload_arquivo

urlpatterns = [
    path('upload/', upload_arquivo, name='upload_arquivo'),
]
