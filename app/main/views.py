#!/usr/bin/env python
# coding=utf-8
from datetime import datetime
from flask import render_template,session,redirect,url_for
from flask_login import current_user
from . import main
from .forms import NameForm,PostArticle
from .. import db
from ..models import User,Post

@main.route('/',methods=['GET','POST'])
def index():
    posts=Post.query.order_by(Post.timestamp.desc()).all()

    return render_template('index.html',posts=posts)

@main.route('/edit',methods=['GET','POST'])
def edit():
    form=PostArticle()
    if form.validate_on_submit():
        post=Post(title=form.title.data,body=form.body.data,author_id=1)
        db.session.add(post)
        return redirect(url_for('.index'))
    return render_template('edit.html',form=form)

@main.route('/<int:id>')
def show(id):
    post=Post.query.get_or_404(id)
    return render_template('show.html',post=post)

@main.route('/edit/<int:id>')
def edit_a(id):
    post=Post.query.get_or_404(id)
    form=PostArticle()
    form.title=post.title
    form.body.data=post.body
    if form.validate_on_submit():
        post.body=form.body.data
        db.session.add(post)
        return redirect(url_for('.id'))
    return render_template('edit.html',form=form)



