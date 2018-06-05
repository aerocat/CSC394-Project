from django import forms
from django.contrib.auth.models import User
from accounts.models import Student
from django.contrib.auth.forms import UserChangeForm


class EditProfileForm(UserChangeForm):
    
    student_name_last = forms.CharField(label='Last_Name')

    class Meta:
        model = Student
        fields = (
            'student_id',
            'student_name_first',
            'student_name_last',
            'student_email',
			'password'
        )
