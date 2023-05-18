import random
from dataclasses import dataclass
from models.country import Country
from get_data import list_of_name, list_of_lastname, phone_number, list_of_country


@dataclass
class Person:
    name: str = None
    last_name: str = None
    phone: int = None
    sex: str = None
    country: Country = None

    def generate(self):
        sex = ["male", "female"]

        self.sex = random.choice(sex)
        self.name = random.choice(list_of_name(self.sex))
        self.last_name = random.choice(list_of_lastname(self.sex))
        self.phone = phone_number()
        self.country = random.choice(list_of_country())

        return self
