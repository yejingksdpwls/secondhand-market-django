from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.urls import reverse
from django import forms



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ("email", "first_name", "last_name", "image",)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 비밀번호 필드가 없다면 help_text를 설정할 필요 없음
        if "password" in self.fields:
            del self.fields["password"]  # 비밀번호 필드를 아예 폼에서 제거

class CustomUserProfileChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            "image",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 비밀번호 필드가 없다면 help_text를 설정할 필요 없음
        if "password" in self.fields:
            del self.fields["password"]  # 비밀번호 필드를 아예 폼에서 제거
