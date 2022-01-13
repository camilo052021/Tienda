from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import request
from .models import Datos


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	password1=forms.CharField(widget=forms.PasswordInput)
	password2=forms.CharField(widget=forms.PasswordInput)
	
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
		help_texts={k:"" for k in fields}

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class DatosForm(forms.ModelForm):
    class Meta:
        model = Datos
        fields  = '__all__'
        widgets = {
            'nombre' : forms.TextInput(attrs = {'class':'form-control mt-2', 'placeholder':'Nombre'}),
            'ciudad' : forms.TextInput(attrs = {'class':'form-control mt-2', 'placeholder':'Ciudad'}),
            'direccion' : forms.TextInput(attrs = {'class':'form-control mt-2', 'placeholder':'Dirección'}),
            'celular' : forms.TextInput(attrs = {'class':'form-control mt-2', 'placeholder':'Celular'}),     
        }

class ActualizaUsuarioForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username','email',]

class ActualizaDatosForm(forms.ModelForm):
    class Meta:
        model = Datos
        fields  = ['nombre','ciudad','direccion','celular',]
        widgets = {
            'nombre' : forms.TextInput(attrs = {'class':'form-control mt-2', 'placeholder':'Nombre'}),
            'ciudad' : forms.TextInput(attrs = {'class':'form-control mt-2', 'placeholder':'Ciudad'}),
            'direccion' : forms.TextInput(attrs = {'class':'form-control mt-2', 'placeholder':'Dirección'}),
            'celular' : forms.TextInput(attrs = {'class':'form-control mt-2', 'placeholder':'Celular'}),     
        }
