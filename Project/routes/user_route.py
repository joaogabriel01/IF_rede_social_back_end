from flask import Flask, request, redirect, session, flash, jsonify
from ..controllers.user_controller import UserController
from ..ext.authentication import jwt_required
from ..dtos.user.create_dto import CreateDto
from ..dtos.user.login_dto import LoginDto
from ..dtos.user.send_email_dto import SendEmailDto
from ..dtos.user.reset_password_dto import ResetPasswordDto

class Routes:

    def init_app(app,db):

        user_controller = UserController(db)
            
        @app.route('/user/create', methods=['POST'])
        def createUser():
            dataPost = request.json
            try:
                createDto = CreateDto(nickname=dataPost['nickname'], mail=dataPost['email'], password=dataPost['password'], confirmPassword=dataPost['confirmPassword'])
            except:
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
            try:
                loginDto = LoginDto(nickname=dataPost['nickname'], password=dataPost['password'])
            except ValueError:
                return jsonify({"response":"Faltando dados de requisição"}), 400
            response = user_controller.loginUser(loginDto)
            return response

        @app.route('/user', methods=['GET'])
        @jwt_required
        def getUser(**kwargs):
            idUser = kwargs['current_user_id']
            response = user_controller.getUserById(idUser)
            return response


        @app.route('/user/sendEmailToResetPassword', methods=['POST'])
        def sendEmail():
            dataPost = request.json
            try:
                sendEmailDto = SendEmailDto(dataPost['email'])
            except:
                return jsonify({"response":"Faltando dados de requisição"}), 400
            response = user_controller.sendEmailToResetPassword(sendEmailDto)
            return response

        @app.route('/user/resetPassword', methods=['POST'])
        def resetPassword():
            dataPost = request.json
            try:
                resetPasswordDto = ResetPasswordDto(dataPost['id_user'], dataPost['password'])
            except:
                return jsonify({"response":"Faltando dados de requisição"}), 400
            response = user_controller.resetPassword(resetPasswordDto)
            return response



