from flask import Flask, jsonify, request, redirect, session, flash

from Project.dtos.group.create_dto import GroupDto
from ..controllers.group_controller import GroupController
from ..ext.authentication import jwt_required

class Routes:

    def init_app(app,db):
        groupController = GroupController(db)

        @app.route('/group/create', methods=['POST'])
        @jwt_required
        def createGroup(**kwargs):
            dataPost = request.json
            try:
                idUser = kwargs['current_user_id']
                createDto = GroupDto(name=dataPost['groupname'], idUser=idUser)
            except ValueError:
                return jsonify({"response":"Faltando dados de requisição"}), 400
            response = groupController.save(createDto)
            return response

        @app.route('/group/user', methods=['POST'])
        @jwt_required
        def insertUserGroup(**kwargs):
            dataPost = request.json
            try:
                idUser = kwargs['current_user_id']
                createDto = GroupDto(name=dataPost['groupname'], idUser = idUser)
            except ValueError:
                return jsonify({"response":"Faltando dados de requisição"}), 400
            response = groupController.saveUser(createDto)
            return response
