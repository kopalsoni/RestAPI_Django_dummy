from django.urls import path
from .views import index


urlpatterns = [
    path('', index),    # here index is the function name we created in views.py
    path('join', index),
    path('create', index)
]
