from flask import Flask, render_template,request,redirect,session, flash
from ..ext.database import Connection
from ..controllers.user_controller import UserController


class routes:

    def init_app(app):

        db = Connection.createConnection(app)

        @app.route('/createUser')
        def createUser():
            # print(request.form)
            # user_controller = UserController()
            # user_controller.saveUser(db,request.form)
            return render_template('login.html')