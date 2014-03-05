from flask import Blueprint, render_template

disclaimer = Blueprint('disclaimer', __name__)

@disclaimer.route('/')
def index():
	return render_template('dislaimer.html')
