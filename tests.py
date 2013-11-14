import unittest
import routes
import happysad

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
		self.assertEquals(None, routes.get_location_data(""))

	def test_city_name(self):
		"""
		Tests only having a city name as input
		"""
		lat_lon = routes.get_location_data("Sydney")
		lat_lon = (round(lat_lon[0], 2), round(lat_lon[1], 2))
		self.assertEquals((-33.85, 151.22), lat_lon)

	def test_state_name(self):
		"""
		Tests only having a state name as input
		"""
		lat_lon = routes.get_location_data("Illinois")
		lat_lon = (round(lat_lon[0], 2), round(lat_lon[1], 2))
		self.assertEquals((40.08, -89.43), lat_lon)

	def test_country_name(self):
		"""
		Tests only having a country name as input
		"""
		lat_lon = routes.get_location_data("USA")
		lat_lon = (round(lat_lon[0], 2), round(lat_lon[1], 2))
		self.assertEquals((39.78, -100.45), lat_lon)

	def test_imaginary_name(self):
		"""
		Tests a place that doesn't exist
		"""
		self.assertEquals(None, routes.get_location_data("eskjfbwlkej"))

	def test_get_set_total_empty_file(self):
		"""
		Tests the get and set total on an empty file
		"""
		f = open("counts.txt", "r+")
		f.truncate()
		happysad.get_set_total(0, 0)
		self.assertEquals(0, int(f.readline()))
		self.assertEquals(0, int(f.readline()))
		f.close()

	def test_get_set_total_valid(self):
		f = open("counts.txt", "r")
		total1 = 10 + int(f.readline())
		total2 = 10 + int(f.readline())
		f.close()
		happysad.get_set_total(10, 10)
		f = open("counts.txt", "r")
		self.assertEquals(total1, int(f.readline()))
		self.assertEquals(total2, int(f.readline()))
		f.close()

	def test_get_strings_both_happy(self):
		"""
		Tests a total happy string and a delta happy
		DH, DS, TH, TS
		"""
		happy = "Yay! Twitter is happy!"
		a, b = happysad.get_strings(1, 0, 1, 0)
		self.assertEquals(a, happy)
		self.assertEquals(b, "...And it's getting happier!")

	def test_get_strings_total_happy(self):
		"""
		Tests a total happy and a delta sad
		"""
		happy = "Yay! Twitter is happy!"
		a, b = happysad.get_strings(0, 1, 1, 0)
		self.assertEquals(a, happy)
		self.assertEquals(b, "But it's getting sadder.  Spread some love... call your Mom")

	def test_get_strings_both_sad(self):
		"""
		Tests a total sad and a delta sad
		"""
		sad = "Aww.  Twitter is sad =( You guys suck."
		a, b = happysad.get_strings(0, 1, 0, 1)
		self.assertEquals(a, sad)
		self.assertEquals(b, "Everyone is miserable.  World is ending.  Whatever")

	def test_get_strings_total_sad(self):
		"""
		Tests a total sad and a delta happy
		"""
		sad = "Aww.  Twitter is sad =( You guys suck."
		a, b = happysad.get_strings(1, 0, 0, 1)
		self.assertEquals(a, sad)
		self.assertEquals(b, "Well, someone is being happy somewhere.  There's still hope")


suite = unittest.TestLoader().loadTestsFromTestCase(Tests)
unittest.TextTestRunner(verbosity=2).run(suite)