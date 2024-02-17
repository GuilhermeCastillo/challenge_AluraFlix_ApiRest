from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Video
from .serializers import VideoSerializer


# class VideoAPIView(APIView):

#     def get(self, request):
#         videos = Video.objects.all()
#         serializer = VideoSerializer(videos, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = VideoSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

class VideosAPIView(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    
class VideoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer