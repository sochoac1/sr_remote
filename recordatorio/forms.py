from django import forms
from . import myFields
from recordatorio.models import Recordatorio


DAY_CHOICES = (
    ("Lunes", "Lunes"),
    ("Martes", "Martes"),
    ("Miercoles", "Miercoles"),
    ("Jueves", "Jueves"),
    ("Viernes", "Viernes"),
    ("Sabado", "Sabado"),
    ("Domingo", "Domingo"),
)


class RecordatorioForm(forms.ModelForm):
    nombre = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':2,'placeholder':'Nombre'}),required=True)
    contenido = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':2,'placeholder':'contenido'}),required=True)
    diaSemana = forms.ChoiceField(choices=DAY_CHOICES)
    hora = forms.TimeField()

    class Meta:
        model = Recordatorio
        fields = ['nombre', 'contenido','diaSemana','hora']