''' Modules related to the application '''

from flask import Flask, jsonify

from views import views

app = Flask(__name__)

app.register_blueprint(views)

heroes = {
	"num_results": 2,
	"objects": [
	{
		"id": 1,
		"name": "Ana",
		"description": "Ana’s versatile arsenal allows her to affect heroes all over the battlefield. Her Biotic Rifle rounds and Biotic Grenades heal allies and damage or impair enemies; her sidearm tranquilizes key targets, and Nano Boost gives one of her comrades a considerable increase in power.",
		"health": 200,
		"armour": 0,
		"shield": 0,
		"real_name": "Ana Amari",
		"affiliation": "Overwatch",
		"difficulty": 3,
		"role": {
			"id": 4,
			"name": "support"
		},
		"abilities": [
		{
			"id": 1,
			"name": "Biotic Rifle",
			"description": "Ana’s rifle shoots darts that can restore health to her allies or deal ongoing damage to her enemies. She can use the rifle’s scope to zoom in on targets and make highly accurate shots.",
			"is_ultimate": false
		},
		{
			"id": 2,
			"name": "Sleep Dart",
			"description": "Ana fires a dart from her sidearm, rendering an enemy unconscious (though any damage will rouse them).",
			"is_ultimate": false
		},
		{
			"id": 3,
			"name": "Biotic Grenade",
			"description": "Ana tosses a biotic bomb that deals damage to enemies and heals allies in a small area of effect. Affected allies briefly receive increased healing from all sources, while enemies caught in the blast cannot be healed for a few moments.",
				"is_ultimate": false
		},
		{
			"id": 4,
			"name": "Nano Boost",
			"description": "After Ana hits one of her allies with a combat boost, they temporarily move faster, deal more damage, and take less damage from enemies’ attacks.",
			"is_ultimate": true
		}
		],
		"rewards": [
		{
			"id": 46,
			"name": "Action",
			"cost": {
				"currency": "credit",
				"value": 25
			},
			"type": {
				"id": 1,
				"name": "spray"
			},
			"quality": {
				"name": "common"
			},
			"event": null
		}
		]
	},
	{
		"id": 2,
		"name": "Bastion",
		"description": "Repair protocols and the ability to transform between stationary Assault, mobile Recon and devastating Tank configurations provide Bastion with a high probability of victory.",
		"health": 200,
		"armour": 100,
		"shield": 0,
		"real_name": "SST Laboratories Siege Automaton E54",
		"affiliation": null,
		"difficulty": 1,
		"role": {
			"id": 2,
			"name": "defense"
		},
		"abilities": [
		{
			"id": 5,
			"name": "Configuration: Recon",
			"description": "In Recon mode, Bastion is fully mobile, outfitted with a submachine gun that fires steady bursts of bullets at medium range.",
			"is_ultimate": false
		},
		{
			"id": 6,
			"name": "Configuration: Sentry",
			"description": "In Sentry mode, Bastion is a stationary powerhouse equipped with a gatling gun capable of unleashing a hail of bullets. The gun's aim can be \"walked\" across multiple targets dealing devastating damage at short to medium range.",
			"is_ultimate": false
		},
		{
			"id": 7,
			"name": "Reconfigure",
			"description": "Bastion transforms between its two primary combat modes to adapt to changing battlefield conditions.",
			"is_ultimate": false
		},
		{
			"id": 8,
			"name": "Self-Repair",
			"description": "Bastion restores its health; it cannot move or fire weapons while the repair process is in effect.",
			"is_ultimate": false
		},
		{
			"id": 9,
			"name": "Configuration: Tank",
			"description": "In Tank mode, Bastion extends wheeled treads and a powerful long-range cannon. The cannon’s explosive shells demolish targets in a wide blast radius, but Bastion can only remain in this mode for a limited time.",
				"is_ultimate": true
		}
		],
		"rewards": [
		{
			"id": 71,
			"name": "Action",
			"cost": {
				"currency": "credit",
				"value": 25
			},
			"type": {
				"id": 1,
				"name": "spray"
			},
			"quality": {
				"name": "common"
			},
			"event": null
		}
		]
	}
	]
}

