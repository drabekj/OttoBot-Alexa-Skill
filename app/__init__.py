from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy

# local import
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

    return app
