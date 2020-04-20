from django.contrib import admin
from .models import UserDetail
# Register your models here.


from django.utils.safestring import mark_safe
from django.utils.html import format_html




class UserDetailEntry(admin.ModelAdmin):
	list_display = ( 'get_profile_image', 'user' , 'mobile_no', 'birth_date', 'gender')
	list_display_links = ( 'get_profile_image','user')
	# list_filter = ('created_date' , 'is_publish',)
	list_per_page = 10
	search_fields = [ 'user__username', 'mobile_no', 'birth_date']
	ordering = ['-user']
	fieldsets  = ( ('User info', {'fields':( 'user', 'mobile_no','birth_date', 'gender')}) , ('Profile picture', {'fields':('profile_image',)}))
	# list_editable = ('is_publish',  )
	# actions = ('set_to_publish', 'set_to_unpublish')
	# readonly_fields = ('created_date',)

	def get_profile_image(seft, request):
		img = '<img src="/media/'+str(request.profile_image)+'" title="'+str(request.user.username)+'" height="45">'
		return mark_safe(img)

	get_profile_image.short_description = "Profile image"

admin.site.register(UserDetail, UserDetailEntry)
