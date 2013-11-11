import unittest
import f_p_1

class Tests(unittest.TestCase):
	""" Tests for f_p_1 """
	
	def setUp(self):
		unittest.TestCase.setUp(self)

	def tearDown(self):
		unittest.TestCase.tearDown(self)

	def test_no_location(self):
		"""
		Tests no location output
		"""
		self.assertEquals("", f_p_1.get_location(""))

	def test_city_name(self):
		"""
		Tests only having a city name as input
		"""
		lat_lon = f_p_1.get_location("Sydney")
		lat_lon = (round(lat_lon[0], 2), round(lat_lon[1], 2))
		self.assertEquals((-33.85, 151.22), lat_lon)

	def test_state_name(self):
		"""
		Tests only having a state name as input
		"""
		lat_lon = f_p_1.get_location("Illinois")
		lat_lon = (round(lat_lon[0], 2), round(lat_lon[1], 2))
		self.assertEquals((40.08, -89.43), lat_lon)

	def test_country_name(self):
		"""
		Tests only having a country name as input
		"""
		lat_lon = f_p_1.get_location("USA")
		lat_lon = (round(lat_lon[0], 2), round(lat_lon[1], 2))
		self.assertEquals((39.78, -100.45), lat_lon)

	def test_imaginary_name(self):
		"""
		Tests a place that doesn't exist
		"""
		self.assertEquals("", f_p_1.get_location("eskjfbwlkej"))


suite = unittest.TestLoader().loadTestsFromTestCase(Tests)
unittest.TextTestRunner(verbosity=2).run(suite)