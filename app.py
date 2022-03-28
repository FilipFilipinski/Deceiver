from flask import Flask
from get_data import list_of_name, list_of_last_name, phone_number, list_country
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
    person = [random.choice(list_of_name(gender)), random.choice(list_of_last_name(gender)),
              random.choice(list_country())]
    return {'name': rs(person[0].name), 'last_name': rs(person[1].lastname), 'sex': rs(person[0].sex),
            'phone': phone_number(), 'country': [person[2].country, person[2].short]}


if __name__ == '__main__':
    app.run()
