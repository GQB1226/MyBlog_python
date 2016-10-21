#!/usr/bin/env python
# coding=utf-8

from flask_wtf import Form
from wtforms import StringField,SubmitField,TextField
from wtforms.fields import TextAreaField
from wtforms.validators import DataRequired

class NameForm(Form):
    name=StringField('What\'s your name?',validators=[DataRequired()])
    #name=StringFiled('What\'s your name?',validators=[Required()])
    submit=SubmitField('Submit')

class PostArticle(Form):
    title=StringField('input your title',validators=[DataRequired()])
    # content=PageDownField('input your article',validators=[DataRequired()])
    body=TextAreaField('input your article',validators=[DataRequired()])
   # body=TextField
    submit=SubmitField('Submit')

