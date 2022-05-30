from django.urls import path
from music.api.viewset import MusicsListAPIView, MusicsDetailAPIView

urlpatterns = [
    path("music-list", MusicsListAPIView.as_view(), name="music_list"),
    path("<int:pk>", MusicsDetailAPIView.as_view(), name="music_detail"),
]
