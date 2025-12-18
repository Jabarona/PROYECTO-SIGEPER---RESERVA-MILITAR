from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy

class AdminRequiredMixin(UserPassesTestMixin):
    """Permite solo a usuarios con is_admin=True."""
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin

    def handle_no_permission(self):
        return redirect(reverse_lazy('error404'))  # Cambia esto por tu vista de error/autorización


class DivperRequiredMixin(UserPassesTestMixin):
    """Permite solo a usuarios con is_divper=True."""
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_divper

    def handle_no_permission(self):
        return redirect(reverse_lazy('error404'))


class UacRequiredMixin(UserPassesTestMixin):
    """Permite solo a usuarios con is_uac=True."""
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_uac

    def handle_no_permission(self):
        return redirect(reverse_lazy('error404'))


class UbmRequiredMixin(UserPassesTestMixin):
    """Permite solo a usuarios con is_ubm=True."""
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_ubm

    def handle_no_permission(self):
        return redirect(reverse_lazy('error404'))


class LectorRequiredMixin(UserPassesTestMixin):
    """Permite solo a usuarios con is_lector=True."""
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_lector

    def handle_no_permission(self):
        return redirect(reverse_lazy('error404'))


class AdminOrDivperRequiredMixin(UserPassesTestMixin):
    """Permite solo a usuarios con is_admin=True O is_divper=True."""
    def test_func(self):
        user = self.request.user
        return user.is_authenticated and (user.is_admin or user.is_divper)

    def handle_no_permission(self):
        return redirect(reverse_lazy('error404'))

