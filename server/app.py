from flask import Flask, jsonify, request
from flask_cors import CORS

#importing code that I wrote
# from data import *

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

#This roue
@app.route('/firstQuestionData', methods=['GET', 'POST'])
def DeathData():
    if request.method == 'POST':
        # data = Data()
        post_data = request.get_json()
        state = post_data['state']
        orientation = post_data['orientation']
        # death_Selector = post_data['deathSelector']
        # all_Death_Data = data.allDeathsByDate(first_date, last_date, death_Selector)
        return jsonify('Hi')


if __name__ == '__main__':
    app.run()
