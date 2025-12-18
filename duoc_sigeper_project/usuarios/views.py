from django.contrib.auth.views import LogoutView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import *
from .mixins import *
from .models import CustomUser
from django.views import View
from django.contrib.auth import login, authenticate
from django.contrib.auth import get_user_model
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView
from django.contrib import messages
from mantenedor.models import UnidadModel, GradoModel
from django.core.mail import send_mail
import random

User = get_user_model()

# Vista para login
class CustomLoginView(View):
    template_name = 'usuarios/login.html'
    form_class = CustomLoginForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            correo = form.cleaned_data['correo']
            password = form.cleaned_data['password']
            user = authenticate(request, correo=correo, password=password)

            if user:
                # 1. Guardar el id en sesión TEMPORAL, pero NO hacer login todavía
                request.session['pre_2fa_user_id'] = user.id
                # 2. Generar código y guardarlo en sesión
                codigo_2fa = str(random.randint(100000, 999999))
                request.session['codigo_2fa'] = codigo_2fa
                # 3. Enviar código por correo
                send_mail(
                    'Autenticación en dos pasos para acceder a SIGEPER',
                    f'Tu código es: {codigo_2fa}',
                    'no-reply@sigeper.cl',
                    [user.correo],
                    fail_silently=True
                )
                # 4. Redirigir a la pantalla de verificación de 2FA
                return redirect('verificar_2fa')
            else:
                return render(request, self.template_name, {'form': form, 'error': 'Credenciales inválidas.'})
        return render(request, self.template_name, {'form': form})

# Vista para logout
class CustomLogoutView(LogoutView):
    # Redirige al login tras cerrar sesión
    next_page = reverse_lazy('login')



#Vista para crear usuario
class CreateUserView(AdminOrDivperRequiredMixin, CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'usuarios/user-create.html'
    success_url = reverse_lazy('user_create')

    def form_valid(self, form):
        user = form.save(commit=False)
        password = "Reserva2025"
        user.set_password(password)
        user.save()
        messages.success(self.request, f'Usuario creado. Contraseña: {password}')
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Errores del formulario:", form.errors)
        messages.error(self.request, "Ocurrió un error al crear el perfil. Revisa los campos e intenta nuevamente.")
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['unidades'] = UnidadModel.objects.all()
        context['grados'] = GradoModel.objects.all()
        return context

#vista para listar usuarios
class UserListView(AdminOrDivperRequiredMixin, ListView):
    template_name = 'usuarios/user_list.html'
    model = CustomUser
    context_object_name = 'usuarios'
    paginate_by = 10


#Vista para actualizar usuario
class UserUpdateView(AdminOrDivperRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserUpdateForm
    template_name = 'usuarios/user_update.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['unidades'] = UnidadModel.objects.all()
        context['grados'] = GradoModel.objects.all()
        return context
    
    def form_valid(self, form):
        messages.success(self.request,'Usuario actualizado correctamente')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, 'algo anda mal')
        print()
        return super().form_invalid(form)
    
    def get_success_url(self):   
        return reverse_lazy('user_update', args=[self.object.id])

#Vista para eliminar usuario
class UserDeleteView(AdminOrDivperRequiredMixin, DeleteView):
    template_name ='usuarios/user_confirm_delete.html'
    model =CustomUser
    success_url = reverse_lazy('user_list')
    
#vista para ver perfil
class ProfileView(TemplateView):
    template_name = 'usuarios/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
    
#vista para cambiar contraseña
class ProfileChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'usuarios/profile-change_password.html'
    success_url = reverse_lazy('profile')

    def get(self, request):
        form = self.form_class(user=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(user=request.user, data=request.POST)
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)
    
# vista para editar perfil
class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = ProfileEditForm
    template_name = 'usuarios/profile-update.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, 'Perfil actualizado correctamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, 'Ocurrió un error al actualizar el perfil. Revisa los campos e intenta nuevamente.')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['unidades'] = UnidadModel.objects.all()
        context['grados'] = GradoModel.objects.all()
        return context


class Verificar2FAView(View):
    def get(self, request):
        correo = None
        if 'pre_2fa_user_id' in request.session:
            from usuarios.models import CustomUser
            user_id = request.session['pre_2fa_user_id']
            correo = CustomUser.objects.get(id=user_id).correo
        return render(request, 'usuarios/verificar_2fa.html', {'correo': correo})

    def post(self, request):
        codigo_ingresado = request.POST.get('codigo')
        codigo_correcto = request.session.get('codigo_2fa')
        user_id = request.session.get('pre_2fa_user_id')

        if codigo_ingresado == codigo_correcto and user_id:
            from usuarios.models import CustomUser
            user = CustomUser.objects.get(id=user_id)
            login(request, user)
            # Limpiar la sesión
            request.session.pop('codigo_2fa', None)
            request.session.pop('pre_2fa_user_id', None)
            return redirect('index')
        else:
            correo = None
            if user_id:
                from usuarios.models import CustomUser
                correo = CustomUser.objects.get(id=user_id).correo
            return render(request, 'usuarios/verificar_2fa.html', {
                'error': 'Código inválido. Intenta nuevamente.',
                'correo': correo
            })
