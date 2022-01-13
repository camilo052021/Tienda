from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls.resolvers import URLPattern
 

urlpatterns = [
    path("registro", views.register_request, name="registro"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),

    path('reset_password/', 
        auth_views.PasswordResetView.as_view(template_name='password/password_reset.html'), 
        name='reset_password'),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'), 
        name='password_reset_done'),

    path('reset/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name='password/password_reset_confirm.html'), 
        name='password_reset_confirm'),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'), 
        name='password_reset_complete'),

    path('datos/', views.datos, name='datos'),
    path('datos/<str:username>', views.datos, name='datos'), 
    path('editar_datos/', views.editar_datos, name='editar_datos'),
    #path('agregar_datos/', views.agregar_datos, name='agregar_datos'),

]