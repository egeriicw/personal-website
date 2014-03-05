from flask import Blueprint

resume = Blueprint('resume', __name__)

@resume.route('/')
def index():
	return "Resume Placeholder"