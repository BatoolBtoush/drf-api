from rest_framework import generics
from .serializers import MusicSerializer
from music.models import Music


class MusicsListAPIView(generics.ListCreateAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer


class MusicsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
