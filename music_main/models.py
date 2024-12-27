from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    created_at = models.DateField(verbose_name="Дата создания")
    image = models.ImageField(upload_to="groups/", verbose_name="Изображение", blank=True, null=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="albums", verbose_name="Группа")
    release_date = models.DateField(verbose_name="Дата выпуска")
    cover = models.ImageField(upload_to="albums/", verbose_name="Обложка альбома", blank=True, null=True)

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, related_name="songs", verbose_name="Альбом", blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="songs", verbose_name="Группа", blank=True, null=True)
    duration = models.DurationField(verbose_name="Длительность")
    audio_file = models.FileField(upload_to="songs/", verbose_name="Аудиофайл", blank=True, null=True)
    lyrics = models.TextField(verbose_name="Текст песни", blank=True, null=True)

    def __str__(self):
        return self.name


class GroupMember(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    biography = models.TextField(verbose_name="Биография")
    role = models.CharField(max_length=255, verbose_name="Роль")
    birth_date = models.DateField(verbose_name="Дата рождения")
    photo = models.ImageField(upload_to="members/", verbose_name="Фотография", blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="members", verbose_name="Группа")

    def __str__(self):
        return self.name
