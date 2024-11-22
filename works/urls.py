from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('subject', views.subject, name='subject'),
    path('subject/new', views.createSubject, name='newSubject'),
    path('subject/<int:id>', views.task, name='task'),
    path('subject/<int:id>/new', views.createTask, name='newTask'),
    path('subject/<int:id>/download', views.downloadTask, name='download'),
]