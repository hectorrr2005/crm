from django import forms
from apps.userprofile.models import Profile
from apps.common.forms import UserForm


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'bio',
            'phone_number',
            'birth_date',
            'profile_image'
        ]