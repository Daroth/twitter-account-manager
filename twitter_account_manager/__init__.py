from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config.from_object('twitter_account_manager.config.Config')
app.config.from_envvar('TWITTER_ACCOUNT_MANAGER_LOCAL_SETTINGS', silent=True)

if app.config['DEBUG']:
	toolbar = DebugToolbarExtension(app)

from .blueprints import web

app.register_blueprint(web.blueprint, url_prefix='/')