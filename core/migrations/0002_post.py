# Generated by Django 4.1.5 on 2023-01-28 10:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='post_images')),
                ('caption', models.TextField()),
                ('post_date', models.DateTimeField(default=datetime.datetime.now)),
                ('no_of_like', models.IntegerField(default=0)),
            ],
        ),
    ]
