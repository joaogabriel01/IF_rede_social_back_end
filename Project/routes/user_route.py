from flask import Flask, request, redirect, session, flash, jsonify
from ..controllers.user_controller import UserController
from ..ext.authentication import jwt_required

class routes:

    def init_app(app,db):

        user_controller = UserController(db)
            
        @app.route('/user/create', methods=['POST'])
        def createUser():
            dataPost = request.json
            response = user_controller.saveUser(dataPost)
            return response
        
        @app.route('/user/testAuthenticated', methods=['GET'])
        @jwt_required
        def testAuthenticated(**kwargs):
            return jsonify(1)
        
        @app.route('/user/login', methods=['POST'])
        def loginUser():
            dataPost = request.json
            response = user_controller.loginUser(dataPost)
            return response

        @app.route('/user/sendEmailToResetPassword', methods=['POST'])
        def sendEmail():
            dataPost = request.json
            response = user_controller.sendEmailToResetPassword(dataPost['email'])
            return response

        @app.route('/user/resetPassword', methods=['POST'])
        def resetPassword():
            dataPost = request.json
            response = user_controller.resetPassword(dataPost)
            return response



