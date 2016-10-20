#!/usr/bin/env python
# coding=utf-8
#creat_app

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_script import Manager
from flask_moment import Moment
from flask_wtf import Form
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_pagedown import PageDown
from config import config


bootstrap=Bootstrap()
moment=Moment()
db=SQLAlchemy()
loginm=LoginManager()
loginm.session_protection='strong'
loginm.login_view='auth.login'
pagedown=PageDown()

def create_app(config_name):
    app=Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    loginm.init_app(app)
    pagedown.init_app(app)

    from .main import main as main_buleprint

    app.register_blueprint(main_buleprint)

    from .auth import auth as auth_blueprint

    app.register_blueprint(auth_blueprint,url_prefix='/auth')



    return app
