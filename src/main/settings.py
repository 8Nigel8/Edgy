from flask import Flask
from flask_cors import CORS

from src.main.api.v1.collection import collection_bp
from src.main.api.v1.lexeme import lexeme_bp
from src.main.api.v1.paper import paper_bp
from src.main.config import config
from src.main.consts import API_VERSION
from src.main.error_handlers import add_error_handlers
from src.main.extention import db


class __PrefixMiddleware(object):

    def __init__(self, app, prefix=''):
        self.app = app
        self.prefix = prefix

    def __call__(self, environ, start_response):
        if environ['PATH_INFO'].startswith(self.prefix):
            environ['PATH_INFO'] = environ['PATH_INFO'][len(self.prefix):]
            environ['SCRIPT_NAME'] = self.prefix
            return self.app(environ, start_response)
        else:
            start_response('404', [('Content-Type', 'text/plain')])
            return ["This url does not belong to the app.".encode()]


def create_app(env):
    app = Flask(__name__)

    app.wsgi_app = __PrefixMiddleware(app.wsgi_app, prefix=f'/api/{API_VERSION}')

    app.config.from_object(config)

    db.init_app(app)
    CORS(app)

    app.register_blueprint(collection_bp)
    app.register_blueprint(paper_bp)
    app.register_blueprint(lexeme_bp)

    add_error_handlers(app, env)
    return app
