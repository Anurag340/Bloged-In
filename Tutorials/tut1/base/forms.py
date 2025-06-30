from django.forms import ModelForm
from .models import Roome

class RoomForm(ModelForm):
    class Meta:
        model = Roome
        fields = '__all__'