import jellyfish

from .country_data import departments
from .services import (
    get_departament,
    get_center_of_population,
    get_department_by_coordinadora_location,
    separate_coordinadora_department_code_and_city,
)


def get_data(department, municipality):
    department = department.lower()
    municipality = municipality.lower()

    department = get_less_distant_item(department, departments.keys())

    municipalities = departments[department]["municipalities"]
    municipality = get_less_distant_item(municipality, municipalities.keys())

    dane_code = departments[department]["municipalities"][municipality]["dane_code"]

    place_data = {
        "department": department,
        "department_code": departments[department]["dane_code"],
        "municipality": municipality,
        "municipality_code": dane_code,
    }

    return place_data


def get_less_distant_item(to_compare, options):
    last_distance = None

    for option in options:
        distance = jellyfish.levenshtein_distance(to_compare, option)

        if last_distance == None:
            last_distance = distance
        elif distance > last_distance:
            continue

        last_distance = distance
        best_value = option

    return best_value


def coordinadora_center_of_population(coordinadora_location):
    (
        center_of_population_name,
        department_code,
    ) = separate_coordinadora_department_code_and_city(coordinadora_location)
    department = get_department_by_coordinadora_location(department_code)
    departamento_data = get_departament(department)
    center_of_population = get_center_of_population(
        center_of_population_name, departamento_data["code"]
    )
    return center_of_population
