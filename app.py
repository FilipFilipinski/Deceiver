from flask import Flask
from get_data import list_of_name
import random

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

sex = ['male', 'female']


@app.route('/')
def random_person():  # put application's code here
    person = random.choice(list_of_name(random.choice(sex)))
    return {'name': person.name, 'last_name': 'lastname', 'sex': person.sex}


if __name__ == '__main__':
    app.run()
