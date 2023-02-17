from django.urls import path
from .views import (
    home,
    about,
    contacts,
)

app_name = 'application'


urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
]
