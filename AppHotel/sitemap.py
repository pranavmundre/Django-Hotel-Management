from django.contrib.sitemaps import Sitemap
from AppAdmin.models import Room

class HotelSitemap(Sitemap):
	changefreq = 'weekly'
	priority = 0.5

	def items(self):
		return Room.objects.all()