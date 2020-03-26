from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=200,
                            help_text='Username is required',
                            required=True,)
    email = forms.EmailField(max_length=100,
                            label='Sender',
                            help_text='E.g., "me@example.com"')
    comment = forms.CharField(max_length=200,widget=forms.Textarea(attrs={
        'rows':'5',
        'placeholder':'Leave Comment',
    }))


    # name = forms.CharField(max_length=200,
    #                         widget=forms.TextInput(attrs={
    #                             'required':'False',
    #                             'class':'form-control',
    #                             'placeholder':'Enter Username',
    #                             'help_text':'100 characters max',
    #                         }))
    # email = forms.EmailField(max_length=100,
    #                         widget=forms.EmailInput(attrs={
    #                                 'required':'True',
    #                                 'class':'form-control',
    #                                 'placeholder':'Enter Email'
    #                           }))
    # comment = forms.CharField(max_length=200,
    #                             widget=forms.Textarea(attrs={
    #                                 'rows':'6',
    #                                 'required':'True',
    #                                 'class':'form-control',
    #                                 'placeholder':'Comment here'
    #                           }))



