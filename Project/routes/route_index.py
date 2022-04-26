from flask import Flask, render_template,request,redirect,session, flash

from ..controllers.user_controller import UserController


class routes:

    def init_app(app,db):

        @app.route('/createUser',methods=['POST'])
        def createUser():
            user = request.form
            user_controller = UserController(db)
            user_controller.saveUser(user)
            return render_template('intro/login_form.html')