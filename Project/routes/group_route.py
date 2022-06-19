from flask import Flask, jsonify, request, redirect, session, flash

from Project.dtos.group.create_dto import GroupDto
from ..controllers.group_controller import GroupController

class Routes:

    def init_app(app,db):
        groupController = GroupController(db)

        @app.route('/group/create', methods=['POST'])
        def createGroup():
            dataPost = request.json
            try:
                createDto = GroupDto(dataPost['groupname'])
            except:
                return jsonify({"response":"Faltando dados de requisição"}), 400
            response = groupController.save(createDto)
            return response
