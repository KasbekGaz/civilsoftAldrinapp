from django.urls import path
from .views import PersonalList


urlpatterns = [
    path('personal/', PersonalList.as_view(), name='personal')
]
