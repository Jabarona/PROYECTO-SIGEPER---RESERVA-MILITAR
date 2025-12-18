from django.contrib.auth.backends import ModelBackend
from usuarios.models import CustomUser

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Django espera username, pero tú quieres buscar por correo.
        if username is None:
            username = kwargs.get('correo')
        try:
            user = CustomUser.objects.get(correo=username)
        except CustomUser.DoesNotExist:
            return None
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None
