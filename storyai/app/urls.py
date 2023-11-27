from django.urls import path
from .views import HomePageView,AboutPageView,GenerateStoryView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('generate/', GenerateStoryView.as_view(), name='generate_story'),
]
