from flask import Blueprint, render_template, jsonify
import json
import traceback
import models as models
from models import *
from sqlalchemy import or_

views = Blueprint('views', __name__)


@views.route('/')
def index():
    """ Returns Welcome Page """
    return render_template('index.html')


@views.route('/tests/run')
def run_tests():
    """ Runs all the unittests and returns the text result with verbosity 2 """
    import overwatchdb.test_runner as test_runner
    return test_runner.run_tests()


@views.route('/api/players', methods=['GET'])
def players():
    """ Returns Players Page """
    data = models.Player.query.all()
    if not data:
        return render_template('404.html', thing='Players')
   
    return render_template('players.html', data=data)

@views.route('/api/players/asc', methods=['GET'])
def players_asc():
    """ Returns Heroes Page """
    data = models.Player.query.order_by(models.Player.name.asc()).all()
    if not data:
        return render_template('404.html', thing='Heroes')
    
    return render_template('players.html', data=data)

@views.route('/api/players/desc', methods=['GET'])
def players_desc():
    """ Returns Heroes Page """
    data = models.Player.query.order_by(models.Player.name.desc()).all()
    if not data:
        return render_template('404.html', thing='Heroes')
    
    return render_template('players.html', data=data)

@views.route('/api/players/<int:player_id>', methods=['GET'])
def player(player_id):
    """ Returns Page for a single Player """
    data = models.Player.query.get(player_id)
    if not data:
        return render_template('404.html', thing='Player')

    return render_template('players_instance.html', data=data)


@views.route('/api/heroes', methods=['GET'])
def heroes():
    """ Returns Heroes Page """
    data = models.Hero.query.order_by(models.Hero.name.asc()).all()
    if not data:
        return render_template('404.html', thing='Heroes')
    
    return render_template('heroes.html', data=data)


@views.route('/api/heroes/<int:hero_id>', methods=['GET'])
def hero(hero_id):
    """ Returns Page for a single Hero """
    data = models.Hero.query.get(hero_id)
    if not data:
        return render_template('404.html', thing='Hero')
    
    return render_template('heroes_instance.html', data=data)

@views.route('/api/heroes/asc', methods=['GET'])
def heroes_asc():
    """ Returns Heroes Page """
    data = models.Hero.query.order_by(models.Hero.name.asc()).all()
    if not data:
        return render_template('404.html', thing='Heroes')
    
    return render_template('heroes.html', data=data)

@views.route('/api/heroes/desc', methods=['GET'])
def heroes_desc():
    """ Returns Heroes Page """
    data = models.Hero.query.order_by(models.Hero.name.desc()).all()
    if not data:
        return render_template('404.html', thing='Heroes')
    
    return render_template('heroes.html', data=data)

@views.route('/api/heroes/others', methods=['GET'])
def heroes_others():
    """ Returns Heroes Page """
    data = models.Hero.query.filter(Hero.affiliation != 'Overwatch').all()
    if not data:
        return render_template('404.html', thing='Heroes')
    
    return render_template('heroes.html', data=data)

@views.route('/api/heroes/overwatch', methods=['GET'])
def heroes_overwatch():
    """ Returns Heroes Page """
    data = models.Hero.query.filter(Hero.affiliation == 'Overwatch').all()
    if not data:
        return render_template('404.html', thing='Heroes')
    
    return render_template('heroes.html', data=data)


@views.route('/api/rewards', methods=['GET'])
def rewards():
    """ Returns Rewards Page """
    data = models.Reward.query.order_by(models.Reward.name.asc()).all()
    if not data:
        return render_template('404.html', thing='Rewards')
    
    return render_template('rewards.html', data=data)


@views.route('/api/rewards/<int:reward_id>', methods=['GET'])
def reward(reward_id):
    """ Returns Page for a single Reward """
    data = models.Reward.query.get(reward_id)
    if not data:
        return render_template('404.html', thing='Reward')
    
    return render_template('rewards_instance.html', data=data)

@views.route('/api/rewards/asc', methods=['GET'])
def rewards_asc():
    """ Returns Heroes Page """
    data = models.Reward.query.order_by(models.Reward.cost.asc()).all()
    if not data:
        return render_template('404.html', thing='Heroes')
    
    return render_template('rewards.html', data=data)

