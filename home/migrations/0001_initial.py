# Generated by Django 2.2.1 on 2019-05-06 09:24

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
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='article/')),
                ('date', models.DateTimeField()),
                ('content', models.TextField()),
                ('draft', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='hero/')),
                ('caption', models.CharField(max_length=250)),
                ('sub_heading', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('date', models.DateTimeField()),
                ('image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='story/')),
                ('content', models.TextField()),
                ('draft', models.BooleanField(default=True)),
                ('photographer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tag', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.Tag')),
            ],
            options={
                'verbose_name': 'My Stories',
                'ordering': ['-date'],
            },
        ),
    ]
