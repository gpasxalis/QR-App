import os

from flask import Flask
from flask_elasticsearch import FlaskElasticsearch

def create_app():

	# common prefix for all routes in blueprints
	APP_URL_PREFIX = os.environ.get('MY_APP_PREFIX',None)
	# common prefix will also be prefix for static files
	APP_STATIC_URL = '/static'
	APP_STATIC_FOLDER = 'static'
	if APP_URL_PREFIX:
		APP_STATIC_URL = APP_URL_PREFIX + APP_STATIC_URL


	app = Flask(__name__, static_folder=APP_STATIC_URL ,static_url_path=APP_STATIC_URL)

	# configure elastic
	es.init_app(app)



	# register all blueprints
	from .views import blueprints
	for bp in blueprints:
		app.register_blueprint(bp,url_prefix=APP_URL_PREFIX)



	return app


es = FlaskElasticsearch()
app = create_app()