from flask import Blueprint, render_template
import json
import traceback

import overwatchdb.models as models

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
    print(data)
    return render_template('players.html', data=data)


@views.route('/api/players/<int:player_id>', methods=['GET'])
def player(player_id):
    """ Returns Page for a single Player """
    data = models.Player.query.get(player_id)
    if not data:
        return render_template('404.html', thing='Player')
    print(data.url)
    return render_template('players_instance.html', data=data)


@views.route('/api/heroes', methods=['GET'])
def heroes():
    """ Returns Heroes Page """
    data = models.Hero.query.all()
    if not data:
        return render_template('404.html', thing='Heroes')
    print(data)
    return render_template('heroes.html', data=data)


@views.route('/api/heroes/<int:hero_id>', methods=['GET'])
def hero(hero_id):
    """ Returns Page for a single Hero """
    data = models.Hero.query.get(hero_id)
    if not data:
        return render_template('404.html', thing='Hero')
    print(data)
    return render_template('heroes_instance.html', data=data)


@views.route('/api/rewards', methods=['GET'])
def rewards():
    """ Returns Rewards Page """
    data = models.Reward.query.all()
    if not data:
        return render_template('404.html', thing='Rewards')
    print(data)
    return render_template('rewards.html', data=data)


@views.route('/api/rewards/<int:reward_id>', methods=['GET'])
def reward(reward_id):
    """ Returns Page for a single Reward """
    data = models.Reward.query.get(reward_id)
    if not data:
        return render_template('404.html', thing='Reward')
    print(data)
    return render_template('rewards_instance.html', data=data)


@views.route('/api/achievements', methods=['GET'])
def achievements():
    """ Returns Achievements Page """
    data = models.Achievement.query.all()
    if not data:
        return render_template('404.html', thing='Achievements')
    print(data)
    return render_template('achievements.html', data=data)  # id=achievement_id)


@views.route('/api/achievements/<int:achievement_id>', methods=['GET'])
def achievement(achievement_id):
    data = models.Achievement.query.get(achievement_id)
    if not data:
        return render_template('404.html', thing='Achievement')
    print(data)
    return render_template('achievements_instance.html', data=data)


@views.route('/about/')
def about():
    """ Returns Heroes Page """
    return render_template('about.html')
