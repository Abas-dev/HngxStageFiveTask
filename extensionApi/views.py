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
        is_complete = request.data.get('is_complete')
        chunk_video = request.data.get('chunk_video')
        chunk_video_id = request.data.get('video_id')
        
        



    def get(self,request:Request):
        videos = self.get_queryset()
        serializer = self.get_serializer(videos, many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)          