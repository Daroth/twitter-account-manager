from .. import db

class Account(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	oauth_token = db.Column(db.String, unique=True)
	oauth_secret = db.Column(db.String)

	def __init__(self, oauth_token, oauth_secret):
		self.oauth_token = oauth_token
		self.oauth_secret = oauth_secret

	def __repr__(self):
		return u'<Account oauth_token = %s ;  oauth_secret = %s>' % (self.oauth_token, self.oauth_token)
