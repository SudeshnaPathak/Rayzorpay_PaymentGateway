
from django.urls import path, include
from .views import home, success, view

urlpatterns = [
   path('', view, name='view'),
   path('success/', success, name='success'),
   path('payment/', home, name='home')
]