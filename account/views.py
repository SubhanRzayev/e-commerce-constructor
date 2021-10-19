# from django.shortcuts import render
# from account.forms import RegistrationForm

# def register(request):
#     form = RegistrationForm()
#     if request.POST:
#         form = RegistrationForm(data = request.POST)
#         if form.is_valid():
#             form.save()
#     context = {
#         'form':form
#     }
#     return render(request,'login.html',context)


# def login


from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import get_user_model
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView, PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from account.tasks import send_confirmation_mail
from account.utils.tokens import account_activation_token
from account.forms import *

User = get_user_model()


# class CustomPasswordResetView(PasswordResetView):
#     email_template_name = 'email/password_reset_email.html'
#     form_class = CustomPasswordResetForm
#     template_name = 'forget_password.html'
#     success_url = reverse_lazy('accounts:login')
    
#     def get_success_url(self):
#         messages.success(self.request, 'Şifrəni dəyişməklə bağlı müraciyyətiniz qeydə alındı.'
#                                        'Elektron poçtunuzu yoxlamağınz tələb olunur.')
#         return super(CustomPasswordResetView, self).get_success_url()


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'reset_password.html'
    form_class = CustomSetPasswordForm
    success_url = reverse_lazy('account:login')

    def get_success_url(self):
        messages.success(self.request, 'Şifrəniz uğurla dəyişdirildi...')
        return super(CustomPasswordResetConfirmView, self).get_success_url()


class RegisterView(CreateView):
    form_class = RegistrationForm
    template_name = 'login.html'
    success_url = reverse_lazy('account:login-register')

    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            print('SUbhan')
            return redirect('/')
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.is_active = False
        result = super().form_valid(form)
        user = form.instance
        send_confirmation_mail(user)
        messages.success(self.request, 'Siz uğurla qeydiyyatdan keçdiniz, xaihiş olunur emailinizi təsdiqləyəsiniz...')
        return result
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] =  RegistrationForm()
        context['forms'] = LoginForm()
        return context


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = reverse_lazy("core:index")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] =  RegistrationForm()
        context['forms'] = LoginForm()
        return context

class LogoutView(LogoutView):
    success_url = reverse_lazy('account:logout')

    def get(self, request, *args, **kwargs): 
        """
        Logout user and redirect to target url.
        """
        if self.request.user.is_authenticated():
            django_logout(request)
            messages.success(request, 'Hesabdan çıxış etdiniz...')
        return super(LogoutView, self).get_redirect_url(*args, **kwargs)


# def logout(request):
#     django_logout(request)
#     messages.success(request, 'You are logout...')
#     return redirect(reverse_lazy('core:index'))


def activate(request, uidb64, token):
    uid = force_text(urlsafe_base64_decode(uidb64))
    user = User.objects.filter(pk=uid, is_active=False).first()

    if user is not None and account_activation_token.check_token(user, token):
        messages.success(request, 'Hesabınız aktiv edildi...')
        user.is_active = True
        user.save()
        # logout(request)
        LogoutView()
        return redirect('account:login')
    else:
        messages.error(request, 'Bağlantınızın müddəti bitdi və ya keçid etibarsız oldu...')
        return redirect('core:index')


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'change-password.html'

    def get_success_url(self):
        messages.success(self.request, 'Əvvəlki şifrəniz uğurla dəyişdirildi...')
        return super(CustomPasswordResetConfirmView, self).get_success_url()


class MyAccountDetailView(DetailView):
    model = User
    template_name = 'my-account.html'


class UpdateAccountView(LoginRequiredMixin,CreateView):
    form_class = UpdateForm
    template_name ='my-account.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["forms"]=UpdateForm() 
        return context
    


    





