import uuid
from django.db import models

class VideoData(models.Model):
    video = models.FileField(upload_to='videos/')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Recorded Video {self.id}"  