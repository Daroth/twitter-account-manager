from ..model.account import Account
from .twitter import twitter as t
from .. import app

@t.tokengetter
def get_twitter_token(token=None):
	app.logger.debug("get_twitter_token %s" % (token))
	account = Account.query.filter_by(oauth_token=token).first()
	return None if account is None else (account.oauth_token, account.oauth_secret)