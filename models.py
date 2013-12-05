from run import db

"""
Object for the analysis table
"""
class Analysis(db.Model):
	__tablename__ = "tweets"
	id = db.Column(db.Integer, primary_key=True)
	tweet = db.Column(db.String(200))
	analysis = db.Column(db.String(10))
	actual = db.Column(db.String(10))

	"""
	Initialises the table
	"""
	def __init__(self, tweet, analysis, actual):
		self.tweet = tweet
		self.analysis = analysis
		self.actual = actual