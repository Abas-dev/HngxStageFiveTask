import uuid
from django.db import models

class VideoData(models.Model):
    #videoId = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    videoName = models.CharField(max_length=250)
    video = models.FileField(upload_to='videos/')
    
    def __str__(self):
        return self.videoName