@views.route('/api/rewards/desc', methods=['GET'])
def rewards_desc():
    """ Returns Heroes Page """
    data = models.Reward.query.order_by(models.Reward.cost.desc()).all()
    if not data:
        return render_template('404.html', thing='Heroes')
    
    return render_template('rewards.html', data=data)

@views.route('/api/rewards/achievements', methods=['GET'])
def rewards_achievements_available():
    """ Returns Achievements Page """
    data = models.Reward.query.filter(Reward.achievement_id != None ).all()
    if not data:
        return render_template('404.html', thing='Achievements')
    
    return render_template('rewards.html', data=data)

@views.route('/api/rewards/achievements-', methods=['GET'])
def rewards_achievements_unavailable():
    """ Returns Achievements Page """
    data = models.Reward.query.filter(Reward.achievement_id == None ).all()
    if not data:
        return render_template('404.html', thing='Achievements')
    
    return render_template('rewards.html', data=data)

@views.route('/api/achievements', methods=['GET'])
def achievements():
    """ Returns Achievements Page """
    data = models.Achievement.query.all()
    if not data:
        return render_template('404.html', thing='Achievements')
    
    return render_template('achievements.html', data=data)  # id=achievement_id)


@views.route('/api/achievements/<int:achievement_id>', methods=['GET'])
def achievement(achievement_id):
    data = models.Achievement.query.get(achievement_id)
    if not data:
        return render_template('404.html', thing='Achievement')
    
    return render_template('achievements_instance.html', data=data)

@views.route('/api/achievements/asc', methods=['GET'])
def achievements_asc():
    """ Returns Heroes Page """
    data = models.Achievement.query.order_by(models.Achievement.name.asc()).all()
    if not data:
        return render_template('404.html', thing='Heroes')
    
    return render_template('achievements.html', data=data)

@views.route('/api/achievements/desc', methods=['GET'])
def achievements_desc():
    """ Returns Heroes Page """
    data = models.Achievement.query.order_by(models.Achievement.name.desc()).all()
    if not data:
        return render_template('404.html', thing='Heroes')
    
    return render_template('achievements.html', data=data)

@views.route('/api/achievements/heroes', methods=['GET'])
def achievements_heroes_available():
    """ Returns Achievements Page """
    data = models.Achievement.query.filter(Achievement.hero_id != None ).all()
    if not data:
        return render_template('404.html', thing='Achievements')
    
    return render_template('achievements.html', data=data)

@views.route('/api/achievements/heroes-', methods=['GET'])
def achievements_heroes_unavailable():
    """ Returns Achievements Page """
    data = models.Achievement.query.filter(Achievement.hero_id == None ).all()
    if not data:
        return render_template('404.html', thing='Achievements')
    
    return render_template('achievements.html', data=data)

@views.route('/about/')
def about():
    """ Returns Heroes Page """
    return render_template('about.html')

@views.route('/api/search_and/<search_string>', methods=['GET'])
def search_and(search_string):
    search_string = "%" + search_string + "%"
    data = models.Achievement.query.filter(or_(Achievement.name.like(search_string),
                                               Achievement.description.like(search_string))).all()
    data += models.Reward.query.filter(or_(Reward.name.like(search_string),
                                           Reward.quality.like(search_string))).all()
    data += models.Player.query.filter(or_(Player.name.like(search_string),
                                           Player.server.like(search_string),
                                           Player.level.like(search_string),
                                           Player.server.like(search_string))).all()
    data += models.Hero.query.filter(or_(Hero.name.like(search_string),
                                         Hero.age.like(search_string),
                                         Hero.description.like(search_string),
                                         Hero.affiliation.like(search_string))).all()
    return jsonify([d.serialize() for d in data])

@views.route('/api/search_or/<search_string>', methods=['GET'])
def search_or(search_string):
    data = []
    for word in search_string.split():
        word = "%" + word + "%"
        data += models.Achievement.query.filter(or_(Achievement.name.like(word),
                                                   Achievement.description.like(word))).all()
        data += models.Reward.query.filter(or_(Reward.name.like(word),
                                               Reward.quality.like(word))).all()
        data += models.Player.query.filter(or_(Player.name.like(word),
                                               Player.server.like(word),
                                               Player.level.like(word),
                                               Player.server.like(word))).all()
        data += models.Hero.query.filter(or_(Hero.name.like(word),
                                             Hero.age.like(word),
                                             Hero.description.like(word),
                                             Hero.affiliation.like(word))).all()
    return jsonify([d.serialize() for d in data])

