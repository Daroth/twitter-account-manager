from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash
from .. import app
from ..service.twitter import twitter
from ..service.twitter import get_all
from ..service.twitter import save_token


blueprint = Blueprint('web', __name__)



@blueprint.route('', methods=['GET', ])
def index():
	return render_template('web/index.html')

@blueprint.route('accounts', methods=['GET', ])
def accounts():
	accounts=get_all()
	app.logger.debug("web.accounts %s" % (accounts))
	return render_template('web/accounts.html', accounts=accounts)

@blueprint.route('request_new_account', methods=['GET', ])
def request_new_account():
	next = request.args.get('next') or request.referrer or None
	return twitter.authorize(callback=url_for('web.twitter_callback'))

@blueprint.route('twitter_callback', methods=['GET', ])
@twitter.authorized_handler
def twitter_callback(resp):
	next_url = request.args.get('next') or url_for('web.index' )
	if resp is None:
		app.logger.debug(">>> twitter_callback WRONG")
		flash('WRRRONG')
	else:
		app.logger.debug(">>> twitter_callback save %s %s" % (resp['oauth_token'], resp['oauth_token_secret']))
		if save_token(resp['oauth_token'], resp['oauth_token_secret']):
			flash('account created')
		else:
			flash('account alreay registred')
	return redirect(next_url)