# pages/urls.py
from django.urls import path
from .views import homePageView, aboutPageView, alexPageView, results, homePost

urlpatterns = [
    path('', homePageView, name='home'),
    path('about/', aboutPageView, name='about'),
    path('alex/', alexPageView, name='alex'),
    path('homePost/', homePost, name='homePost'),
    path('results/<int:choice>/<str:gmat>/', results, name='results'),

]
