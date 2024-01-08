# Generated by Django 4.2.4 on 2024-01-08 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Predict', '0002_projects_delete_carbrand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='project_alt',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='project_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='project_image_path',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='project_link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='project_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
