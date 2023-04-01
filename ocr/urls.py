from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_image, name='upload_image'),
    path('analysis-results/', views.analysis_results, name='analysis_results'),
]