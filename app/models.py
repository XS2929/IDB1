"""models for the database"""
# pylint: disable=too-few-public-methods,invalid-name

import sys

import flask

from flask import jsonify

from flask_sqlalchemy import SQLAlchemy

#from flask.ext.sqlalchemy import SQLAlchemy, Pagination
from werkzeug import generate_password_hash, check_password_hash

db = SQLAlchemy()

player_achievement = db.Table('player_achievement',
    db.Column('player_id', db.Integer, db.ForeignKey('player.id')),
    db.Column('achievement_id', db.Integer, db.ForeignKey('achievement.id'))
)

player_reward = db.Table('player_reward',
    db.Column('player_id', db.Integer, db.ForeignKey('player.id')),
    db.Column('reward_id', db.Integer, db.ForeignKey('reward.id'))
)

#USER MODEL FOR SIGNIN PAGE 
class User(db.Model):
  __tablename__ = 'users'
  uid = db.Column(db.Integer, primary_key = True)
  firstname = db.Column(db.String(100))
  lastname = db.Column(db.String(100))
  email = db.Column(db.String(100), unique=True)
  pwdhash = db.Column(db.String(54))

  def __init__(self, firstname, lastname, email, password):
    self.firstname = firstname.title() #makes capital
    self.lastname = lastname.title() 
    self.email = email.lower() #always lower case
    self.set_password(password) #see set_password method
     
  def set_password(self, password):
    self.pwdhash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.pwdhash, password)


class Hero(db.Model):
    """model for hero"""
    __tablename__ = 'hero'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    affiliation = db.Column(db.String, nullable=False)
    age = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)
    players = db.relationship('Player', backref='Hero',lazy='dynamic')
    achievements = db.relationship('Achievement', backref='Hero',lazy='dynamic')

    def __init__(self, name, description, affiliation, age, url):
        self.name = name
        self.description = description 
        self.age = age
        self.url = url
        self.affiliation = affiliation


    def __repr__(self):
        return "<Hero(name='%s', description=%s, affiliation=%s, age=%s, url=%s)>" % (
            self.name, self.description, self.affiliation, self.age, self.url)

    def search_result(self):
        """ Returns result format for the hero """
        return {"model": "hero", "id": self.id}

    def serialize(self):
        result = {"search_url": "/api/heroes/" + str(self.id)}
        result = dict(result, **{column.name: getattr(self, column.name) for column in self.__table__.columns})
        return result

class Player(db.Model):
    """model for player"""
    __tablename__ = 'player'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    server = db.Column(db.String, nullable=False)
    hero_id = db.Column(db.Integer, db.ForeignKey("hero.id"), nullable=False)
    level = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)

    achievements = db.relationship('Achievement', secondary=player_achievement ,backref=db.backref('players', lazy='dynamic'))
    
    hero = db.relationship("Hero",backref='Player',uselist=False,foreign_keys=[hero_id])

    def __init__(self, name, server, level, url):
        self.name = name
        self.server = server 
        self.level = level
        self.url = url

    def __repr__(self):
        return "<Player(name='%s', server=%s, level=%s, url=%s, hero=%s, achievements=%s)>" % (
            self.name, self.server, self.level, self.url, self.hero, self.achievements)

    def search_result(self):
        """ Returns result format for the player """
        return {"model": "player", "id": self.id}

    def serialize(self):
        result = {"search_url": "/api/players/" + str(self.id)}
        result = dict(result, **{column.name: getattr(self, column.name) for column in self.__table__.columns})
        return result

class Reward(db.Model):
    """model for reward"""
    __tablename__ = 'reward'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    quality = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    hero_id = db.Column(db.Integer, db.ForeignKey("hero.id"), nullable=True)
    achievement_id = db.Column(db.Integer, db.ForeignKey("achievement.id"), nullable=True)

    achievement = db.relationship("Achievement",backref='Reward',uselist=False,foreign_keys=[achievement_id])
    hero = db.relationship("Hero",backref='Reward',uselist=False,foreign_keys=[hero_id])

    def __init__(self, name, quality, cost, url):
        self.name = name
        self.quality = quality 
        self.cost = cost
        self.url = url

    def __repr__(self):
        return "<Reward(name='%s', quality=%s, url=%s, cost=%s, achievement=%s, hero=%s)>" % (
            self.name, self.quality, self.url, self.cost, self.achievement, self.hero)

    def search_result(self):
        """ Returns result format for the reward """
        return {"model": "reward", "id": self.id}

    def serialize(self):
        result = {"search_url": "/api/rewards/" + str(self.id)}
        result = dict(result, **{column.name: getattr(self, column.name) for column in self.__table__.columns})
        return result

class Achievement(db.Model):
    """model for achievement"""
    __tablename__ = 'achievement'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)
    hero_id = db.Column(db.Integer, db.ForeignKey("hero.id"), nullable=True)
    reward_id = db.Column(db.Integer, db.ForeignKey("reward.id"), nullable=True)
    
    #hero = db.relationship("Hero", backref="Achievement",lazy='dynamic')
    reward = db.relationship("Reward",backref='Achievement',uselist=False,foreign_keys=[reward_id])
    hero = db.relationship("Hero",backref='Achievement',uselist=False,foreign_keys=[hero_id])
    
    def __init__(self, name, description, type, url):
        self.name = name
        self.description = description 
        self.type = type
        self.url = url

    def __repr__(self):
        return "<Achievement(name='%s', description=%s, type=%s, url=%s, reward=%s, hero=%s)>" % (
            self.name, self.description, self.type, self.url, self.reward.name, self.hero)

    def search_result(self):
        """ Returns result format for the achievement """
        return {"model": "achievement", "id": self.id}

    def serialize(self):
        result = {"search_url": "/api/achievements/" + str(self.id)}
        result = dict(result, **{column.name: getattr(self, column.name) for column in self.__table__.columns})
        return result

