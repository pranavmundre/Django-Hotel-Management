from django.forms import  Textarea, TextInput, IntegerField, ImageField, BooleanField, DateTimeField
from django import forms

from .models import Room 
 
class RoomForm(forms.ModelForm):
	room_no = forms.CharField(
	    max_length=250,
	    label = 'Room No.',
	    widget=forms.NumberInput(attrs={
	        'class': 'form-control',
	        'placeholder': 'Room No',
	        'title': 'Room No',
	        # 'autocomplete': 'off',
	        'min':'1'
	    }),
	)
	room_type = forms.CharField(
	    max_length=250,
	    label = 'Room type',
	    widget=forms.TextInput(attrs={
	        'placeholder' : 'Room Type',
	        'title' : 'Room Type',
	        'list':"room_type_list",
	        'class':'form-control',
	        'autocomplete':'off',
	    }),
	)
	price = forms.IntegerField(
	    label = 'Price',
	    widget=forms.TextInput(attrs={
	        'placeholder' : 'Price',
	        'title' : 'Price',
	        'class':'form-control',
	        # 'autocomplete':'off',
	    }),
	)
	details = forms.CharField(
	    max_length=250,
	    label = 'Details',
	    required=False,
	    widget=forms.Textarea(attrs={
	        'placeholder' : 'Details',
	        'title' : 'Details',
	        'class':'form-control textarea',
	        # 'required':'false',
	        'autocomplete':'off','cols': 80, 'rows': 5,
	    }),
	)
	image = forms.ImageField(
	    label = 'Room Image',
	    widget=forms.ClearableFileInput(attrs={
	        # 'placeholder' : 'Room Image',
	        'title' : 'Room Image',
	        'class':'custom-file-input',
	        'type': 'file',
	    }),
	)
	is_publish = forms.BooleanField(
	    label = 'Publish',
	    initial=True,
	    required=False,
	    widget=forms.CheckboxInput(attrs={
	        'placeholder' : 'Publish',
	        'title' : 'Publish',
	        # 'class':'form-control',
	    }),
	)
	# published_date = forms.DateTimeField(
	#     label = 'Publish Date',
	#     widget=forms.DateTimeInput(attrs={
	#         'placeholder' : 'Publish Date',
	#         'title' : 'Publish Date',
	#         'class':'form-control',
	#         'type':'datetime-local',
	#     }),
	# )
 
	class Meta:
		model = Room
		exclude = ( 'created_date', 'is_publish' )
