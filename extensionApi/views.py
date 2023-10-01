import base64
import os
import uuid

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
        video_chunk = request.data.get('videoChunk')
        is_completed = request.data.get('isCompleted')
        video_id = request.data.get('video_id')

        # Validate video_id (example: check if it contains only alphanumeric characters)
        if not video_id:
            return Response({'error': 'Invalid video ID'}, status=status.HTTP_400_BAD_REQUEST)

        file_path = f'video/video/{video_id}.mp4'

        # Check if the video ID matches the one sent by the frontend
        if not os.path.exists(file_path):
            return Response({'error': 'Invalid video ID'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Append the video chunk to the existing video file
            with open(file_path, 'ab') as video_file:
                video_file.write(video_chunk)
                
            # Check if the video is completed
            if is_completed:
                # Convert the file to video and save it
                # Your code to convert the file to video and save it goes here
                
                # After saving the complete video, you can delete the temporary chunk file
                os.remove(file_path)
                
                return Response({'message': 'Video saved successfully'}, status=status.HTTP_200_OK)
            
            return Response({'message': 'Video chunk appended successfully'}, status=status.HTTP_200_OK)
            
        except Exception as e:
            # Handle the exception (e.g., log the error, return an error response)
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



    def get(self,request:Request):
        videos = self.get_queryset()
        serializer = self.get_serializer(videos, many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)    

# class VideoUploadAPIView(APIView):
#     def post(self, request, *args, **kwargs):
#         title = request.data.get('title', 'Untitled')
#         video_chunk = request.data.get('video_chunk')
#         try:
#             video_instance = RecordedVideo.objects.get(title=title)
#         except RecordedVideo.DoesNotExist:
#             video_instance = RecordedVideo.objects.create(title=title)
#         # Create a temporary file to store the video chunks
#         temp_file = NamedTemporaryFile(delete=False)
#         try:
#             # Write the received video chunk to the temporary file
#             temp_file.write(video_chunk.read())
#             # Close the temporary file to flush the data to disk
#             temp_file.close()
#             # Check if all chunks have been received
#             if request.data.get('final_chunk'):
#                 # Concatenate all chunks into the final video file
#                 final_video_path = os.path.join('media', f'{title}_final.mp4')
#                 with open(final_video_path, 'ab') as final_video:
#                     with open(temp_file.name, 'rb') as temp_file_content:
#                         final_video.write(temp_file_content.read())
#                 # Update the video file field in the database
#                 video_instance.video_file.name = final_video_path
#                 video_instance.save()
#                 # Clean up the temporary file
#                 os.remove(temp_file.name)
#                 return Response({'message': 'Video uploaded successfully.'}, status=status.HTTP_200_OK)
#             else:
#                 return Response({'message': 'Video chunk uploaded successfully.'}, status=status.HTTP_200_OK)
#         except Exception as e:
#             # Handle any errors (e.g., data corruption, incomplete chunks)
#             return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)        