import base64
import os
import uuid
from io import BytesIO
from django.core.files.storage import default_storage

from rest_framework.request import Request 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView

from .serializers import VideoSerializers
from .models import VideoData

class GetuploadedVideo(GenericAPIView):
    serializer_class = VideoSerializers
    queryset = VideoData.objects.all()

  
    def post(self, request):
        is_complete = request.data.get('is_complete')
        chunk_video = request.data.get('chunk_video')
        #chunk_video_id = request.data.get('video_id')
        
        video_instance = VideoData.objects.create()

        #coverting blob data 
        video_chunk = base64.b64decode(chunk_video)
            
        # Create an in-memory buffer to store the video chunks
        buffer = BytesIO()

        # Write the video chunk to the buffer using chunks() method
        buffer.write(video_chunk)

        # Move to the beginning of the buffer to read from it
        buffer.seek(0)

        # Path to the temporary file to store the video chunks
        temp_file_path = os.path.join("media", f"{video_instance.id}_temp.mp4")

        # Write the buffer content to the temporary file
        with open(temp_file_path, "ab") as temp_file:
                temp_file.write(buffer.read())

        # If it's the final chunk, move it to the final video file
        if is_complete:
            final_video_path = os.path.join("media", f"{video_instance.id}_final.mp4")
                
            # Read from the temporary file and write to the final video file
            with open(temp_file_path, "rb") as temp_file_content:
                with open(final_video_path, "ab") as final_video_file:
                    final_video_file.write(temp_file_content.read())

            # Update the video file field in the database
            video_instance.video = final_video_path
            video_instance.save()

            # Clean up the temporary file
            os.remove(temp_file_path)

            return Response(data={"message": "Video uploaded successfully."}, status=status.HTTP_200_OK)
        
        else:
            return Response(data={"message": "Video chunk uploaded successfully."}, status=status.HTTP_200_OK)        




    # def get(self,request:Request):
    #     videos = self.get_queryset()
    #     serializer = self.get_serializer(videos, many=True)
    #     return Response(data=serializer.data,status=status.HTTP_200_OK)          