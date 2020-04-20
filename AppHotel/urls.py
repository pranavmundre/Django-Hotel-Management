from django.urls import path
from django.contrib.auth import views as auth_views

from.import views

urlpatterns = [
	path('', views.index, name='Home'  ),
	path('login/', views.loginUser, name='loginUser'  ),
	path('register/', views.register, name='register'  ),


	path('about-us/', views.About_Us, name='About_Us'  ),
	path('user/logout/', views.logoutUser, name='logoutUser'  ),
	path('admin/logout/', views.logoutUser, name='logoutUser'  ),

	path('send-email/', views.sendEmail, name='sendEmail'  ),
	path('ajax/get', views.getData, name='getData'  ),

	path('test/', views.Test, name='Test'  ),



	path('reset_password/', 
		auth_views.PasswordResetView.as_view(template_name="password_reset_template/password_reset.html") , 
		name="reset_password" 
	),
	path('reset_password_sent/', 
		auth_views.PasswordResetDoneView.as_view(template_name="password_reset_template/password_reset_sent.html"), 
		name="password_reset_done"  
	),
	path('reset/password/<uidb64>/<token>/', 
		auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_template/password_reset_confirm.html"), 
		name="password_reset_confirm"  
	),
	path('reset_password_done/', 
		auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_template/password_reset_done.html"), 
		name="password_reset_complete"  
	),
	path('reset_password_done/', 
		auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_template/password_reset_done.html"), 
		name="login"  
	),


]


