from flask import Flask
from controllers.brain_dead_controller import brain_blueprint
from controllers.index_controller import index_blueprint
from controllers.supreme_controller import supreme_blueprint
from controllers.sign_up_controller import sign_up_blueprint
from controllers.login_controller import login_blueprint

def register_routes(app: Flask) -> None:
    """Central router to register all controller Blueprints."""
    app.register_blueprint(index_blueprint)
    app.register_blueprint(brain_blueprint)
    app.register_blueprint(supreme_blueprint)
    app.register_blueprint(sign_up_blueprint)
    app.register_blueprint(login_blueprint)
