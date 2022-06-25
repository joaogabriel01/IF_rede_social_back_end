from flask import Flask, jsonify, request, redirect, session, flash

from ..dtos.publication.create_dto import CreateDto
from ..dtos.publication.create_comment_dto import CreateCommentDto
from ..controllers.publication_controller import PublicationController
from ..ext.authentication import jwt_required

class Routes:

    def init_app(app,db):

        publication_controller = PublicationController(db)

        @app.route('/publication/create', methods=['POST'])
        @jwt_required
        def createPublication(**kwargs):
            dataPost = request.json
            try:
                if ('images' not in dataPost):
                    dataPost['images'] = ''
                idUser = kwargs['current_user_id']
                createDto = CreateDto(idUser=idUser, groupName=dataPost['group-name'], text=dataPost['text'], images=dataPost['images'])
            except:
                return jsonify({"response": "Faltando dados de requisição"}), 400
            response = publication_controller.savePublication(createDto)
            return response

        @app.route('/publication/createComment', methods=['POST'])
        @jwt_required
        def createComment(**kwargs):
            dataPost =  request.json
            idUser = kwargs['current_user_id']
            try:
                createCommentDto = CreateCommentDto(idUser=idUser, idPublication=dataPost['idPublication'], text=dataPost['text'])
            except:
                return jsonify({"response":"Faltando dados de requisição"}), 400
            response = publication_controller.saveComment(createCommentDto)
            return response
