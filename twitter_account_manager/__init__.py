from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('twitter_account_manager.config.Config')
app.config.from_envvar('TWITTER_ACCOUNT_MANAGER_LOCAL_SETTINGS', silent=True)

if app.config['DEBUG']:
	toolbar = DebugToolbarExtension(app)

db = SQLAlchemy(app)

from .blueprints import web

app.register_blueprint(web.blueprint, url_prefix='/')