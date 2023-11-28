from django.db import models
from django.urls import reverse


class Story(models.Model):
    id = models.AutoField(primary_key=True)
    story_name = models.CharField(max_length=255)
    file = models.CharField(max_length=255)
    content = models.TextField()
    age = models.IntegerField(null=True, blank=True)
    language = models.CharField(max_length=50)
    mp3_file = models.BinaryField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return f'{self.id}-{self.story_name}'
    

    def get_absolute_url(self):
        return reverse('story_list_detail', args=[str(self.id)])

    