


from django import forms
from django.forms import ModelForm


from authentications.models import Profile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
    
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('image', 'socialname', 'description')
        # widgets = {
        #     'description': forms.Textarea(attrs={'maxlength': '200'})
        # }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['socialname'].widget.attrs['placeholder'] = 'socialname'
        self.fields['description'].widget.attrs['placeholder'] = 'description'        
