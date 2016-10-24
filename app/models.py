#!/usr/bin/env python
# coding=utf-8

from . import db
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime
from . import loginm

@loginm.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))


class Role(db.Model):
    __tablename__='roles'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64),unique=True)

    users=db.relationship('User',backref='role')

class User(UserMixin,db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(64),unique=True,index=True)
    username=db.Column(db.String(64),unique=True,index=True)
    #passwd=db.Column(db.String(128))
    passwdhs=db.Column(db.String(128))

    role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))
    posts=db.relationship('Post',backref='author',lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('can\'t read!')

    @password.setter
    def password(self,psw):
        self.passwdhs=generate_password_hash(psw)

    def verify_psw(self,psw):
        return check_password_hash(self.passwdhs,psw)


class Post(db.Model):
    __tablename__='post'
    id=db.Column(db.Integer,primary_key=True)
    fileId=db.Column(db.Integer,unique=True)
    title=db.Column(db.String(128),unique=True)
    body=db.Column(db.Text)
    timestamp=db.Column(db.DateTime,index=True,default=datetime.utcnow)
    author_id=db.Column(db.Integer,db.ForeignKey('users.id'))
    comments=db.Column(db.Integer,default=0)
    totalNum=db.Column(db.Integer,default=0)

class Comment(db.Model):
    __tablename__='comment'
    id=db.Column(db.Integer,primary_key=True)
    fileId=db.Column(db.Integer,db.ForeignKey('post.fileId'))
    Sid=db.Column(db.Integer,index=True)
    Tid=db.Column(db.Integer)
    comment=db.Column(db.Text)
    user=db.Column(db.String(128))
    datetime=db.Column(db.DateTime,index=True,default=datetime.utcnow)


