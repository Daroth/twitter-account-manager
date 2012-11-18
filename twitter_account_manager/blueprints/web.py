from flask import Blueprint
from flask import render_template

blueprint = Blueprint('web', __name__)

@blueprint.route('', methods=['GET', ])
def index():
	return render_template('web/index.html')

@blueprint.route('accounts', methods=['GET', ])
def accounts():
	return render_template('web/accounts.html')