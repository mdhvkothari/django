from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserInfoForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'This Email address is already registered.')
        return email
# class RegistraionForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#
#     class Meta:
#         model = User
#         fields = (
#             'username',
#             'first_name',
#             'last_name',
#             'email',
#             'password1',
#             'password2'
#         )
    # def save(self,commit=True):
    #     user = super(RegistraionForm,self).save(commit=False)
    #     user.first_name =  self.cleaned_data['first_name']
    #     user.last_name =  self.cleaned_data['last_name']
    #     user.email =  self.cleaned_data['email']
    #
    #     if commit:
    #         user.save()
    #
    #     return user
    # def save(self, commit=True):
    #     user = super(UserCreateForm, self).save(commit=False)
    #     if commit:
    #         user.save()
    #     return user
