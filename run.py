from flask import Flask
"""
Imports are needed for database code
"""
#from flask.ext.sqlalchemy import SQLAlchemy
#from flask.ext.heroku import Heroku
app = Flask(__name__)
app.secret_key = 'a'
app.debug = True
"""
# This code is needed for when database is added
heroku = Heroku(app)
db = SQLAlchemy(app)
db.init_app(app)
"""