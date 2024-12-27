from django.contrib import admin
from .models import Group, Album, Song, GroupMember

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'release_date', 'group')
    search_fields = ('name', 'group__name')

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('name', 'album', 'group', 'duration')
    search_fields = ('name', 'album__name', 'group__name')

@admin.register(GroupMember)
class GroupMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'group')
    search_fields = ('name', 'group__name')
