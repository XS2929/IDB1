"""models for the database"""
# pylint: disable=too-few-public-methods,invalid-name

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

player_achievement = db.Table('player_achievement',
    db.Column('player_id', db.Integer, db.ForeignKey('player.id')),
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
	url = db.Column(db.String, nullable=False)
	players = db.relationship('Player', backref='Hero',lazy='dynamic')
	# achievement_id = db.Column(db.Integer, db.ForeignKey("achievement.id"))
	reward = db.relationship('Reward', backref('Hero'),lazy='dynamic')

	def __repr__(self):
		return "<Hero(name='%s', description=%s, affiliation=%s, age=%s, url=%s)>" % (
			self.name, self.description, self.affiliation, self.age, self.url)

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
	type = db.Column(db.String, nullable=False)
	url = db.Column(db.String, nullable=False)
      
	def __repr__(self):
		return "<Player(name='%s', server=%s, level=%s, url=%s)>" % (
			self.name, self.server, self.level, self.url)

	def search_result(self):
		""" Returns result format for the player """
		return {"model": "player", "id": self.id}

class Reward(db.Model):
	"""model for reward"""
	__tablename__ = 'reward'

	id = db.Column(db.Integer, nullable=False, primary_key=True)
	name = db.Column(db.String, nullable=False)
	quality = db.Column(db.String, nullable=False)
	url = db.Column(db.String, nullable=False)
	cost = db.Column(db.String, nullable=False)
	hero_id = db.Column(db.Integer, db.ForeignKey("hero.id"), nullable=True)
	achievement_id = db.Column(db.Integer, db.ForeignKey("achievement.id"), nullable=True)

	def __repr__(self):
		return "<Reward(name='%s', quality=%s, url=%s, cost=%s)>" % (
			self.name, self.quality, self.url, self.cost)

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
	url = db.Column(db.String, nullable=False)
	hero_id = db.Column(db.Integer, db.ForeignKey("hero.id"), nullable=True)
	achievement_id = db.Column(db.Integer, db.ForeignKey("achievement.id"), nullable=True)
	
	hero = db.relationship("Hero", backref="Achievement",lazy='dynamic')
	reward = db.relationship("Reward",backref('Achievement'),lazy='dynamic')

	def __repr__(self):
		return "<Achievement(name='%s', description=%s, type=%s, url=%s)>" % (
			self.name, self.description, self.type, self.url)

	def search_result(self):
		""" Returns result format for the achievement """
		return {"model": "achievement", "id": self.id}

