#!/usr/bin/env python3

def famous_births(persons):
    # sort dictionary by date_of_birth
    sorted_people = sorted(
        persons.values(),
        key=lambda person: person["date_of_birth"]
    )

    for person in sorted_people:
        print(f"{person['name']} is a great scientist born in {person['date_of_birth']}.")

scientists = {
    "a": {"name": "AB", "date_of_birth": 1995},
    "c": {"name": "CD", "date_of_birth": 1997},
    "l": {"name": "LM", "date_of_birth": 2000},
    "g": {"name": "GH", "date_of_birth": 2002}
}

famous_births(scientists)