from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator , MaxValueValidator
from django.contrib.auth.models import User

from django.conf import settings
# Create your models here.
from AppUser.models import UserDetail

class Room(models.Model):
	room_no = models.PositiveIntegerField(unique=True , validators=[MinValueValidator(1)])
	room_type = models.CharField(max_length=100, unique=False )
	price = models.IntegerField()
	details = models.TextField()
	image = models.ImageField(upload_to = 'rooms/',null=True)
	is_publish = models.BooleanField(default=False, blank=False )
	created_date = models.DateTimeField(default=timezone.now )
	published_date = models.DateTimeField(blank=True, null=True)

	class Meta:
		db_table = "rooms"

	def __str__(self):
		return self.room_type

	def get_room_no(self):
		return self.room_no


class RoomOrder(models.Model):
	class Meta:
		db_table = "room_order"

	# """
	# def increament_order_no():
	# 	last_invoice = RoomOrder.objects.all().order_by('-order_no').last()
	# 	# print('Query: ', last_invoice.order_no)
	# 	# print('Query1: ', last_invoice.id)
	# 	if last_invoice.order_no is None:
	# 		return 'MAG0001'
	# 	else:
	# 		invoice_no = last_invoice.order_no
	# 		try:
	# 			invoice_int = int(invoice_no.split('MAG')[-1])
	# 		except Exception as e:
	# 			invoice_int = int(invoice_no)
	# 			# raise e
	# 		# check = RoomOrder.objects.get(order_no= invoice_int)[:1]
	# 		# if check:
	# 		# 	print("exit")
	# 		new_invoice_int = invoice_int + 1
	# 		new_invoice_no = str(new_invoice_int)
	# 	return new_invoice_no
	# """

	order_no = models.CharField( default='', max_length=255, unique=True, null=True, blank=True)
	room = models.ForeignKey('Room', on_delete=models.CASCADE)
	user = models.ForeignKey(settings.AUTH_USER_MODEL ,on_delete=models.CASCADE, null=True)
	check_in_date = models.DateTimeField(blank=True, null=True)
	check_out_date = models.DateTimeField(blank=True, null=True)
	occupancy = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)] )
	order_timestamp = models.DateTimeField(default=timezone.now )

	'''
	def save(self):
		if self.order_no is None:
			self.order_no = str(self.increament_order_no()) 

		# self.order_no = str(self.increament_order_no()) 
		print("Order: ",self.order_no)
		print("TT: ", self.id)	
		super().save()
	''' 	