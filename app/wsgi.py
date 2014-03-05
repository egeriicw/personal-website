from flask import Flask

#from .extensions import db, googlelogin
from .views import root, admin, resume

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('app.config')
app.config.from_pyfile('application.cfg', silent=True)

#db.init_app(app)
#googlelogin.init_app(app)

app.register_blueprint(root)
app.register_blueprint(disclaimer, url_prefix='/dislaimer')
app.register_blueprint(resume, url_prefix='/resume')

application = app
