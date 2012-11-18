from twitter_account_manager import app
from twitter_account_manager.model import reset_db
from flask.ext.script import Manager
from flask.ext.script import Command

class CommandResetDb(Command):
	def run(self):
		reset_db()


if __name__ == '__main__':
	manager = Manager(app)
	manager.add_command('reset_db', CommandResetDb())
	manager.run()