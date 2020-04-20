from .models import UserDetail

from django import forms


class ProfileForm(forms.ModelForm):
	class Meta: 
		model = UserDetail
		fields = [
			'birth_date',
			'profile_image',
		]  