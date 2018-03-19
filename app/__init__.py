from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy

# initialize sql-alchemy
from app.utils.MyError import UnknownRequestError
from app.utils.alexa.request import alexa_request
from app.utils.alexa.response import ResponseBuilder

db = SQLAlchemy()

# local import
from app.handle_intent import handle_intent
from app.handle_launch import handle_launch
from instance.config import app_config


def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    # Disabled track modifications for SQLAlchemy because it'll be deprecated
    # in future due to it's significant performance overhead
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Connected app to the DB
    db.init_app(app)

    print("Config: " + config_name)

    @app.route('/', methods=['GET'])
    def test():
        # TODO makes POST requests freeze (restart server needed)
        message = "OttoBot server is running."
        return ResponseBuilder.create_response(message=message) \
            .set_session("RUNNING", "")

    @app.route('/api/', methods=['POST'])
    @alexa_request
    def handle_request(request):
        """
        Route POST request by request type.
        :type request: AlexaRequest
        """
        if request.request_type() == "LaunchRequest":
            return handle_launch(request)
        elif request.request_type() == "IntentRequest":
            return handle_intent(request)
        elif request.request_type() == "Dialog.Delegate":
            return handle_intent(request)
        elif request.request_type() == "SessionEndedRequest":
            # TODO SessionEndedRequest
            pass
        else:
            raise UnknownRequestError(request.request_type())

    return app
