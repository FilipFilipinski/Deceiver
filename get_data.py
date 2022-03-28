from dataclasses import dataclass


@dataclass
class Name:
    name: str
    sex: str
    number_of_appearances: int


def list_od_name(sex: str) -> list:
    with open(f'data/data_{sex}.csv') as f:
        csv = f.readlines()[1:]
        name = []
        for i in csv:
            name.append(Name(*i.strip().split(',')))
    return name



