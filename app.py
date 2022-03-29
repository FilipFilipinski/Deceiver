from flask import Flask
from get_data import list_of_name, list_of_lastname, phone_number, list_of_country
import random
import unidecode

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

sex = ['male', 'female']


def rs(x: str) -> str:
    # remove all the accents
    return unidecode.unidecode(x)


@app.route('/api/')
def random_person() -> dict:
    gender = random.choice(sex)
    person = [random.choice(list_of_name(gender)), random.choice(list_of_lastname(gender)),
              random.choice(list_of_country())]
    return {'name': rs(person[0].name), 'last_name': rs(person[1].lastname), 'sex': rs(person[0].sex),
            'phone': phone_number(), 'country': person[2]}


@app.route('/api/<quantity>')
def random_people_list(quantity) -> dict:
    # function returns false data depending on the given quantity
    try:
        quantity = int(quantity)
    except ValueError:
        print(ValueError)
        quantity = 1
    x = [random_person() for _ in range(quantity)]
    return {'data': x}


if __name__ == '__main__':
    app.run()
