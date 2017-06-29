''' Modules related to the application '''

from flask import Flask, jsonify

from views import views

app = Flask(__name__)

app.register_blueprint(views)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/api/heroes', methods=['GET'])
def get_heroes():
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.run()
