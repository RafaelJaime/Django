from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.contrib import messages

from .models import User
from .forms import SingUpForm
# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}.'.format(user.username))
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña no válidos.')
    return render(request, 'account/login.html', {})


def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión cerrada correctamente.')
    return redirect('index')


def register_view(request):
    form = SingUpForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = User.objects.create_user(
            form.cleaned_data.get('username'), 
            password=form.cleaned_data.get('password'), 
            dni=form.cleaned_data.get('dni'), 
            first_name=form.cleaned_data.get('firstName'), 
            last_name = form.cleaned_data.get('lastName'),
            direction = form.cleaned_data.get('direction'),
            telephone = form.cleaned_data.get('telephone'),
            # bornDate = form.cleaned_data.get('bornDate'),
            is_active = False,
            is_client=True
        )
        # user.bornDate = form.cleaned_data.get('bornDate')
        if user:
            login(request, user)
            messages.success(request, 'Usuario creado correctamente.')
            messages.info(request, 'Debes esperar a que el administrador active tu cuenta.')
            return redirect('index')
    return render(request, 'account/singup.html', {'form': form})