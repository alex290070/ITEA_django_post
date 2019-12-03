from django.views.generic import TemplateView, FormView, RedirectView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator

from users.forms import RegisterForm
from django.http import JsonResponse


class ProfileView(TemplateView):
    template_name = 'users/profile.html'
    login_url = '/users/login/'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class RegisterView(FormView):
    template_name = 'users/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('core:post-list')

    def form_valid(self, form):
        user = form.save()
        user.send_user_mail('Registration', 'Welcome!')
        login(self.request, user)
        return super().form_valid(form)

    def form_invalid(self, form):
        return JsonResponse(form.errors)


class LoginView(FormView):
    template_name = 'users/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('core:post-list')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)

class LogoutView(RedirectView):
    pattern_name = 'users:login'

    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        return super().get_redirect_url(*args, **kwargs)
