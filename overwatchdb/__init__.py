
""" All modules related to the application """

import os
from flask import Flask, render_template, jsonify, request
# from flask.ext.cors import CORS

from overwatchdb.models import db
from overwatchdb.views import views


def create_app():
    """ Application factory function """
    SQLALCHEMY_DATABASE_URI = \
        '{engine}://{username}:{password}@{hostname}/{database}'.format(
            engine='',
            username='',
            password='',
            hostname='',
            database='')

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # CORS(app)

    db.init_app(app)
    app.register_blueprint(views)

    return app
