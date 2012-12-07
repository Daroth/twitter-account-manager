from flask_oauth import OAuth
from .. import app
from ..model.account import Account
from .. import db

oauth = OAuth()
twitter = oauth.remote_app(__name__,
	base_url=app.config['TWITTER_BASE_URL'],
	request_token_url=app.config['TWITTER_REQUEST_TOKEN_URL'],
    access_token_url=app.config['TWITTER_ACCESS_TOKEN_URL'],
    authorize_url=app.config['TWITTER_AUTHOTIZE_URL'],
    consumer_key=app.config['TWITTER_CONSUMER_KEY'],
    consumer_secret=app.config['TWITTER_CONSUMER_SECRET'])

def save_token(token, secret):
	account = Account(oauth_token=token,
		oauth_secret=secret)
	db.session.add(account)
	db.session.commit()
	return True

def get_all():
	return Account.query.all()
