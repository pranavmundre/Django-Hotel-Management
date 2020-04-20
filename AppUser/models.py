from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator , MaxValueValidator
from django.contrib.auth.models import User

from django.conf import settings
# Create your models here.


GENDER = (
	( '1' , 'Male'),
	( '0' , 'Female'),
	( '2' , 'Other'),
)

class UserDetail(models.Model):

	user = models.OneToOneField(User, null=True , on_delete=models.CASCADE)
	birth_date = models.DateField(null=True, blank=True)
	mobile_no = models.CharField(null=True, blank=True, max_length=30)
	gender = models.CharField( max_length=1, choices = GENDER, null=True, blank=True,)
	address = models.CharField( max_length=100, null=True, blank=True,)
	profile_image = models.ImageField(default='images/default-avtar.png', upload_to='users/', null=True, blank=True)


	def __str__(self):
		return self.user.username	

	class Meta:
		db_table = "user_details"