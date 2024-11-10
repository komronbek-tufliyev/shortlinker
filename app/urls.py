from django.urls import path
from .views import home_view, redirect_url_view, about_view

urlpatterns = [
    path('', home_view, name="home"),
    path('about/', about_view, name="about"),
    path('<str:shortened_part>', redirect_url_view, name='redirect'),
]
