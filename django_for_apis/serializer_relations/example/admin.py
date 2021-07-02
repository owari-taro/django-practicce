from django.contrib import admin
from .models import Album, Track


class TrackInline(admin.TabularInline):
    model = Track
# Register your models here.


class AlbumAdmin(admin.ModelAdmin):
    #use the plurl not inline!
    inlines = [TrackInline]


admin.site.register(Album, AlbumAdmin)
