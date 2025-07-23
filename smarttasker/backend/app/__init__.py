from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SECRET_KEY'] = 'secret-key'
    app.config['JWT_SECRET_KEY'] = 'jwt-secret'

    db.init_app(app)
    jwt.init_app(app)

    from .routes.auth import auth_bp
    from .routes.tasks import task_bp
    from .routes.habits import habit_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(task_bp)
    app.register_blueprint(habit_bp)

    return app
  