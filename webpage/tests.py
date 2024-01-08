from django.test import TestCase, Client
from django.urls import reverse
from .models import projects


class webpageTests(TestCase):

    def setUp(self):
        self.test_project = projects.objects.create(
            project_image_path='../static/webpage/1.png', project_alt='Test Project', project_title='Test Project', project_description='Test Project Description', project_link='/home/predict_landmarks/')

    def test_index_view(self):
        # Test the index view
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Project')

    def test_project_model(self):
        # Test the project model
        project = projects.objects.get(id=self.test_project.id)
        self.assertEqual(project.project_image_path, '../static/webpage/1.png')
        self.assertEqual(project.project_alt, 'Test Project')
        self.assertEqual(project.project_title, 'Test Project')
        self.assertEqual(project.project_description,
                         'Test Project Description')
        self.assertEqual(project.project_link, '/home/predict_landmarks/')
