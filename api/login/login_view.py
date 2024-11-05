from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import  User
from django.contrib.auth.hashers import make_password
    # Create your views here.
def login_view( request):
    template_view = "auth-login.html"
    
    if request.user.is_authenticated and request.user.is_active:
        return redirect('home')
    
    if request.method =='POST':
        username = request.POST ['username']
        password = request.POST ['password']
        user= authenticate(request, username=username, password= password)
        
        if user is not None:
                login(request, user)
                return redirect('home')
        else:
            
            messages.error(request,'Credenciales Invalidas o Usuario no activo')
    return render(request, template_name=template_view)


# vista para registro
def register_view( request):
    template_name= "auth-register.html"
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        
        if password != password_confirmation:
            messages.error(request, 'la contraseña no coincide')
            return render(request, template_name)
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'la cuenta ya existe')
            return render(request, template_name)
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'El correo ya existe ')
            return render(request, template_name)
        
        # Crear el usuario
        user = User(
            username=username,
            email=email,
            password=make_password(password),  # Almacenar la contraseña encriptada
            is_active=True  # Establecer el usuario como activo
        )
        user.save()
        
        # Establecer el estado is_online en False (o 0)
        user.is_online = False  # Asegúrate de que este campo esté en tu modelo
        user.save()
        messages.success(request, 'cuenta creada exitosamente')
    return render(request, template_name)

# vista para recuperar contraseña
def forgot_view( request):
    template_view = "auth-forgot-password.html"
#vista para salir 
    return render(request, template_name=template_view)
def logout_view(request):
    logout(request)
    return redirect('login_vista')