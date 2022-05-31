from flask import Flask, request, redirect, session, flash
from ..controllers.publication_controller import PublicationController
from ..controllers.comment_controller import CommentController

class Routes:

    def init_app(app,db):

        publication_controller = PublicationController(db)
        comment_controller = CommentController(db)

        @app.route('/publication/create', methods=['POST'])
        def createPublication():
            dataPost = request.json
            response = publication_controller.savePublication(dataPost)
            return response

        @app.route('/publication/createComment', methods=['POST'])
        def createComment():
            dataPost =  request.json
            response = comment_controller.saveComment(dataPost)
            return response
