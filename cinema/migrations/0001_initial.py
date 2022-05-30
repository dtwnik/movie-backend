# Generated by Django 4.0.4 on 2022-05-25 10:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('photo', models.ImageField(blank=True, upload_to='cinema')),
                ('year', models.IntegerField(blank=True, null=True)),
                ('director', models.CharField(max_length=255)),
                ('production', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=255)),
                ('duration', models.IntegerField()),
                ('age', models.CharField(max_length=255)),
                ('premiere_date', models.DateField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('idbm', models.FloatField()),
                ('kino_poisk', models.FloatField()),
            ],
            options={
                'verbose_name_plural': 'Кино',
                'ordering': ['genre'],
            },
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(auto_created=True, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Места',
            },
        ),
        migrations.CreateModel(
            name='Soon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('title2', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('cinema_slug', models.SlugField(max_length=255, unique=True)),
                ('photo', models.ImageField(upload_to='soon')),
                ('director', models.CharField(max_length=255)),
                ('production', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=255)),
                ('duration', models.IntegerField()),
                ('age', models.CharField(max_length=255)),
                ('premiere_date', models.DateField(blank=True)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Скоро выйдут',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=255)),
                ('buyed_time', models.DateTimeField(auto_now=True)),
                ('seans_time', models.TimeField()),
                ('buyers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('no', models.ManyToManyField(to='cinema.seat')),
            ],
            options={
                'verbose_name_plural': 'Билеты',
            },
        ),
        migrations.CreateModel(
            name='Seans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.cinema', to_field='title')),
                ('seat', models.ManyToManyField(blank=True, to='cinema.seat')),
            ],
            options={
                'verbose_name_plural': 'Сеансы',
            },
        ),
    ]
