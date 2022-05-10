from flask import Flask, request, redirect, session, flash
from ..controllers.user_controller import UserController

class routes:

    def init_app(app,db):

        @app.route('/createUser',methods=['POST'])
        def createUser():
            user = request.json
            user_controller = UserController(db)
            response = user_controller.saveUser(user)
            return response
