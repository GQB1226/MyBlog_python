#coding=utf-8

from flask_wtf import Form
from wtforms import StringField,SubmitField,PasswordField,BooleanField
from wtforms.validators import Required,Length,Email

class LoginForm(Form):
    email=StringField('Email',validators=[Required(),Email(),Length(1,64)])
    passwd=PasswordField("passwd",validators=[Required()])
    remeber_me=BooleanField("remeber me")
    submit=SubmitField('login')

