from flask.ext.wtf import Form
from wtforms import TextField

class optionsForm(Form):
	"""
	Form for options pane
	"""
	location = TextField("Location: ")