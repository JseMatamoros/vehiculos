# from django import forms
# from .models import Vehiculo

# class VehiculoForm(forms.ModelForm):
#     class Meta:
#         model = Vehiculo
#         exclude = ['condicion_precio']
#         fields = '__all__' 


from django import forms
from .models import Vehiculo

class VehiculoForm(forms.ModelForm):
    imagen = forms.ImageField(required=True)  # Agrega este campo para manejar la imagen

    class Meta:
        model = Vehiculo
        exclude = ['condicion_precio']
