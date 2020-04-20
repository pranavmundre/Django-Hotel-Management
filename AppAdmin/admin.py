from django.contrib import admin
from django.contrib.auth.models import Group, User
# from django.contrib import messages

from .models import Room, RoomOrder

from django.utils.safestring import mark_safe
from django.utils.html import format_html
# Register your models here.




class RoomAdminEntry(admin.ModelAdmin):
	list_display = ( 'room_image' ,'room_no', 'room_type', 'price','render_details', 'is_publish', 'created_date')
	list_display_links = ( 'room_type','room_image')
	list_filter = ('created_date' , 'is_publish',)
	list_per_page = 10
	search_fields = ['room_type', 'room_no', 'price', 'details']
	ordering = ['-created_date']
	fields = (('room_no', 'price'), 'room_type',  'details', 'image', 'is_publish', 'published_date','created_date')
	actions = ('set_to_publish', 'set_to_unpublish')
	readonly_fields = ('created_date',)
	# list_editable = ('is_publish',  )
	# prepopulated_fields = {"price": ("details", )}
	# list_select_related = True
	# exclude = ('summary_html', 'body_html')

	# def formfield_for_dbfield(self, db_field, **kwargs):
	# 	formfield = super().formfield_for_dbfield(db_field, **kwargs)
	# 	if db_field.name == 'body':
	# 		formfield.widget.attrs.update({
 #                'rows': 60,
 #                'style': 'font-family: monospace; width: 810px;',
	# 		})
	# 	return formfield

	def room_image(self, obj):
		data = '<img src="/media/'+ str(obj.image)+'" height="40"> '
		return mark_safe(data)

	def render_details(self, request):
		data = str(request.details)
		str_len  = len(data)
		if str_len > 20:
			data = data[:20] + '...'
		return data
		

	def set_to_publish(self, request, queryset):
		count = queryset.update(is_publish=True)
		# for item in queryset.iterator():
		# 	item.is_publish = 'True'
		# 	item.save()
		self.message_user(request, str(count) +' rooms have been published' )

	def set_to_unpublish(self, request, queryset):
		count = queryset.update(is_publish='False')
		self.message_user(request, str(count) +'rooms have been unpublished',)

	room_image.short_description = "Image"
	render_details.short_description = "details"
	set_to_publish.short_description = "Publish"
	set_to_unpublish.short_description = "UnPublish"
		

class RoomOrderAdminEntry(admin.ModelAdmin):
	list_display = ( 'get_user_name', 'get_room_no', 'order_no', 'get_room_type', 'check_in_date', 'check_out_date', 'occupancy' )
	list_display_links = ( 'get_user_name','get_room_type')
	list_filter = ('check_in_date' , 'check_out_date',)
	list_per_page = 10
	search_fields = ['get_user_name',]
	readonly_fields = ('order_no',)
	# fields = ( 'order_no', ('room', 'user'), 'check_in_date', 'check_out_date', 'occupancy', 'order_timestamp')

	# raw_id_fields = ['room_id']
	readonly_fields = ('order_timestamp',)
	# exclude = ('order_no',)


	def get_room_no(self, request):
		return request.room.room_no

	def get_room_type(self, obj):
		return obj.room.room_type

	def get_user_name(self, obj):
		name = obj.user.first_name
		if not name:
			name =  obj.user.username
		else:
			name =  obj.user.first_name + " " + obj.user.last_name
			pass

		return name

	# get_room_type.admin_order_field  = 'room_type'  #Allows column order sorting
	get_room_no.short_description = 'Room No'  #Renames column head
	get_room_type.short_description = 'Room Type'  #Renames column head

	# get_user_name.admin_order_field  = 'first_name' 
	get_user_name.short_description = 'User Name'  


admin.site.register(Room, RoomAdminEntry)
admin.site.register(RoomOrder, RoomOrderAdminEntry)
admin.site.unregister(Group)