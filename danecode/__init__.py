import jellyfish

from .country_data import departments


def get_data(department, municipality):

    department = get_less_distant_item(department, departments.keys())

    municipalities = departments[department]['municipalities']
    municipality = get_less_distant_item(municipality, municipalities.keys())


    dane_code =  departments[department]['municipalities']\
        [municipality]['dane_code']

    place_data = {
        "department":department,
        "department_code": departments[department]['dane_code'],
        "municipality":municipality,
        "municipality_code": dane_code,
    }

    return place_data


def get_less_distant_item(to_compare, options):
    last_distance = None

    for option in options:
        distance = jellyfish.levenshtein_distance(to_compare, option)

        if not last_distance:
            last_distance = distance
        elif last_distance < distance:
            continue
        
        last_distance = distance
        best_value = option

    return best_value
