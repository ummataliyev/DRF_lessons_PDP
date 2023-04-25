from django.test import TestCase

from music.models.album import Album
from music.models.artist import Artist
from music.serializers import SongSerializer
from music.serializers import ArtistSerializer


class TestArtistSerializer(TestCase):
    def setUp(self) -> None:
        self.artist = Artist.objects.create(name="Tom Odell")

    def test_data(self):
        data = ArtistSerializer(self.artist).data
        assert data['id'] is not None
        assert data['name'] == "Tom Odell"
        assert data['picture'] == ''


class TestSongSerializer(TestCase):
    def setUp(self) -> None:
        self.artist = Artist.objects.create(name="Test Artist")
        self.album = Album.objects.create(artist=self.artist, title="Test Album") # noqa

    def test_is_valid(self):
        data = {
            "title": "Tom Odell",
            "album": None,
            "cover": '',
            "source": "http://example.com/music.mp3",
            "listened": 0,
        }

        serializer = SongSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_is_not_valid(self):
        data = {
            "title": "Test Song",
            "album": self.album.id,
            "cover": '',
            "source": "http://example.com/music",
            "listened": 0,
        }
        serializer = SongSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertEqual(str(serializer.errors['source'][0]), "Mp3 file is requiered")  # noqa
