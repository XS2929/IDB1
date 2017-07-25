
""" All modules related to the application """

import os
from flask import Flask, render_template, jsonify, request
# from flask.ext.cors import CORS

from models import db
from views import views
 

def create_app():
    """ Application factory function """
    SQLALCHEMY_DATABASE_URI = \
        '{engine}://{username}:{password}@{hostname}/{database}'.format(
            engine='postgresql',
            username='overwatchdb',
            password='overwatchsummer',
            hostname='overwatchdb.culm9jl6euht.us-east-2.rds.amazonaws.com:5432',
            database='overwatchdb')

    app = Flask(__name__)
    app.secret_key = "super secret key"
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # CORS(app)

    #app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/learningflask'


    db.init_app(app)
    app.register_blueprint(views)

    return app
