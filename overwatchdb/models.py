"""models for the database"""
# pylint: disable=too-few-public-methods,invalid-name

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

player_achievement = db.Table('player_achievement',
    db.Column('player_id', db.Integer, db.ForeignKey('hero.id')),
    db.Column('achievement_id', db.Integer, db.ForeignKey('achievement.id'))
)

player_reward = db.Table('player_reward',
    db.Column('player_id', db.Integer, db.ForeignKey('player.id')),
    db.Column('reward_id', db.Integer, db.ForeignKey('reward.id'))
)

class Hero(db.Model):
	"""model for hero"""
	__tablename__ = 'hero'

	id = db.Column(db.Integer, nullable=False, primary_key=True)
	name = db.Column(db.String, nullable=False)
	description = db.Column(db.String, nullable=False)
	affiliation = db.Column(db.String, nullable=False)
	age = db.Column(db.String, nullable=False)
	players = db.relationship("Player", backref="played_by")
	# achievement_id = db.Column(db.Integer, db.ForeignKey("achievement.id"))

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
	hero_id = db.Column(db.Integer, db.ForeignKey("hero.id"), nullable=False)
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
	hero_id = db.relationship("Hero", backref="earned_by")
	achievement_id = db.Column(db.Integer, db.ForeignKey("achievement.id"), nullable=True)

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
	# hero_id = db.relationship("Hero", backref="achievement_id")
	reward_id = db.relationship("Reward", backref="awards")

	def __repr__(self):
		return "<Achievement(name='%s', description=%s, type=%s)>" % (
			self.name, self.description, self.type)

	def search_result(self):
		""" Returns result format for the achievement """
		return {"model": "achievement", "id": self.id}

