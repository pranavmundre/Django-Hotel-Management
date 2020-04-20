from django.test import TestCase

# Create your tests here.

import datetime

from django.utils import timezone

from .models import Room


class RoomTests(TestCase):

	def test_was_published_recently_with_future_question(self):
		"""
		was_published_recently() returns False for questions whose pub_date
		is in the future.
		"""
		time = timezone.now() + datetime.timedelta(days=30)
		date_val = Room(published_date=time)
		self.assertIs(date_val.get_room_no(), False)

