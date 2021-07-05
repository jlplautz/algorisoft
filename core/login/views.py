from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, RedirectView
import src.settings as setting


class LoginFormView(LoginView):
    template_name = 'login.html'

    # para verificar se a sessão foi iniciada
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(setting.LOGIN_REDIRECT_URL)
        return super().dispatch(request, *args, **kwargs)

    # para sob-escrever o metodo get_context_data
    def get_context_data(self, **kwargs):
        # para recuperar o que já foi definido na classe LoginView
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Iniciar sessão'
        return context


# Iniciar sessão com LoginForm
class LoginFormView2(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy(setting.LOGIN_REDIRECT_URL)

    # para verificar se a sessão foi iniciada
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)

    # Qdo formulário estiver valido ver o user e redirecionar
    def form_valid(self, form):
        login(self.request, form.get_user())
        return HttpResponseRedirect(self.success_url)

    # para sob-escrever o metodo get_context_data
    def get_context_data(self, **kwargs):
        # para recuperar o que já foi definido na classe LoginView
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Iniciar sessão'
        return context


class LogoutRedirectView(RedirectView):
    pattern_name = 'login'

    # para encerrar a sessão
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)


class LogoutFormView(LogoutView):
    pass
