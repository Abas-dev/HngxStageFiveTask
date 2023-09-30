from rest_framework.request import Request 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView

from .serializers import VideoSerializers
from .models import VideoData

class GetuploadedVideo(GenericAPIView):
    serializer_class = VideoSerializers
    queryset = VideoData.objects.all()

    def post(self,request:Request):

        sentData = {
            "videoName": request.POST.get('videoName', None),
            "video": request.FILES.get('video', None),
            }

        serializer = self.serializer_class(data=sentData)
        if serializer.is_valid():
            serializer.save()
            response = { 
                'message':'video uploaded successfully',
                'data': serializer.data
            }
            return Response(data=response,status=status.HTTP_200_OK)
        return Response(data={'message':serializer.errors},status=status.HTTP_404_NOT_FOUND)

    def get(self,request:Request):
        videos = self.get_queryset()
        serializer = self.get_serializer(videos, many=True)
        
        return Response(data=serializer.data,status=status.HTTP_200_OK)    