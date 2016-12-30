# -*- coding: utf-8 -*-

import json
import logging

from flask import current_app, Flask, redirect, request, url_for, render_template
from flask_restful import Api
import httplib2


def create_app(config, debug=False, testing=False, config_overrides=None):
    app = Flask(__name__, static_folder='statics')
    api = Api(app)
    app.config.from_object(config)

    app.testing = testing

    if config_overrides:
        app.config.update(config_overrides)

    # Configure logging
    if not app.testing:
        logging.basicConfig(level=logging.INFO)

    # Setup the data model.
    with app.app_context():
        model = get_model()
        model.init_app(app)

    ## Setup index to route /
    @app.route('/', methods=['GET'])
    def index():
        return render_template('index.html')

    ## Setup ApiController to route /api
    from .api_controller import ApiController
    api.add_resource(ApiController, '/api/<string:memo_id>')



    # Add an error handler. This is useful for debugging the live application,
    # however, you should disable the output of the exception for production
    # applications.
    @app.errorhandler(500)
    def server_error(e):
        return """
        An internal error occurred: <pre>{}</pre>
        See logs for full stacktrace.
        """.format(e), 500

    return app


def get_model():
    model_backend = current_app.config['DATA_BACKEND']
    if model_backend == 'cloudsql':
        from . import model_cloudsql
        model = model_cloudsql
    else:
        raise ValueError(
            "No appropriate databackend configured. "
            "Please specify cloudsql")

    return model

