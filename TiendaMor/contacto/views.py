from django.shortcuts import redirect, render
from .forms import FormularioContacto
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from src.settings import EMAIL_HOST_USER

# Create your views here.

def contacto(request):
    formulario_contacto = FormularioContacto()

    if request.method=='POST':
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get('nombre')
            email=request.POST.get('correo')
            contenido=request.POST.get('contenido')

##inicio espacio funcion email
            email=EmailMessage(
                    "Mensaje:Mensaje desde Django",
                    "El usuario {} del correo {} escribe lo siguiente:\n\n {}".format(nombre,email,contenido),
                    EMAIL_HOST_USER, 
                    ['camilo.montoya0531@gmail.com'], 
                    reply_to=[email]
                    )

            try:
                email.send()
                return redirect('/contacto/?valido')
            except:
                return redirect('/contacto/?novalido')
    

##fin espacio funcion email

    return render(request, 'contacto/contacto.html',{'formulario_contacto':formulario_contacto})