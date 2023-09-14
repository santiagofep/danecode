import os
import logging

import pandas as pd
from unidecode import unidecode

import jellyfish

logger = logging.getLogger("__name__")
module_dir = os.path.dirname(__file__)


def get_departament(received_departamento):
    received_departamento = unidecode(received_departamento.upper())

    file_path = os.path.join(module_dir, "../files/departamentos.csv")

    data = pd.read_csv(file_path, converters={"code": str})
    departamentos = data.to_dict("records")

    min_distance = {"value": float("inf"), "departamento": {}}
    for departamento in departamentos:
        departamento_to_compare = unidecode(departamento["name"])
        distance = jellyfish.levenshtein_distance(
            received_departamento, departamento_to_compare
        )
        if distance < min_distance["value"]:
            min_distance = {"value": distance, "departamento": departamento}
    return min_distance["departamento"]


def get_center_of_population(received_centro_poblado, departamento_code):
    received_centro_poblado = unidecode(received_centro_poblado.upper())
    file_path = os.path.join(
        module_dir, f"../files/centros_poblados/{departamento_code}.csv"
    )

    data = pd.read_csv(
        file_path,
        converters={
            "codigo_departamento": str,
            "codigo_municipio": str,
            "codigo_centro_poblado": str,
        },
    )
    centros_poblados = data.to_dict("records")

    min_distance = {"value": float("inf"), "centro_poblado": {}}
    for centro_poblado in centros_poblados:
        centro_poblado_to_compare = unidecode(centro_poblado["nombre_centro_poblado"])
        distance = jellyfish.levenshtein_distance(
            received_centro_poblado, centro_poblado_to_compare
        )
        if distance < min_distance["value"]:
            min_distance = {"value": distance, "centro_poblado": centro_poblado}

    return min_distance["centro_poblado"]


def separate_coordinadora_department_code_and_city(location):
    city, department_code = location.split("(")
    if department_code:
        department_code = department_code.replace(")", "")
    return city.lower(), department_code


def get_department_by_coordinadora_location(department_code):
    departments = {
        "ANT": "Antioquia",
        "N/STDER": "Norte de Santander",
        "META": "Meta",
        "STDER": "Santander",
        "HLA": "Huila",
        "BOL": "Bolivar",
        "C/MARCA": "Cundinamarca",
        "CES": "Cesar",
        "C/NARE": "Casanare",
        "CDAS": "Caldas",
        "CAQ": "Caqueta",
        "GUAJ": "La Guajira",
        "VALLE": "Valle",
        "NAR": "Nariño",
        "MG/LENA": "Magdalena",
        "CAU": "Cauca",
        "BOY": "Boyaca",
        "TOL": "Tolima",
        "CHOCO": "Choco",
        "RS": "Risaralda",
        "ARAU": "Arauca",
        "QDIO": "Quindio",
        "ATL": "Atlantico",
        "CORD": "Cordoba",
        "P/MAYO": "Putumayo",
        "SUCRE": "Sucre",
        "VICH": "Vichada",
        "GUAI": "Guainia",
        "AMAZ": "Amazonas",
        "V/PES": "Vaupes",
        "S/ANDRES": "SAN ANDRÉS, PROVIDENCIA Y SANTA CATALINA",
        "G/VIARE": "Guaviare",
    }

    if department_code in departments:
        return departments[department_code].lower()
    else:
        return None
