from django.db import models


class projects(models.Model):
    project_image_path = models.CharField(max_length=100, null=True)
    project_alt = models.CharField(max_length=100, null=True)
    project_title = models.CharField(max_length=100, null=True)
    project_description = models.TextField()
    project_link = models.CharField(max_length=100, null=True)
