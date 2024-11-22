from datetime import date
from django.shortcuts import redirect, render
from .models import Subject, Task
from .forms import CreateSubject, CreateTask
import pandas as pd
import os
# Create your views here.

# Vista para la pagina principal
def index(req):
    return render(req, 'index.html')

# Vista para crear materias
def subject(req):
    materias = Subject.objects.all()
    if len(materias) > 0:
        return render(req, 'subjects/subject.html', {
            'subjects': materias,
        })
    return render(req, 'subjects/subject.html', {
        'materias': 'No hay materias registradas'
    })

# Vista para crear materias
def createSubject(req):
    if req.method == 'POST':
        Subject.objects.create(name=req.POST['name'], descripcion=req.POST['descripcion'])
        return redirect('subject')
    else:
        return render(req, 'subjects/newSubject.html', {
            'form': CreateSubject()
        })
    

# ------------ Tareas ------------

# Vista para listar tareas de cada materia
def task(req, id):
    tareas = Task.objects.filter(materia_id=id)
    materia = Subject.objects.get(id=id)

    return render(req, 'tasks/task.html', {
        'tasks': tareas,
        'materia': materia
    })

# Vista para crear tareas
def createTask(req, id):
    if req.method == 'POST':
        Task.objects.create(name=req.POST['name'], descripcion=req.POST['descripcion'], materia_id=id)
        return redirect('subject')
    else:
        materia = Subject.objects.get(id=id)
        return render(req, 'tasks/newTask.html', {
            'form': CreateTask(),
            'materia': materia
        })
    
def downloadTask(req, id):
    tareas = Task.objects.filter(materia_id=id)
    materia = Subject.objects.get(id=id)

    # Creamos un archivo excel con las tareas de la materia
    # Crear la ruta completa para guardar el archivo en la carpeta 'documents'
    documents_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'documents')
    os.makedirs(documents_path, exist_ok=True)

    nombre_archivo = f"{materia.name.replace(' ', '')}_{date.today()}.xlsx"
    archivo_path = os.path.join(documents_path, nombre_archivo)

    dataFrame = pd.DataFrame(tareas.values())
    dataFrame.to_excel(archivo_path, index=False, sheet_name='Tareas')

    return redirect('task', id=id)
