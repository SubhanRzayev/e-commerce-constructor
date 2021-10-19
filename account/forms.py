from django import forms

from django.contrib.auth import get_user_model,password_validation
from django.forms import widgets

from django.contrib.auth.forms import  PasswordChangeForm, SetPasswordForm, UserCreationForm,AuthenticationForm,UsernameField
from django.utils.translation import gettext,gettext_lazy as _

User = get_user_model()

class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label = ('Password'),
        strip = False,
        widget = forms.PasswordInput(attrs ={
            'class':'form-control',
            'placeholder':'Password'
        }),

        help_text = password_validation.password_validators_help_text_html(),
    )

    password2 = forms.CharField(
        label = _('Password confirmation'),
        widget = forms.PasswordInput(attrs = {
            'class': 'form-control',
            'placeholder': 'Confirm Password'
        }),

        help_text =('Enter the same password as before, for verification'),
    )

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'phone',
            'password1',
            'password2',
        )

        widgets = {
            'first_name':forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First Name*'
            }),

            'last_name':forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last Name*'
            }),


            'username':forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username*'
            }),
            
            

            'email':forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email*'
            }),

            'phone':forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Number*'
            }),

            'address':forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Address*'
            }),
        }

class LoginForm(AuthenticationForm):
    username = UsernameField(label=('E-mail/Username'),widget=forms.TextInput(attrs={'autofocus': True,
                                                            'class':'form-control',
                                                           'placeholder': 'Username*'
                                                           }))
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class':'form-control',
            'placeholder': 'Password*'
        }),
    )

class UpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone',
            'address',
        )
            

        widgets = {
            'first_name':forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First Name*'
            }),

            'last_name':forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last Name*'
            }),

            'email':forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email*'
            }),

            'phone':forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Number*'
            }),

            'address':forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Address*'
            }),
        }







# class LoginForm(forms.Form):
#     username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True,
#                                                            'placeholder': 'Username*'
#                                                            }))
#     password = forms.CharField(
#         label=("Password"),
#         strip=False,
#         widget=forms.PasswordInput(attrs={
#             'placeholder': 'Password*'
#         }),
#     )


class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'New Password'
        }),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),

    )

    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm New Password'
        }),
    )


class CustomChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Change Password'
            }),
    )   
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )




