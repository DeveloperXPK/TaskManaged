from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=200)

    def __str__(self):
        return self.name
    
class Task(models.Model):
    name = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=200)
    materia = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' - ' + self.materia.name