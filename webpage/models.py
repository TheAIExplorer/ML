from django.db import models
import os


def project_image_filename(instance, filename):
    filename, extension = os.path.splitext(filename)
    return f'images/project_{instance.project_id}{extension}'


class projects(models.Model):
    project_id = models.IntegerField(primary_key=True)
    image = models.ImageField(upload_to=project_image_filename)
    project_description = models.TextField(blank=True)

    def __str__(self):
        return 'Project_'+str(self.project_id)
