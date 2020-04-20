from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppAdmin.models import Room
from .models import UserDetail
from .formModels import ProfileForm
from django.contrib.auth.decorators import login_required

from social_django.models import UserSocialAuth
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User

from django.contrib import messages

from django.contrib.auth import login, authenticate, logout

# Create your views here.

@login_required(login_url='/login')
def index(request):
	if request.user.is_superuser:
		return redirect("/admin")
	user_id = request.user.id

	try:
		user_data = UserDetail.objects.get(user = user_id )
	except Exception as e:
		user_data = ''
		pass

	context = {'user_profile':user_data}
	return render( request, "user/index.html", context)

@login_required(login_url='/login')
def rooms(request):
	data = Room.objects.all()
	context = {'rooms_data': data}
	# return HttpResponse("Admin"+res)
	return render(request, 'user/rooms.html', context)

@login_required(login_url='/login')
def settings(request):
    user = request.user

    try:
        github_login = user.social_auth.get(provider='github')
    except UserSocialAuth.DoesNotExist:
        github_login = None

    try:
        twitter_login = user.social_auth.get(provider='twitter')
    except UserSocialAuth.DoesNotExist:
        twitter_login = None

    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    return render(request, 'user/settings.html', {
        'github_login': github_login,
        'twitter_login': twitter_login,
        'facebook_login': facebook_login,
        'can_disconnect': can_disconnect
    })


@login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'user/password.html', {'form': form})