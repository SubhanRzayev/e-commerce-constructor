from django import forms
from core.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'name',
            'email',
            'subject',
            'message',
        )

        widgets = {

            'name':forms.TextInput(attrs={
                        'class':'form-control',
                        'placeholder': 'Your Name'
                    }),

            'email':forms.EmailInput(attrs={
                'class':'form-control',
                'placeholder': 'Your email'
            }),

            'subject':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Write subject'
            }),

            'message':forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Your message'
            }),
        }

 # name = forms.CharField(widget=forms.TextInput(attrs={
    #                     'class': 'form-control',
    #                     'placeholder' : 'Your Name '
    # })) 
    
    # email = forms.EmailField(widget=forms.EmailInput(attrs={
    #                     'class': 'form-control',
    #                     'placeholder' : 'Your Email'
    # })) 

    # subject = forms.CharField(widget=forms.TextInput(attrs={
    #                     'class': 'form-control',
    #                     'placeholder' : 'Your Subject '
    # }))   

    # message = forms.CharField(widget=forms.Textarea(attrs={
    #                     'class': 'form-control',
    #                     'placeholder' : 'Your Message '
    # })) 