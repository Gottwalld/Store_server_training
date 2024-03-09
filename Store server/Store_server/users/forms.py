from django.contrib.auth.forms import AuthenticationForm

class UserLoginForm (AuthenticationForm):
    class Meta:
        model = 'User'
        fields = ('username', 'password')
        pass