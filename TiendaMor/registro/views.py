from django.shortcuts import  render, redirect, get_object_or_404
from .models import Datos
from django.contrib.auth.models import User
from django.urls import reverse_lazy 
from django.forms.forms import Form
from django import forms
from django.http import request
from .forms import NewUserForm, DatosForm, ActualizaDatosForm, ActualizaUsuarioForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registro Exitoso" )
			return redirect("inicio")
		messages.error(request, "Información de registro inválida")
	form = NewUserForm()
	return render (request=request, template_name="registro/registro.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			usuario = form.cleaned_data.get('username')
			clave = form.cleaned_data.get('password')
			user = authenticate(username=usuario, password=clave)
			if user is not None:
				login(request, user)
				messages.info(request, f"Estas Logueado como {usuario}.")
				return redirect("inicio")
			else:
				messages.error(request,"Usuario o Clave inválida")
		else:
			messages.error(request,"Usuario o Clave inválida")
	form = AuthenticationForm()
	return render(request=request, template_name="registro/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "Has Salido") 
	return redirect("inicio")

def datos(request, username =None):
    current_user = request.user
    if username == current_user.username:
        user = User.objects.get(username = username)
    else:
        user = current_user
    return render(request, 'datos.html', {'user':user})


@login_required
def editar_datos(request):
	if request.method=='POST':
		p_form = ActualizaDatosForm(request.POST, request.FILES, instance=request.user.datos)

		if  p_form.is_valid():
			p_form.save()
			return redirect('tienda')

	else:
		p_form = ActualizaDatosForm()

	context = {'p_form' : p_form}
	return render(request, 'datos/editar_datos.html', context)


'''def agregar_datos(request):
	if request.method =='POST':
		form = DatosForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('carro')
	else:
		form = DatosForm()

	context = {'form': form}
	return render(request,'datos/agregar_datos.html',context)'''