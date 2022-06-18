from flask import Flask, request, redirect, session, flash, jsonify
from ..controllers.user_controller import UserController
from ..ext.authentication import jwt_required
from ..dtos.user.create_dto import Create

class Routes:

    def init_app(app,db):

        user_controller = UserController(db)
            
        @app.route('/user/create', methods=['POST'])
        def createUser():
            dataPost = request.json
            try:
                createDto = Create(nickname=dataPost['nickname'], mail=dataPost['mail'], password=dataPost['password'], confirmPassword=dataPost['confirmPassword'])
                print(createDto.getMail())
            except ValueError:
                print(ValueError)
                return jsonify({"response":"Faltando dados de requisição"}), 400
            response = user_controller.saveUser(createDto);
            return response
        
        @app.route('/user/testAuthenticated', methods=['GET'])
        @jwt_required
        def testAuthenticated(**kwargs):
            print(kwargs)
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



