from dataclasses import dataclass
from functools import cache
import random


@dataclass
class Name:
    name: str
    sex: str
    number_of_appearances: int


@dataclass
class LastName:
    lastname: str
    number_of_appearances: int


@dataclass
class Country:
    country: str
    short: int


@cache
def list_of_name(sex: str) -> list:
    with open(f'data/data_{sex}.csv') as f:
        names = []
        for i in f.readlines()[1:]:
            i = i.strip().split(',')
            i[1] = 'Male' if i[1] == 'MĘŻCZYZNA' else 'Female'
            names.append(Name(*i))
    return names


@cache
def list_of_lastname(sex: str) -> list:
    with open(f'data/lastname_{sex}.csv') as f:
        return [LastName(*lastname.strip().split(',')) for lastname in f.readlines()[1:]]


@cache
def list_of_country() -> list:
    with open('data/country.csv') as f:
        return [Country(*name.strip().split(',')) for name in f.readlines()[1:]]


def phone_number() -> str:
    return "".join([str(random.randint(0, 9)) for _ in range(9)])
