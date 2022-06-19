from flask import Flask, jsonify, request, redirect, session, flash

from ..dtos.publication.create_dto import CreateDto
from ..controllers.publication_controller import PublicationController
from ..controllers.comment_controller import CommentController

class Routes:

    def init_app(app,db):

        publication_controller = PublicationController(db)
        comment_controller = CommentController(db)

        @app.route('/publication/create', methods=['POST'])
        def createPublication():
            dataPost = request.json

            try:
                if ('images' not in dataPost):
                    dataPost['images'] = ''
                createDto = CreateDto(idUser=dataPost['idUser'],text=dataPost['text'],images=dataPost['images'])
            except ValueError:
                print(ValueError)
                return jsonify({"response": "Faltando dados de requisição"})
            response = publication_controller.savePublication(createDto)
            return response

        @app.route('/publication/createComment', methods=['POST'])
        def createComment():
            dataPost =  request.json
            response = comment_controller.saveComment(dataPost)
            return response
