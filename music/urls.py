from django.urls import path
from django.urls import include

from rest_framework.routers import DefaultRouter

from .views import SongViewSet
from .views import AlbumViewSet
from .views import ArtistViewSet

router = DefaultRouter()
router.register('songs', SongViewSet)
router.register('albums', AlbumViewSet)
router.register('artists', ArtistViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
