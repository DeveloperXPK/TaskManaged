from django.contrib import admin

from .models import Subject, Task

# Register your models here.
admin.site.register(Subject)
admin.site.register(Task)