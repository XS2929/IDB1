from flask import Blueprint, render_template
import json
import traceback

import overwatchdb.models as models

views = Blueprint('views', __name__)


@views.route('/')
def index():
    """ Returns Welcome Page """
    return render_template('index.html')


@views.route('/api/players/<player_id>', methods=['GET'])
def get_player(player_id):
    """ Returns Page for a single Player """
    data = models.Player.query.get(player_id)
    if not data:
        return render_template('404.html', thing='Player')
    return render_template('player.html', data=data)


@views.route('/api/heroes', methods=['GET'])
def get_heroes():
    """ Returns Heroes Page """
    return render_template('heroes.html')


@views.route('/api/heroes/<int:hero_id>', methods=['GET'])
def get_hero(hero_id):
    """ Returns Page for a single Hero """
    data = models.Hero.query.get(hero_id)
    if not data:
        return render_template('404.html', thing='Hero')
    return render_template('heroes_instance.html', data=data)


@views.route('/api/rewards', methods=['GET'])
def get_rewards():
    """ Returns Rewards Page """
    return render_template('rewards.html')


@views.route('/api/rewards/<int:reward_id>', methods=['GET'])
def get_reward(reward_id):
    """ Returns Page for a single Reward """
    data = models.Reward.query.get(reward_id)
    if not data:
        return render_template('404.html', thing='Reward')
    return render_template('rewards_instance.html', data=data)


@views.route('/api/achievements', methods=['GET'])
def get_achievements():
    """ Returns Achievements Page """
    return render_template('achievements.html')  # id=achievement_id)


@views.route('/api/achievements/<int:achievement_id>', methods=['GET'])
def get_achievement(achievement_id):
    data = models.Achievement.query.get(achievement_id)
    if not data:
        return render_template('404.html', thing='Achievement')
    return render_template('achievements_instance.html', data=data)


@views.route('/about/')
def about():
    """ Returns Heroes Page """
    return render_template('about.html')
