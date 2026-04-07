from flask import Flask

from EnvironmentMonitoringSystem import pages # type: ignore
def create_app():
    app = Flask(__name__)
    app.register_blueprint(pages.bp)
    return app