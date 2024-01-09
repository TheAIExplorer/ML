from django.urls import path, re_path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('index/<int:project_id>/', views.project, name='project'),


]
