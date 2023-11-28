from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('generate/', GenerateStoryView.as_view(), name='generate_story'),
    path('view_list/', StoryListView.as_view(), name='view_list'),
    path('delete_file/<int:story_id>/', DeleteFileView.as_view(), name='delete_file'),
    path('update_file/<int:pk>/edit', StoryUpdateView.as_view(), name='update_file'),
    path('view_test_file/<int:story_id>/', ViewTestFileView.as_view(), name='view_test_file'),
    # path('voiceTest_and_download/<int:story_id>/', VoiceTestAndDownloadView.as_view(), name='voiceTest_and_download'),
]
