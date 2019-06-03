from django.urls import path
from . import views

urlpatterns = [
    path('api/applications/', views.model_form_upload ),
]