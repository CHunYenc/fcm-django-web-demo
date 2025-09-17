from django.urls import path
from . import views

urlpatterns = [
    path('firebase-config.js', views.firebase_config_script, name='firebase-config'),
]
