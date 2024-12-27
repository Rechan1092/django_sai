from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Group, Album, Song, GroupMember


def home(request):
    latest_groups = Group.objects.order_by('-created_at')[:5]
    latest_albums = Album.objects.order_by('-release_date')[:5]
    latest_songs = Song.objects.order_by('-id')[:5]
    latest_groupmembers = GroupMember.objects.order_by('-id')[:5]

    context = {
        'latest_groups': latest_groups,
        'latest_albums': latest_albums,
        'latest_songs': latest_songs,
        'latest_groupmembers': latest_groupmembers,
    }
    return render(request, 'homepage.html', context)

def search(request):
    query = request.GET.get("q", "").strip()  # Убираем пробелы
    results = {
        "groups": [],
        "albums": [],
        "songs": [],
        "members": [],
    }

    if query:
        results["groups"] = Group.objects.filter(Q(name__icontains=query))
        results["albums"] = Album.objects.filter(Q(name__icontains=query))
        results["songs"] = Song.objects.filter(Q(name__icontains=query))
        results["groupmembers"] = GroupMember.objects.filter(Q(name__icontains=query))

    for key, queryset in results.items():
        for obj in queryset:
            obj.url = reverse(f"{key[:-1]}_detail", args=[obj.pk])

    return render(request, "search.html", {"results": results, "query": query})

def group_detail(request, pk):
    group = get_object_or_404(Group, pk=pk)
    albums = group.albums.all()
    songs = group.songs.all()
    return render(request, 'details/group_detail.html', {'group': group, 'albums': albums, 'songs': songs})

def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    songs = album.songs.all()
    return render(request, 'details/album_detail.html', {'album': album, 'songs': songs})

def song_detail(request, pk):
    song = get_object_or_404(Song, pk=pk)
    return render(request, 'details/song_detail.html', {'song': song})

def groupmember_detail(request, pk):
    groupmember = get_object_or_404(GroupMember, pk=pk)
    return render(request, 'details/groupmember_detail.html', {'member': groupmember})
