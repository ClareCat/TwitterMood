from run import app
from flask import render_template, request, url_for, redirect
import urllib2
import urllib
import json
from happysad import get_happy_sad
from forms import optionsForm, analyzeForm


@app.route('/')
def index(location=None):
	"""
	Runs the code to determine the mood of twitter
	Renders the mood of twitter to the index page
	Default of no location entered which defaults to all of twitter
	"""
	if location:
		get_location_data(location)
	curr_string, delta_string, tweet = "", "", ""#get_happy_sad(location)
	return render_template("index.html", curr=curr_string, delta=delta_string, loc=optionsForm(), analyze=analyzeForm())

@app.route('/location', methods=['GET', 'POST'])
def location():
	"""
	Gets the location option
	Returns the index with the data from that location
	"""
	location = None
	if request.method == 'POST':
		form = optionsForm()
		location = form.location.data
	return index(location)


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