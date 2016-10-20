#!/usr/bin/env python
# coding=utf-8
#this is config file for myblog app

import os

basedir = os.path.abspath(os.path.dirname(__file__))

print basedir

class Config:
    DEBUG=True
    SECRET_KEY='GQB1226gqb1226'
    SQLALCHEMY_COMMIT_ON_TEARDOWN=True

    @staticmethod
    def init_app(app):
        pass

class DBConfig(Config):
    SQLALCHEMY_DATABASE_URI='mysql://root:122600@localhost/test'
    #SQLALCHEMY_DATABASE_URI='sqlite:///'+os.path.join(basedir,'data.sqlite')


config={
    'default':DBConfig
}













