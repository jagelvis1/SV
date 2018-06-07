from __future__ import absolute_import

from django import forms

from apps.persona.models import cliente

class PersonaForm(forms.ModelForm):
	"""docstring for PersonaCreate"""
	class Meta:
		model = cliente

		fields = [
			'tipo_cliente',
			'nombre_cliente',
			'tipo_documento',
			'num_documento',
			'direccion',
			'telefono',
			'correo',
			'estatus',
		]
		labels = {
			'tipo_cliente': 'tipo de cliente',
			'nombre_cliente': 'cliente',
			'tipo_documento': 'tipo de documento',
			'num_documento': 'num. de documento',
			'direccion': 'direccion',
			'telefono': 'telefono',
			'correo': 'telefono',
			'estatus': 'estatus',
		}
		widgets = {
			'tipo_cliente': forms.Select(attrs={'class':'form-control'}),
			'nombre_cliente': forms.TextInput(attrs={'class':'form-control'}),
			'tipo_documento': forms.Select(attrs={'class':'form-control'}),
			'num_documento': forms.TextInput(attrs={'class':'form-control'}),
			'direccion': forms.TextInput(attrs={'class':'form-control'}),
			'telefono': forms.TextInput(attrs={'class':'form-control'}),
			'correo': forms.TextInput(attrs={'class':'form-control'}),
			'estatus': forms.Select(attrs={'class':'form-control'}),
		}
