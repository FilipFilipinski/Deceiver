from dataclasses import dataclass


@dataclass
class Name:
    name: str
    sex: str
    number_of_appearances: int


@dataclass
class LastName:
    lastname: str
    number_of_appearances: int


def list_of_name(sex: str) -> list:
    with open(f'data/data_{sex}.csv') as f:
        csv = f.readlines()[1:]
        names = []
        for i in csv:
            i = i.strip().split(',')
            i[1] = 'Male' if i[1] == 'MĘŻCZYZNA' else 'Female'
            names.append(Name(*i))
    return names


def list_of_last_name(sex: str) -> list:
    with open(f'data/lastname_{sex}.csv') as f:
        csv = f.readlines()[1:]
        last_name = []
        for i in csv:
            last_name.append(LastName(*i.strip().split(',')))
    return last_name
