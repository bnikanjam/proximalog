import os

from flask import Flask


# The Application Factory
def create_app(test_config=None):
    """Create and configure the Flask webapp"""
    # Configurations, registrations, and other setup the application needs
    # implemented inside this function, then the application will be returned.
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'proximalog.sqlite'),
    )

    if test_config is None:
        # load the instance config, if exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passes in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # quick test app running
    @app.route('/running')
    def running():
        return f'Hi! I am in {__name__} up and running...'

    from . import db
    db.init_app(app)

    # register authentication blueprint that has views to register new users, log in, and log out a user.
    from . import auth
    app.register_blueprint(auth.bp)

    return app
