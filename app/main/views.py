#!/usr/bin/env python
# coding=utf-8
from datetime import datetime
from flask import render_template,session,redirect,url_for,request
from flask_login import current_user
from . import main
from .forms import NameForm,PostArticle,articleComment
from .. import db
from ..models import User,Post,Comment

@main.route('/',methods=['GET','POST'])
def index():
    page=request.args.get('page',1,type=int)

    #posts=Post.query.order_by(Post.timestamp.desc()).all()
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(page,per_page=5,error_out=False)
    posts = pagination.items
    return render_template('index.html',posts=posts,pagination=pagination)

@main.route('/edit',methods=['GET','POST'])
def edit():
    form=PostArticle()
    post=Post.query.all()
    postid=0;
    if len(post):
        print post[0].totalNum
        #print post[1]
        #postid=post.totalNum+1
    else:
        postid=1;
    if form.validate_on_submit():
        post=Post(fileId=postid,title=form.title.data,body=form.body.data,author_id=1,totalNum=postid)
        db.session.add(post)
        return redirect(url_for('.index'))
    return render_template('edit.html',form=form)

@main.route('/<int:id>',methods=['GET','POST'])
def show(id):
    post = Post.query.get_or_404(id)
    con=Comment.query.all()
    comment=articleComment()
    if comment.validate_on_submit():
        comment.user_ip=request.remote_addr
        com=Comment(fileId=id,Sid=post.comments+1,comment=comment.comment.data,user=comment.user_ip)
        post.comments+=1;
        db.session.add(post)
        db.session.add(com)
        #return render_template('detail.html', post=post,comment=comment)
    return render_template('detail.html',post=post,comment=comment,con=con)

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



