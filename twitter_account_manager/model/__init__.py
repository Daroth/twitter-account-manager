from .. import db
from .account import Account

def reset_db():
	db.drop_all()
	db.create_all()