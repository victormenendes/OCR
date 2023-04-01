from django.urls import path
from .views import upload_arquivo, index

urlpatterns = [
    path('', index, name='index'),
    path('upload/', upload_arquivo, name='upload_arquivo'),
]
