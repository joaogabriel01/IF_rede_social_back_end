from flask import Flask, request, redirect, session, flash
from ..controllers.publication_controller import PublicationController

class routes:

    def init_app(app,db):

        publication_controller = PublicationController(db)

        @app.route('/publication/create',methods=['POST'])
        def createPublication():
            dataPost = request.json
            response = publication_controller.savePublication(dataPost)
            return response