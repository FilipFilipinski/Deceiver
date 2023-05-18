from dataclasses import dataclass


@dataclass
class Name:
    name: str
    sex: str
    number_of_appearances: int