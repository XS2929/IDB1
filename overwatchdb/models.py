"""models for the database"""
# pylint: disable=too-few-public-methods,invalid-name

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Hero(db.Model):
	__tablename__ = 'heroes'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	description = db.Column(db.String)
	real_name = db.Column(db.String)
	role = db.Column(db.String)
	health = db.Column(db.Integer)
	armour = db.Column(db.Integer)
	shield = db.Column(db.Integer)
	difficulty = db.Column(db.Integer)

	# abilities model?


