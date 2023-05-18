from dataclasses import dataclass
from models.lastname import LastName
from models.country import Country
from models.name import Name
from functools import cache
import random


@cache
def list_of_name(sex: str) -> list:
    with open(f'data/data_{sex}.csv') as f:
        names = []
        for i in f.readlines()[1:]:
            i = i.strip().split(',')
            i[1] = 'Male' if i[1] == 'MĘŻCZYZNA' else 'Female'
            names.append(Name(*i).name)
    return names


@cache
def list_of_lastname(sex: str) -> list:
    with open(f'data/lastname_{sex}.csv') as f:
        return [LastName(*lastname.strip().split(',')).lastname for lastname in f.readlines()[1:]]


@cache
def list_of_country() -> list:
    with open('data/country.csv') as f:
        return [Country(*name.strip().split(',')) for name in f.readlines()[1:]]


def phone_number() -> int:
    return int("".join([str(random.randint(0, 9)) for _ in range(9)]))
