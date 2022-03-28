from flask import Flask
from get_data import list_of_name, list_of_last_name, phone_number
import random
import unidecode

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

sex = ['male', 'female']


def rs(x: str) -> str:
    # remove all the accents
    return unidecode.unidecode(x)


@app.route('/')
def random_person():
    gender = random.choice(sex)
    person = [random.choice(list_of_name(gender)), random.choice(list_of_last_name(gender))]
    return {'name': rs(person[0].name), 'last_name': rs(person[1].lastname), 'sex': rs(person[0].sex),
            'phone': phone_number()}


if __name__ == '__main__':
    app.run()
