from flask import Blueprint, render_template


views = Blueprint('views', __name__)


@views.route('/')
def index():
    """ Returns Welcome Page """
    return render_template('index.html')


@views.route('/p/')
@views.route('/players/')
def players():
    """ Returns Players Page """
    return render_template('players.html')


@views.route('/p/<string:player_id>')
@views.route('/players/<string:player_id>')
def player(player_id):
    """ Returns Page for a single Player """
    return render_template('player.html', id=player_id)


@views.route('/h/')
@views.route('/heroes/')
def heroes():
    """ Returns Heroes Page """
    return render_template('heroes.html')


@views.route('/h/<string:hero_name>')
@views.route('/heroes/<string:hero_name>')
def hero(hero_name):
    """ Returns Page for a single Hero """
    return render_template('hero.html', name=hero_name)


@views.route('/r/')
@views.route('/rewards/')
def rewards():
    """ Returns Rewards Page """
    return render_template('rewards.html')


@views.route('/r/<reward_id>')
@views.route('/rewards/<reward_id>')
def reward(reward_id):
    """ Returns Page for a single Reward """
    return render_template('reward.html', id=reward_id)


@views.route('/a/')
@views.route('/achievements/')
def achievements():
    return render_template('/achievements.html', id=achievement_id)


@views.route('/a/<achievement_id>')
@views.route('/achievements/<achievement_id>')
def achievement(achievement_id):
    return render_template('/achievements.html', id=achievement_id)
