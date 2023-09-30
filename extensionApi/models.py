import uuid
from django.db import models
from cloudinary.models import CloudinaryField
from cloudinary_storage.storage import VideoMediaCloudinaryStorage
from cloudinary_storage.validators import validate_video

class VideoData(models.Model):
    videoId = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    videoName = models.CharField(max_length=250)
    video = models.FileField(upload_to='videos/', blank=True, storage=VideoMediaCloudinaryStorage(),validators=[validate_video])
    
    def __str__(self):
        return self.videoName