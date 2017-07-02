"""models for the database"""
# pylint: disable=too-few-public-methods,invalid-name

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Hero(db.Model):
	"""model for hero"""
	__tablename__ = 'hero'

	id = db.Column(db.Integer, nullable=False, primary_key=True)
	name = db.Column(db.String, nullable=False)
	description = db.Column(db.String, nullable=False)
	affiliation = db.Column(db.String, nullable=False)
	age = db.Column(db.String, nullable=False)
	players = db.relationship("Player", backref="hero_id")

    def __repr__(self):
        return "<Hero(name='%s', description=%s, affiliation=%s, age=%s)>" % (
            self.name, self.description, self.affiliation, self.age)

    def search_result(self):
        """ Returns result format for the hero """
        return {"model": "hero", "id": self.id}

class Player(db.Model):
	"""model for player"""
	__tablename__ = 'player'

	id = db.Column(db.Integer, nullable=False, primary_key=True)
	name = db.Column(db.String, nullable=False)
	server = db.Column(db.String, nullable=False)
	hero_id = db.Column(db.Integer, nullable=False, db.ForeignKey("hero_id"))
	level = db.Column(db.String, nullable=False)

    def __repr__(self):
        return "<Player(name='%s', server=%s, level=%s)>" % (
            self.name, self.server, self.level)

    def search_result(self):
        """ Returns result format for the player """
        return {"model": "player", "id": self.id}

class Reward(db.Model):
	"""model for reward"""
	__tablename__ = 'reward'

	id = db.Column(db.Integer, nullable=False, primary_key=True)
	name = db.Column(db.String, nullable=False)
	quality = db.Column(db.String, nullable=False)
	cost = db.Column(db.String, nullable=False)
	hero_id = db.relationship("Hero", backref="reward_id")
	achievement_id = db.Column(db.Integer, nullable=True, db.ForeignKey("achievement.id"))

    def __repr__(self):
        return "<Reward(name='%s', quality=%s, cost=%s)>" % (
            self.name, self.quality, self.cost)

    def search_result(self):
        """ Returns result format for the reward """
        return {"model": "reward", "id": self.id}

class Achievement(db.Model):
	"""model for achievement"""
	__tablename__ = 'achievement'

	id = db.Column(db.Integer, nullable=False, primary_key=True)
	name = db.Column(db.String, nullable=False)
	description = db.Column(db.String, nullable=False)
	type = db.Column(db.String, nullable=False)
	hero_id = db.relationship("Hero", backref="achievement_id")
	reward_id = db.relationship("Reward", backref="achievement_id")

    def __repr__(self):
        return "<Achievement(name='%s', description=%s, type=%s)>" % (
            self.name, self.description, self.type)

    def search_result(self):
        """ Returns result format for the achievement """
        return {"model": "achievement", "id": self.id}

