from flask import Blueprint, render_template
import json
import traceback
import html
import requests

import overwatchdb.models as models

views = Blueprint('views', __name__)


@views.route('/')
def index():
    """ Returns Welcome Page """
    return render_template('index.html')

# Unsure if necessary/desirable - Austin
# @views.route('/players/')
# def players():
#     """ Returns Players Page """
#     return render_template('Players.html')


@views.route('api/players/<player_id>', methods=['GET'])
def get_player(player_id):
    """ Returns Page for a single Player """
    return render_template('player.html', id=player_id)


@views.route('/api/heroes', methods=['GET'])
def get_heroes():
    """ Returns Heroes Page """
    return render_template('Heroes.html')


@views.route('/api/heroes/<int:hero_id>', methods=['GET'])
def get_hero(hero_id):
    """ Returns Page for a single Hero """
    return render_template('HeroHtmls/'+hero_name+'.html', name=hero_name)


@views.route('/api/rewards', methods=['GET'])
def get_rewards():
    """ Returns Rewards Page """
    return render_template('Rewards.html')


@views.route('/api/rewards/<int:reward_id>', methods=['GET'])
def get_reward(reward_id):
    """ Returns Page for a single Reward """
    return render_template('reward.html', id=reward_id)


@views.route('/api/achievements', methods=['GET'])
def get_achievements():
    """ Returns Achievements Page """
    return render_template('/Achievements.html') # id=achievement_id)


@views.route('/api/achievements/<int:achievement_id>', methods=['GET'])
def get_achievement(achievement_id):
    return render_template('/achievements.html', id=achievement_id)


@views.route('/about/')
def about():
    """ Returns Heroes Page """
    return render_template('about.html')

