from django.db import models


class projects(models.Model):
    project_image_path = models.CharField(
        max_length=100, null=True, blank=True)
    project_alt = models.CharField(max_length=100, null=True, blank=True)
    project_title = models.CharField(max_length=100, null=True, blank=True)
    project_description = models.TextField(null=True, blank=True)
    project_link = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.project_title
