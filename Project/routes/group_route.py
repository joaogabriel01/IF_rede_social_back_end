from flask import Flask, request, redirect, session, flash
from ..controllers.group_controller import GroupController

class Routes:

    def init_app(app,db):

        groupController = GroupController(db)

        @app.route('/group/create', methods=['POST'])
        def createGroup():
            dataPost = request.json
            response = groupController.save(dataPost)
            return response
