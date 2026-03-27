from importlib.metadata import version

import jellyfish

from .country_data import departments
from .services import (
    get_department,
    get_center_of_population,
    get_department_by_coordinadora_location,
    separate_coordinadora_department_code_and_city,
)

__version__ = version("danecode")


def get_data(department: str, municipality: str) -> dict:
    if not department or not isinstance(department, str):
        raise ValueError("department must be a non-empty string")
    if not municipality or not isinstance(municipality, str):
        raise ValueError("municipality must be a non-empty string")

    department = department.lower()
    municipality = municipality.lower()

    department = get_less_distant_item(department, departments.keys())

    municipalities = departments[department]["municipalities"]
    municipality = get_less_distant_item(municipality, municipalities.keys())

    dane_code = departments[department]["municipalities"][municipality]["dane_code"]

    return {
        "department": department,
        "department_code": departments[department]["dane_code"],
        "municipality": municipality,
        "municipality_code": dane_code,
    }


def get_less_distant_item(to_compare: str, options) -> str:
    last_distance = None

    for option in options:
        distance = jellyfish.levenshtein_distance(to_compare, option)

        if last_distance is None:
            last_distance = distance
        elif distance > last_distance:
            continue

        last_distance = distance
        best_value = option

    return best_value


def coordinadora_center_of_population(coordinadora_location: str) -> dict:
    if not coordinadora_location or not isinstance(coordinadora_location, str):
        raise ValueError("coordinadora_location must be a non-empty string")
    if "(" not in coordinadora_location:
        raise ValueError("coordinadora_location must be in format 'CITY (DEPT_CODE)'")

    (
        center_of_population_name,
        department_code,
    ) = separate_coordinadora_department_code_and_city(coordinadora_location)
    department = get_department_by_coordinadora_location(department_code)
    if department is None:
        raise ValueError(f"Unknown coordinadora department code: {department_code}")
    departamento_data = get_department(department)
    center_of_population = get_center_of_population(
        center_of_population_name, departamento_data["code"]
    )
    return center_of_population
