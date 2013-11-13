from run import app
from flask import render_template
from TwitterAPI import TwitterAPI
import urllib2
import urllib
import json
import random


@app.route('/')
def index(location=None):
	"""
	Runs the code to determine the mood of twitter
	Renders the mood of twitter to the index page
	Default of no location entered which defaults to all of twitter
	"""
	if location:
		get_location_data(location)
	curr_string, delta_string = get_happy_sad(location)
	return render_template("index.html", curr=curr_string, delta=delta_string)

def get_happy_sad(location):

	happy_count, sad_count = get_happy_sad_count(location)
	#get count
	#get total
	#parse strings
	return happy_count, sad_count

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
	if location:
		happy_query['locations'] = '{0}, {1}'.format(location[0], location[1])
		sad_query['locations'] = '{0}, {1}'.format(location[0], location[1])
	happy = api.request('search/tweets', happy_query)
	sad = api.request('search/tweets', sad_query)
	for item in happy:
		happy_count += 1
	for item in sad:
		sad_count += 1
	return happy_count, sad_count


def get_location_data(location):
	"""
	Gets location input as a string from user and converts it to latitude and longitude using openstreetmap
	Based on code found on stackoverflow (I lost the link =( )
	Returns the location data as latitude and longitude
	Returns None of location was empty of invalid
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
			location = None
	else:
		location = None
	return location


if __name__ == '__main__':
	app.run()