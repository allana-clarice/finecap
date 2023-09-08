from django import forms
from .models import Stand, Reserva
   
class StandForm (forms.ModelForm):
    class Meta:
        model = Stand
        fields = '__all__'
        widgets ={
            'lacalizacao': forms.TextInput(attrs={'class':'form-control'}),
            'valor': forms.TextInput(attrs={'class':'form-control'}),
            # 'valor': forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control'})),   
    }

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'
        widgets = {
            'cnpj': forms.TextInput(attrs={'class': 'form-control' }),
            'nome_empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria_empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'stand': forms.Select(attrs={'class': 'form-control'}),
    }
       
 
