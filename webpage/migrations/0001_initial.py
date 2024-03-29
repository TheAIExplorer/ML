# Generated by Django 4.2.4 on 2024-01-09 09:10

from django.db import migrations, models
import webpage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='projects',
            fields=[
                ('project_id', models.IntegerField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to=webpage.models.project_image_filename)),
                ('project_description', models.TextField(blank=True)),
                ('project_link', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
