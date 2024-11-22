from django import forms


# Formulario para materias
class CreateSubject(forms.Form):
    name = forms.CharField(label="Materia", max_length=50)
    descripcion = forms.CharField(
        label="Descripcion de la materia", max_length=200, widget=forms.Textarea
    )


# Formulario para tareas
class CreateTask(forms.Form):
    name = forms.CharField(label="Tarea", max_length=50)
    descripcion = forms.CharField(
        label="Descripcion de la tarea", max_length=200, widget=forms.Textarea
    )

    # fecha de entrega
    """due_date = forms.DateField(label='Fecha de entrega', widget=forms.SelectDateWidget)"""
