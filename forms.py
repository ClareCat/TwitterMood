from flask.ext.wtf import Form
from wtforms import TextField, RadioField

class optionsForm(Form):
	"""
	Form for options pane
	"""
	location = TextField("Location: ")

class analyzeForm(Form):
	"""
	Form for deciding whether a tweet is positive or negative
	"""
	mood = TextField("Idk what radio buttons are")