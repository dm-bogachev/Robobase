from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

class EmployeeCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields

class EmployeeChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = UserChangeForm.Meta.fields