from flask import make_response
from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy

# local import
from alexaresponse import ResponseBuilder
from instance.config import app_config

# initialize sql-alchemy
db = SQLAlchemy()


def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    # Disabled track modifications for SQLAlchemy because it'll be deprecated
    # in future due to it's significant performance overhead
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Connected app to the DB
    db.init_app(app)

    from flask import request, jsonify, abort

    @app.route('/', methods=['GET'])
    def test():
        # TODO routing of requests
        message = "OttoBot server is running."

        welcome_response = ResponseBuilder.create_response(message)
        return ResponseBuilder.create_response(message)

    @app.route('/api/', methods=['POST'])
    def test_page():
        # TODO routing of requests
        message = """Hey, I'm Otto Investment bot, I' here to inform you about your investments. Do you want me to tell you a report on your portfolio? Or maybe information about specific stock? """
        reprompt_message = "Go on, tell me what can I do for you."

        return ResponseBuilder.create_response(message)\
            .with_reprompt(message=reprompt_message)

    return app
