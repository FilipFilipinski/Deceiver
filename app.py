from flask import Flask
from get_data import list_of_name, list_of_lastname, phone_number, list_of_country
from models.person import Person
import random
import unidecode

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

sex = ["male", "female"]


def rs(x: str) -> str:
    # remove all the accents
    return unidecode.unidecode(x)


@app.route('/api/')
def random_person() -> dict:
    return Person().generate()


@app.route('/api/<quantity>')
def random_people_list(quantity) -> dict:
    # function returns false data depending on the given quantity
    try:
        quantity = int(quantity)
    except ValueError:
        quantity = 1
    return {'data': [random_person() for _ in range(1 if quantity <= 0 else quantity)]}


if __name__ == '__main__':
    app.run()
