from run import app, db
from flask import render_template, request, url_for, redirect
import urllib2
import urllib
import json
from happysad import get_happy_sad
from forms import optionsForm, analyzeForm
from models import Analysis


@app.route('/', methods=['GET', 'POST'])
def index(location=None, new_loc=False):
	"""
	Runs the code to determine the mood of twitter
	Renders the mood of twitter to the index page
	If post request also inserts the analysis into the table
	Default of no location entered which defaults to all of twitter
	"""
	correct_str = None
	if location:
		get_location_data(location)
	if request.method == 'POST' and not new_loc:
		form = analyzeForm()
		newAnalysis = Analysis(form.tweet.data, form.mood.data, form.actual.data)
		db.session.add(newAnalysis)
		db.session.commit()
		if form.mood.data == form.actual.data:
			correct_str = "You and Twitter agree that \"{a}\" is {b}".format(a=form.tweet.data.encode("utf-8"), b=form.actual.data)
		else:
			correct_str = "Twitter actually thinks that \"{a}\" is {b}.  Maybe you're confused.  Twitter wouldn't lie.".format(a=form.tweet.data.encode("utf-8"), b=form.actual.data)
		correct_str = unicode(correct_str, errors='ignore')
	curr_string, delta_string, tweet = get_happy_sad(location)
	analysis = analyzeForm()
	analysis.tweet.label = tweet[0]
	analysis.tweet.data = tweet[0]
	analysis.actual.data = tweet[1]
	return render_template("index.html", curr=curr_string, delta=delta_string, loc=optionsForm(), analyze=analysis, correct=correct_str)

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
	return index(location, True)


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