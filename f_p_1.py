from TwitterAPI import TwitterAPI
from time import sleep
import urllib2
import urllib
import json


def main():
	"""
	main function - runs all the input and output.  Also makes the calls to associated functions
	"""
	location = get_location(raw_input("Enter a location: "))
	happy_count = 0
	sad_count = 0
	while(True):
		h, s = get_happy_sad_count(location)
		happy_count += h
		sad_count += s
		curr_mood = (" and it's getting happier =)" if h >= s else " and it's getting sadder =(")
		total_mood = ("Twitter is happy" if happy_count >= sad_count else "Awww, Twitter is sad")
		print total_mood + curr_mood
		sleep(2)

def get_happy_sad_count(location):
	"""
	Gets the happy and sad count on the current query
	Returns the happy count and the sad count
	"""
	api = TwitterAPI('SSuspEaugDP7vcITlMA', '6FdUGOTcqlcoufjz62frkKHJ5cgm1vnaIHqjlboOHg', '78925893-xs57TGEPdYpSmbfBKi1XPKVliu5i2TrDRFOEPwVmt', 'fAVXZr4cnEi2hNtVvLyh68mxh4JysMbyJVlBbefhLvf5v')
	happy_count = 0
	sad_count = 0
	happy_query = {'q':':)', 'lang':'en', 'count':'100', 'result_type':'recent'}
	sad_query = {'q':':(', 'lang':'en', 'count':'100', 'result_type':'recent'}
	if location != "":
		happy_query['locations'] = '{0}, {1}'.format(location[0], location[1])
		sad_query['locations'] = '{0}, {1}'.format(location[0], location[1])
	happy = api.request('search/tweets', happy_query)
	sad = api.request('search/tweets', sad_query)
	for item in happy:
		happy_count += 1
	for item in sad:
		sad_count += 1
	return happy_count, sad_count

def get_location(location):
	"""
	Gets location input as a string from user and converts it to latitude and longitude using openstreetmap
	Based on code found on stackoverflow (I lost the link =( )
	Returns the location data as latitude and longitude
	"""
	if location != "":
		url = 'http://nominatim.openstreetmap.org/search?'
		params = urllib.urlencode(dict(q=location, format='json'))
		response = urllib.urlopen(url+params)
		response = response.read()
		if len(response) != 2:
			data = json.loads(response)[0]
			location = (float(data['lat']), float(data['lon']))
		else:
			location = ""
	return location


		

if __name__ == '__main__':
	main()