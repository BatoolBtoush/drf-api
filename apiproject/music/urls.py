from django.urls import path
from music.api.viewset import MusicsListAPIView, MusicsDetailAPIView

urlpatterns = [
    path("api/musics-list", MusicsListAPIView.as_view(), name="music_list"),
    path("api/<int:pk>", MusicsDetailAPIView.as_view(), name="music_detail"),
]
