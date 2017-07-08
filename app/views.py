from flask import Blueprint, render_template, jsonify, request, session
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
    if ("hero page" not in session):
        session["hero page"] = 1
    if type(request.args.get('page')) is unicode:
        session["hero page"] = int(request.args.get('page'))
    if ("hero order" not in session):
        session["hero order"] = "ascending"

    """ Returns Heroes Page """
    if (session["hero order"] == "ascending"):
        data = models.Hero.query.order_by(models.Hero.name.asc()).all()
    else:
        data = models.Hero.query.order_by(models.Hero.name.desc()).all()
    if not data:
        return render_template('404.html', thing='Heroes')
    data = data[9 * (session["hero page"] - 1): 9 * session["hero page"]]
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

    session["hero order"] = "ascending"
    
    return heroes()

@views.route('/api/heroes/desc', methods=['GET'])
def heroes_desc():
    session["hero order"] = "descending"
    
    return heroes()

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

# Usage example: "http://127.0.0.1:5000/api/search?search_string=her&page=1"
@views.route('/api/search', methods=['GET'])
def search():
    search_string = request.args.get('search_string')
    page = int(request.args.get('page'))

    # Find the AND search matches in the tables
    like_search_string = "%" + search_string + "%"
    data = [[], []]
    data[0] += models.Achievement.query.filter(or_(Achievement.name.like(like_search_string),
                                               Achievement.description.like(like_search_string))).all()
    data[0] += models.Reward.query.filter(or_(Reward.name.like(like_search_string),
                                           Reward.quality.like(like_search_string))).all()
    data[0] += models.Player.query.filter(or_(Player.name.like(like_search_string),
                                           Player.server.like(like_search_string),
                                           Player.level.like(like_search_string),
                                           Player.server.like(like_search_string))).all()
    data[0] += models.Hero.query.filter(or_(Hero.name.like(like_search_string),
                                         Hero.age.like(like_search_string),
                                         Hero.description.like(like_search_string),
                                         Hero.affiliation.like(like_search_string))).all()

    # Find the OR search matches in the tables
    for word in search_string.split():
        word = "%" + word + "%"
        data[1] += models.Achievement.query.filter(or_(Achievement.name.like(word),
                                                   Achievement.description.like(word))).all()
        data[1] += models.Reward.query.filter(or_(Reward.name.like(word),
                                               Reward.quality.like(word))).all()
        data[1] += models.Player.query.filter(or_(Player.name.like(word),
                                               Player.server.like(word),
                                               Player.level.like(word),
                                               Player.server.like(word))).all()
        data[1] += models.Hero.query.filter(or_(Hero.name.like(word),
                                             Hero.age.like(word),
                                             Hero.description.like(word),
                                             Hero.affiliation.like(word))).all()

    # Get the data into usable dicts
    data = [[d.serialize() for d in data[0]], [d.serialize() for d in data[1]]]

    search_results = [[], []]
    # Search through the results for the context of search terms as well as format the search results into usable values
    for result in data[0]:
        context = []
        for value in [getContext(val, search_string) for val in result.values()]:
            if (value != []):
                context += value
        search_results[0].append({"name": result["name"], "search_url": result["search_url"], "matches": context})
    for result in data[1]:
        context = []
        for word in search_string.split():
            for value in [getContext(val, word) for val in result.values()]:
                if (value != []):
                    context += value
        search_results[1].append({"name": result["name"], "search_url": result["search_url"], "matches": context})

    # Get the results for the specified page
    search_results = [search_results[0][10 * (page - 1):10 * page], search_results[1][10 * (page - 1):10 * page]]
    return render_template('search.html', data=jsonify(search_results))

# Method to find context in the values of the table entries
def getContext(val, search):
    context_amount = 5
    results = []
    if (type(val) is int):
        try:
            if (val == int(search)):
                return [val]
        except Exception:
            return results
    if (type(val) is unicode):
        index = val.find(search)
        while (index != -1):
            front = index
            back = index
            frontCount = context_amount + 1
            backCount = context_amount + 1
            while (frontCount > 0 or backCount > 0):
                if (front > 0 and frontCount > 0):
                    front -= 1
                if (back < len(val) and backCount > 0):
                    back += 1
                if (val[front] == ' ' or front == 0):
                    frontCount -= 1
                if (back == len(val) or val[back] == ' '):
                    backCount -= 1
            results.append(val[front:back])
            frontCount = context_amount + 1
            backCount = context_amount + 1
            val = val[back::]
            index = val.find(search)
    return results




