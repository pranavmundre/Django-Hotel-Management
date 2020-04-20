from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, Http404 

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone

from .models import Room, RoomOrder
from .formsModel import RoomForm 

from django.core import serializers
import json

from django.db.models import Q
# Create your views here.

# raise  Http404("Poll does not exist") //404 response

@login_required(login_url='/login')
def index(request):
	return render(request, 'AppAdmin/index.html' )

@login_required(login_url='/login')
def rooms(request):
	data = Room.objects.all()
	context = {'rooms_data': data}
	return render(request, 'AppAdmin/rooms.html', context)

@login_required(login_url='/login')
def addRoom(request):
	if request.method == "POST" :
		form = RoomForm(request.POST, request.FILES)
		form.published_date = timezone.now()
		is_publish = request.POST.get('is_publish', False);
		# form.is_publish = is_publish #get_value_of_checkbox(is_publish)
		print("Check: ",is_publish)

		if form.is_valid():
			form.save()
			form = RoomForm()
			messages.success(request, {'msg': 'Room added successfully', 'icon':'check', 'alert_box':'success'})
		else:
			print("Error: ",form.errors)
			messages.error(request, {'msg': 'Failed to add room', 'icon':'ban', 'alert_box':'danger'})
	else:
		form = RoomForm()

	context = {'form': form}
	return render(request, 'AppAdmin/add-room.html', context)

@login_required(login_url='/login')
def editRoom(request, get_room_no):
	if request.method == "POST" :
		messages.success(request, {'msg': 'Room added successfully ', 'icon':'check', 'alert_box':'success'})
	else:
		form = EditRoomForm()
	# 	messages.error(request, {'msg': 'Failed to add room', 'icon':'ban', 'alert_box':'danger'})
	rooms_data = Room.objects.all()
	
	# res = serializers.serialize( 'json' , rooms_data)
	context = {'form': form}
	# context = {'rooms_data': rooms_data}

@login_required(login_url='/login')
def bookingDetails(request):
	data = RoomOrder.objects.all().order_by('order_timestamp')
	print("Data: ", data)
	context = {'rooms_orders': data}
	return render(request, 'AppAdmin/booking-details.html', context)


@login_required(login_url='/login')
def profile(request):
	context = {}
	return render(request, 'AppAdmin/booking-details.html', context)

@login_required(login_url='/login')
def SaveRoomDetails(request):
	context = {'status' : 'failed', 'message' : '' }
		# context.update(data= 33)

	if request.method == 'POST':
		room_no = request.POST['room_no']
		room_type = request.POST['room_type']
		price = request.POST['price']
		details = request.POST['details']
		is_publish = request.POST.get('is_publish', False);
		data = Room.objects.get(room_no=room_no)
		data.room_type = room_type
		data.price = price
		data.details = details
		data.is_publish = get_value_of_checkbox(is_publish)

		data.save()
		context.update(status= 'success')
		context.update(message= ' Room updated successfully...')
	else:
		context.update(message= 'Invaild Request')

	return JsonResponse(context)

@login_required(login_url='/login')
def getRoomDetails(request):
	context = {}
	status = 'failed'
	message = ''
 
	if request.method == 'POST':
		r_no = str(request.POST['id'])
		if r_no:
			data = Room.objects.get(room_no=r_no)
			if data:
				# context = serializers.serialize("json", data)
				context = {
					'room_no':data.room_no,
					'room_type':data.room_type,
					'price': data.price,
					'image': 'media/'+str(data.image),
					'is_publish': data.is_publish,
					'details': str(data.details),

				}
				status = 'success'
				# return HttpResponse(context, content_type='text/json')
			else:
				message = 'No record found'
		else:
			message = 'invalid input'
	else:
		context = {'error':'method not supported'}
	return JsonResponse({'status':status, 'message':message, 'data':context})
	

@login_required(login_url='/login')
def dataTableAjax(request):
	table_data = []
	publish = ''
	db_column = ['image','room_no', 'room_type', 'price', 'details', 'is_publish']
	get_request = request.GET
	get_val =request.GET
	
	try:
		draw = request.GET.get('draw')
		start = int(request.GET.get('start'))
		length = int(request.GET.get('length'))
		search = request.GET.get('search[value]')
		order = request.GET.get('order[0][dir]')
		order_column = request.GET.get('order[0][column]')
	except Exception as e:
		start = 0
		length = 10
		search = ''
		# raise e

	filter_val = (
		Q(room_no__contains=search) | 
		Q(room_type__icontains=search) | 
		Q(price__contains=search) | 
		Q(details__icontains=search)
	)

	try:
		order_val = db_column[int(order_column)]
	except Exception as e:
		order_val = db_column[1]
		# raise e

	if order == 'desc' :
		order_val = "-" + str(order_val)

	all_data = Room.objects.all()
	if search:
		data = Room.objects.filter(filter_val).order_by(order_val)[start : start+length]
		f_data = Room.objects.filter(filter_val)
		recordsFiltered = f_data.count()
	else:
		data = Room.objects.filter(filter_val).order_by(order_val)[start : start+length]
		recordsFiltered = all_data.count()

	recordsTotal = all_data.count()

	for x in data:
		if x.is_publish == True:
			publish = '<i class="fas fa-check" style="color:green;"></i>'
		else:
			publish = '<i class="far fa-times-circle" style="color:red;"></i>'

		single_data = [
			'<img src="/media/'+str(x.image)+'" class="room-image">',
			x.room_no,
			x.room_type,
			x.price,
			x.details,
			publish,
			'<a id="EditRoom" onclick="EditMyRoom(this)"  href="/admin/room/edit/'+str(x.room_no)+'" room-no="'+str(x.room_no)+'" data-toggle="modal" data-target="#edit-room-modal" class="btn btn-info btn-sm">Edit</a>  <a href="#" room-no="'+str(x.room_no)+'" class="btn btn-danger btn-sm">Delete</a>'  
		]
		table_data.append(single_data)

	context = {
		"draw" : draw,
		"recordsTotal" : recordsTotal,
		"recordsFiltered" : recordsFiltered,
		"data" : table_data
	}
	return JsonResponse(context)


def get_value_of_checkbox(value):
	if value:
		value_s = 'True'
	else:
		value_s = 'False'
	return value_s