players = {
	"_request": {
		"api_ver": 3,
		"route": "/api/v3/u/Dad-12262/blob"
	},
	"kr": null,
	"eu": null,
	"us": {
		"stats": {
			"win_rate": 0,
			"level": 20,
			"prestige": 1,
			"avatar": "https://blzgdapipro-a.akamaihd.net/game/unlocks/0x0250000000000BBA.png",
			"wins": 373,
			"games": null,
			"comprank": 2395,
			"losses": null
		},
		"heroes": {
			"quickplay": {
				"junkrat": 7.0,
				"soldier76": 3.0,
				"hanzo": 0.8333333333333334,
				"bastion": 0.3333333333333333,
				"torbjorn": 6.0,
				"winston": 6.0,
				"dva": 0.5166666666666667,
				"ana": 0,
				"reinhardt": 16.0,
				"lucio": 3.0,
				"pharah": 8.0,
				"zenyatta": 1.0,
				"reaper": 0.2833333333333333,
				"zarya": 7.0,
				"mercy": 7.0,
				"symmetra": 4.0,
				"mccree": 3.0,
				"widowmaker": 3.0,
				"mei": 1.0,
				"tracer": 2.0,
				"roadhog": 8.0,
				"genji": 0.26666666666666666
			},
			"achievements": {
				"defense": {
					"ice_blocked": true,
					"triple_threat": false,
					"simple_geometry": false,
					"the_dragon_is_sated": false,
					"did_that_sting": true,
					"mine_like_a_steel_trap": true,
					"charge": false,
					"cold_snap": false,
					"raid_wipe": true,
					"armor_up": true,
					"roadkill": true,
					"smooth_as_silk": true
				},
				"offense": {
					"whoa_there": true,
					"die_die_die_die": false,
					"its_high_noon": false,
					"their_own_worst_enemy": false,
					"clearing_the_area": true,
					"target_rich_environment": true,
					"death_from_above": false,
					"total_recall": true,
					"rocket_man": false,
					"slice_and_dice": false,
					"special_delivery": false,
					"waste_not_want_not": false
				},
				"support": {
					"rapid_discord": false,
					"enabler": false,
					"huge_rez": true,
					"supersonic": true,
					"naptime": false,
					"huge_success": false,
					"the_iris_embraces_you": false,
					"the_car_wash": true,
					"the_floor_is_lava": false,
					"group_health_plan": true
				},
				"general": {
					"decorated": true,
					"blackjack": true,
					"centenary": true,
					"undying": true,
					"level_10": true,
					"the_path_is_closed": true,
					"level_50": true,
					"level_25": true,
					"decked_out": false,
					"survival_expert": false,
					"the_friend_zone": true
				},
				"tank": {
					"i_am_your_shield": true,
					"mine_sweeper": false,
					"storm_earth_and_fire": false,
					"giving_you_the_hook": true,
					"power_overwhelming": true,
					"anger_management": false,
					"hog_wild": true,
					"the_power_of_attraction": true,
					"shot_down": false,
					"game_over": false
				},
				"maps": {
					"world_traveler": true,
					"lockdown": true,
					"cant_touch_this": true,
					"shutout": true,
					"escort_duty": true,
					"double_cap": true
				}
			},
			"any": null
		}
	}
}

rewards = {
	"total": 2,
	"data": [
	{
		"id": 1,
		"name": "Logo",
		"cost": null,
		"type": {
			"id": 1,
			"name": "spray",
		},
		"quality": {
			"name": "common"
		}
	},
	{
		"id": 2,
		"name": "You Are Not Prepared!",
		"cost": null,
		"type": {
			"id": 1,
			"name": "spray",
		},
		"quality": {
			"name": "common"
		}
	}
	]
}

achievements = {
	"total": 2,
	"data": [
	{
		"id": 1,
		"name": "Level 10",
		"description": "Reach level 10.",
		"hero": null,
		"reward": {
			"id": 30,
			"name": "Forge Onward",
			"cost": null,
			"type": {
				"id": 1,
				"name": "spray"
			},
			"quality": {
				"name": "common"
			}
		}
	},
	{
		"id": 2,
		"name": "Level 25",
		"description": "Reach level 25.",
		"hero": null,
		"reward": {
			"id": 40,
			"name": "Rise",
			"cost": null,
			"type": {
				"id": 1,
				"name": "spray"
			},
			"quality": {
				"name": "common"
			}
		}
	}
	]
}

@app.route('/api/heroes', methods=['GET'])
def get_heroes():
    return jsonify({'heroes': heroes})
	
@app.route('/api/heroes/<int:hero_id>', methods=['GET'])
def get_hero(hero_id):
	for (h in heroes['objects']):
		if (h['id'] == hero_id)
			return jsonify(h)
	abort(404)
	
@app.route('api/players/<player_id>', methods=['GET'])
def get_player(player_id):
	return jsonify(players)

@app.route('/api/rewards', methods=['GET'])
def get_rewards():
    return jsonify(rewards)
	
@app.route('/api/rewards/<int:reward_id>', methods=['GET'])
def get_reward(reward_id):
	for (r in rewards['data']):
		if (r['id'] == reward_id)
			return jsonify(r)
	abort(404)

@app.route('/api/achievements', methods=['GET'])
def get_achievements():
    return jsonify(achievements)
	
@app.route('/api/achievements/<int:achievement_id>', methods=['GET'])
def get_achievement(achievement_id):
	for (a in achievements['data']):
		if (a['id'] == achievement_id)
			return jsonify(a)
	abort(404)
	
if __name__ == '__main__':
    app.run()
