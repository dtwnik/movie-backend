from django.db import models
from django.contrib.auth.models import User


class Seat(models.Model):
    number = models.IntegerField(unique=True, auto_created=True)

    class Meta:
        verbose_name_plural = "Места"


class Cinema(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    photo = models.ImageField(upload_to='cinema', blank=True)
    year = models.IntegerField(null=True, blank=True)
    director = models.CharField(max_length=255)
    production = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    duration = models.IntegerField()
    age = models.CharField(max_length=255)
    premiere_date = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    description = models.TextField(blank=True)
    idbm = models.FloatField()
    kino_poisk = models.FloatField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Кино"
        ordering = ['genre']


class Theatr(models.Model):
    title = models.CharField(max_length=255, unique=True)
    photo = models.ImageField(upload_to='theatr', blank=True)
    photo_detail = models.ImageField(upload_to='theatr', blank=True)
    director = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    duration = models.IntegerField()
    age = models.CharField(max_length=255)
    premiere_date = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    description = models.TextField(blank=True)


class Soon(models.Model):
    title = models.CharField(max_length=255)
    title2 = models.CharField(max_length=255)
    year = models.IntegerField()
    cinema_slug = models.SlugField(max_length=255, unique=True, db_index=True)
    photo = models.ImageField(upload_to='soon')
    director = models.CharField(max_length=255)
    production = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    duration = models.IntegerField()
    age = models.CharField(max_length=255)
    premiere_date = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Скоро выйдут"


class Ticket(models.Model):
    no = models.ManyToManyField(Seat)
    movie_name = models.CharField(max_length=255)
    buyed_time = models.DateTimeField(auto_now=True)
    buyers = models.ForeignKey(User, on_delete=models.CASCADE)
    seans_time = models.TimeField()

    class Meta:
        verbose_name_plural = "Билеты"


class Seans(models.Model):
    time = models.TimeField()
    name = models.ForeignKey(Cinema, on_delete=models.CASCADE, to_field="title")
    seat = models.ManyToManyField(Seat, blank=True)

    class Meta:
        verbose_name_plural = "Сеансы"


class TSeans(models.Model):
    time = models.TimeField()
    name = models.ForeignKey(Theatr, on_delete=models.CASCADE, to_field="title")
    seat = models.ManyToManyField(Seat, blank=True)

    class Meta:
        verbose_name_plural = "Сеансы театра"