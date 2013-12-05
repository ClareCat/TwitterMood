from flask.ext.wtf import Form
from wtforms import TextField, RadioField, HiddenField

class optionsForm(Form):
	"""
	Form for options pane
	"""
	location = TextField("Location: ")

class analyzeForm(Form):
	"""
	Form for deciding whether a tweet is positive or negative
	"""
	tweet = HiddenField('None')
	actual = HiddenField('None')
	mood = RadioField("Is this positive or negative?", choices=[("positive", "positive"), ("negative", "negative")])