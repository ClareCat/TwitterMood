from TwitterAPI import TwitterAPI
from random import random

def get_happy_sad(location):
	"""
	Central function for getting the happy and sad counts and strings
	Returns the correct for the situation
	"""
	curr_happy, curr_sad, tweet = get_happy_sad_count(location)
	total_happy, total_sad = get_set_total(curr_happy, curr_sad)
	curr_string, delta_string = get_strings(curr_happy, curr_sad, total_happy, total_sad)
	return curr_string, delta_string, tweet

def get_strings(curr_happy, curr_sad, total_happy, total_sad):
	"""
	Translates the different levels of happiness into strings
	Returns the correct string
	"""
	happy = "Yay! Twitter is happy!"
	sad = "Aww.  Twitter is sad =( You guys suck."
	if curr_happy >= curr_sad and total_happy >= total_sad:
		return happy, "...And it's getting happier!"
	elif curr_happy < curr_sad and total_happy >= total_sad:
		return happy, "But it's getting sadder.  Spread some love... call your Mom"
	elif curr_happy >= curr_sad and total_happy < total_sad:
		return sad, "Well, someone is being happy somewhere.  There's still hope"
	elif curr_happy < curr_sad and total_happy < total_sad:
		return sad, "Everyone is miserable.  World is ending.  Whatever"
	else:
		return "OH NO!", "SHIT GOT FUCKED UP!"

def get_set_total(happy_count, sad_count):
	"""
	Takes the happy count and sad count and adds it to the running totals
	Reads and writes these totals to file for later use.  
	Returns the total happy and the total sad
	"""
	f = open("counts.txt", "r+")
	f.seek(0)
	total_happy = 0
	total_sad = 0
	try:
		total_happy = int(f.readline())
		total_sad = int(f.readline())
	except ValueError:
		pass
	total_happy += happy_count
	total_sad += sad_count
	f.seek(0)
	f.write(str(total_happy) + '\n')
	f.write(str(total_sad) + '\n')
	f.truncate()
	f.close()
	return total_happy, total_sad

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
	tweet = (happy[int(random()*len(happy))], "=)")
	if random()*2 < 1:
		tweet = (sad[int(random()*len(sad))], "=(")
	return happy_count, sad_count, tweet
