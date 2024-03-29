"""
    Apache License 2.0 Copyright (c) 2023 Pavel Bystrov
    Flask web-app for style extraction from stories
"""
from flask import Flask, render_template
from flask_login import LoginManager
from webapp.db import DB
from webapp.user.models import User
from webapp.user.views import blueprint as user_blueprint


def create_app():
    """ create app """
    app = Flask(__name__, static_url_path="/", static_folder="/")
    app.config.from_pyfile("config.py")
    login_mgr = LoginManager()
    login_mgr.init_app(app)
    login_mgr.login_view = "user.login"
    DB.init_app(app)
    app.register_blueprint(user_blueprint)

    @login_mgr.user_loader
    def load_user(user_id):
        """ load user """
        user = User.query.get(user_id)
        return user

    @app.route("/")
    def index():
        """ main page """
        return render_template("index.html")

    return app
