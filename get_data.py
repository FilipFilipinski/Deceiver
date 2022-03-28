from dataclasses import dataclass


@dataclass
class Name:
    name: str
    sex: str
    number_of_appearances: int


def list_of_name(sex: str) -> list:
    with open(f'data/data_{sex}.csv') as f:
        csv = f.readlines()[1:]
        names = []
        for i in csv:
            names.append(Name(*i.strip().split(',')))
    return names



