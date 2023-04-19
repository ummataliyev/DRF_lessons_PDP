from django.contrib import admin

from .models import Artist
from .models import Album
from .models import Song

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Song)
