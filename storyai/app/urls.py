from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('generate/', GenerateStoryView.as_view(), name='generate_story'),
    path('view_list/', StoryListView.as_view(), name='view_list'),
]
