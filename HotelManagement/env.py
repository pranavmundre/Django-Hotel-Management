
class Credentials:
	SECRET_KEY = 'o463nqy(*ctqiatyasts^t&c_60wp1#j2us%e#v77$_lf=^mjq'	
	DEBUG = True
	ALLOWED_HOSTS = ['*']
	
	# GitHub Keys
	SOCIAL_AUTH_GITHUB_KEY = 'fa400f71c8afeb6b5bc3'
	SOCIAL_AUTH_GITHUB_SECRET = '8a5e34dc98377d62475a50ec8a3d3ee994112cba'

	# Facebook Keys
	SOCIAL_AUTH_FACEBOOK_KEY = '657689641725413'  # App ID
	SOCIAL_AUTH_FACEBOOK_SECRET = '6b4db543ffa082b422c705fcce19f9ad'  # App Secret

	#Twitter Keys
	SOCIAL_AUTH_TWITTER_KEY = '0svhh85HsaBahhXlYCuQEVmbc'
	SOCIAL_AUTH_TWITTER_SECRET = '2zsgeEeh759XiBymwnZS1b9j0UD2mNwv96rlTulAqGfx43MLms'

	# MAIL SETTING
	EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
	EMAIL_HOST = 'smtp.gmail.com'
	EMAIL_PORT = 587
	EMAIL_HOST_USER = 'onlineexaminationportal54@gmail.com'
	EMAIL_HOST_PASSWORD = 'Online@123'
	EMAIL_USE_TLS = True
	EMAIL_USE_SSL = False

	# GOOGLE RECHAPCHA
	# V3
	GOOGLE_RECAPTCHA_SITE_KEY_V3 = '6LclH-cUAAAAAFfy6MJS9Xyh-d5SR0uWbUU4C2TO'
	GOOGLE_RECAPTCHA_SECRET_KEY_V3 = '6LclH-cUAAAAAIpw0WzGiHGes-qk4c1iq2-VXqL2'

	# V2
	GOOGLE_RECAPTCHA_SITE_KEY_V2 = '6LclH-cUAAAAAFfy6MJS9Xyh-d5SR0uWbUU4C2TO'
	GOOGLE_RECAPTCHA_SECRET_KEY_V2 = '6LczIecUAAAAAOXBa68zyUFAMMPjANEKzWQQr6rP'