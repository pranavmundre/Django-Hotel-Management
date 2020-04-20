from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from .formsModel import CreateUserForm
from django.contrib import messages
# from django.contrib import sessions

from django.core.mail import send_mail, EmailMessage

# Create your views here.

# @api_view(['POST']) use above funtion on post method

def Test(request):
	context = {'title': 'Login', }
	# request.session["data12"] = 'set'
	if request.session.has_key("data12"):
		val = request.session["data12"] + '1'
	else:
		val = 'new session' 

	print("Session Val: ", val )
	# data = '<?xml version="1.0" encoding="UTF-8"?><site>	<url>text</url></site>'
	# return HttpResponse(  data, 'application/xml')
	return render( request, 'test.html',{'data':context})

# @login_required(login_url='login')
def index(request):
	return render( request, "index.html" )


def loginUser(request):
	context = {}
	message= ''
	next_url = request.get_full_path()
	try:
		redirect_url = next_url[next_url.index('?next=', 1):]
		redirect_url = redirect_url.replace('?next=', '')
	except Exception as e:
		redirect_url = ''
		# raise e

	if request.user.is_authenticated:
		return redirect("/user")
		
	if request.method == 'POST':
		username = request.POST['username'] 
		password = request.POST['password']

		user = auth.authenticate(request, username=username, password=password)
		if user is not None:
			login(request,user)
			if redirect_url:
				return redirect(redirect_url)
				
			if request.user.is_superuser:
				return redirect("/admin")

			return redirect("/user")
			# messages.info(request, 'Pass')
		else:
			messages.info(request, 'Username Or Password is incorrect')

	context = {'title': 'Login', }
	return render( request, "login.html", context)

def logoutUser(request):
	logout(request)
	return redirect("/login")


def register(request):
	message= ''
	form = CreateUserForm()

	form.fields['username'].widget.attrs.update(placeholder =  'Username' )
	form.fields['email'].widget.attrs.update(placeholder =  'Email' )
	form.fields['password1'].widget.attrs.update(placeholder =  'Password' )
	form.fields['password2'].widget.attrs.update(placeholder =  'Confirm Password' )
		
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid() :
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Account has created for '+ user)
			return redirect('loginUser')
	return render( request, "register.html" , {'title': 'Register', 'message': message, 'form':form})


def About_Us(request):
	context = {  }
	return render( request, "about-us.html", context)

def sendEmail(request):
	res = send_mail(
	    'Online Hotel Management11',
	    'Hi Pranav, Welcome',
	    'onlineexaminationportal54@gmail.com',
	    ['pmundre1@gmail.com'],
	    fail_silently=False,
	)
	return HttpResponse("sent " + str(res))

# from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt #//You can use or not use choice is left to you
def getData(request):
	if request.method == 'POST':
		data={'name':'Pranav', 'status':'1'}
		# if request.is_ajax:
		# 	data={'name':'Pranav', 'status':'1'}
		# else:
		# 	data={'status':'0','error':'method not supported'}
	else:
		data={'status':'3','error':'get method not supported'}
	return JsonResponse(data)



def sitemap(request, self):
	urlset  = {'location':'rest'} 
	return urlset 