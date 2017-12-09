from django.forms import ModelForm
from devnoob.models import Habilidade

class HabiliadeForm(ModelForm):
    class Meta:
        model = Habilidade
        fields = ['titulo', 'nivel']
