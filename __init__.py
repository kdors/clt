import os

from flask import Flask

def create_app(test_config=None):
    # create and configure app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config == None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # ensure instance path exists
    try: 
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # register blueprint for main page in app
    from . import clt_main
    app.register_blueprint(clt_main.bp)

    return app
