#coding=utf-8

from flask import render_template,flash,url_for,request,redirect
from flask_login import login_user,login_required,logout_user

from . import auth
from .form import LoginForm
from ..models import User

#采用wtf方式
# @auth.route('/login',methods=['GET','POST'])
# def login():
#     form=LoginForm()
#     if form.validate_on_submit():
#         print 'test'
#         user=User.query.filter_by(email=form.email.data).first()
#         if user is not None and user.verify_psw(form.passwd.data):
#             login_user(user,form.remeber_me.data)
#             return redirect(request.args.get('next') or url_for('main.index'))
#         flash('Error username or passwd')
#
#
#     return render_template('auth/login.html',form=form)


@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        user=User.query.filter_by(email=request.form['username']).first()
        if user is not None and user.verify_psw(request.form['password']):
            login_user(user)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash("ERROR")

    return render_template('auth/login.html')




# @auth.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         print 'aa'
#         user = User.query.filter_by(email=form.email.data).first()
#         if user is not None and user.verify_password(form.password.data):
#             login_user(user, form.remember_me.data)
#             return redirect(request.args.get('next') or url_for('main.index'))
#         flash('Invalid username or password.')
#     return render_template('auth/login.html', form=form)
#
#
# @auth.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     flash('You have been logged out.')
#     return redirect(url_for('main.index'))